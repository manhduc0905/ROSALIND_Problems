import sys

# --- Matrix Parsing ---
raw_matrix = """
  A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y
A  4  0 -2 -1 -2  0 -2 -1 -1 -1 -1 -2 -1 -1 -1  1  0  0 -3 -2
C  0  9 -3 -4 -2 -3 -3 -1 -3 -1 -1 -3 -3 -3 -3 -1 -1 -1 -2 -2
D -2 -3  6  2 -3 -1 -1 -3 -1 -4 -3  1 -1  0 -2  0 -1 -3 -4 -3
E -1 -4  2  5 -3 -2  0 -3  1 -3 -2  0 -1  2  0  0 -1 -2 -3 -2
F -2 -2 -3 -3  6 -3 -1  0 -3  0  0 -3 -4 -3 -3 -2 -2 -1  1  3
G  0 -3 -1 -2 -3  6 -2 -4 -2 -4 -3  0 -2 -2 -2  0 -2 -3 -2 -3
H -2 -3 -1  0 -1 -2  8 -3 -1 -3 -2  1 -2  0  0 -1 -2 -3 -2  2
I -1 -1 -3 -3  0 -4 -3  4 -3  2  1 -3 -3 -3 -3 -2 -1  3 -3 -1
K -1 -3 -1  1 -3 -2 -1 -3  5 -2 -1  0 -1  1  2  0 -1 -2 -3 -2
L -1 -1 -4 -3  0 -4 -3  2 -2  4  2 -3 -3 -2 -2 -2 -1  1 -2 -1
M -1 -1 -3 -2  0 -3 -2  1 -1  2  5 -2 -2  0 -1 -1 -1  1 -1 -1
N -2 -3  1  0 -3  0  1 -3  0 -3 -2  6 -2  0  0  1  0 -3 -4 -2
P -1 -3 -1 -1 -4 -2 -2 -3 -1 -3 -2 -2  7 -1 -2 -1 -1 -2 -4 -3
Q -1 -3  0  2 -3 -2  0 -3  1 -2  0  0 -1  5  1  0 -1 -2 -2 -1
R -1 -3 -2  0 -3 -2  0 -3  2 -2 -1  0 -2  1  5 -1 -1 -3 -3 -2
S  1 -1  0  0 -2  0 -1 -2  0 -2 -1  1 -1  0 -1  4  1 -2 -3 -2
T  0 -1 -1 -1 -2 -2 -2 -1 -1 -1 -1  0 -1 -1 -1  1  5  0 -2 -2
V  0 -1 -3 -2 -1 -3 -3  3 -2  1  1 -3 -2 -2 -3 -2  0  4 -3 -1
W -3 -2 -4 -3  1 -2 -2 -3 -3 -2 -1 -4 -4 -2 -3 -3 -2 -3 11  2
Y -2 -2 -3 -2  3 -3  2 -1 -2 -1 -1 -2 -3 -1 -2 -2 -2 -1  2  7
"""

def parse_matrix(raw):
    rows = [r.strip() for r in raw.strip().split("\n")]
    headers = rows[0].split()
    matrix = {}
    for row in rows[1:]:
        parts = row.split()
        aa = parts[0]
        scores = list(map(int, parts[1:]))
        matrix[aa] = dict(zip(headers, scores))
    return matrix

BLOSUM62 = parse_matrix(raw_matrix)
g_ext = 1
g_open = 11

# --- Constants for Bit Packing ---
# We use 2 bits per state decision to save memory
# 0: Match, 1: Upper, 2: Left, 3: STOP (0)
STOP = 3
MATCH = 0
UPPER = 1
LEFT = 2

def linear_space_alignment(seq1, seq2, output_file):
    n = len(seq1)
    m = len(seq2)

    # Memory Optimization:
    # We DO NOT store the full score matrix (which would be 3 * 10k * 10k ints).
    # We ONLY store the current and previous rows of scores.
    # We DO store the full Traceback matrix, but packed into bytearrays (1 byte per cell).
    
    # Initialize Score Rows
    # [0] = Match, [1] = Upper, [2] = Left
    prev_scores = [[0, -float('inf'), -float('inf')] for _ in range(m + 1)]
    curr_scores = [[0, 0, 0] for _ in range(m + 1)]

    # Trace Matrix: List of bytearrays
    # Each byte stores decisions for all 3 states:
    # Bits 0-1: Source for Match state
    # Bits 2-3: Source for Upper state
    # Bits 4-5: Source for Left state
    trace_matrix = []

    # Track Global Max for Local Alignment
    max_score = -1
    max_pos = (0, 0, 0) # (i, j, state)

    # --- Forward Pass ---
    print("Computing Alignment Matrix...")
    
    # Pre-calculate row 0 trace (all STOPs)
    # trace_matrix.append(bytearray([ (STOP | (STOP << 2) | (STOP << 4)) ] * (m + 1)))
    # Actually, row 0 logic is handled implicitly by the loop bounds or checks, 
    # but for local alignment starting at 0,0 is valid.
    # Let's just push the first row of traces (all zeros/stops)
    trace_matrix.append(bytearray([(STOP | (STOP << 2) | (STOP << 4))] * (m + 1)))

    for i in range(1, n + 1):
        char1 = seq1[i-1]
        
        # Create a new bytearray row for traces
        curr_trace_row = bytearray(m + 1)
        
        # Initialize Column 0 scores
        curr_scores[0] = [0, -float('inf'), -float('inf')]
        # Trace for Col 0 is all STOP (handled by bytearray default 0, but lets be explicit if needed)
        # 0|0|0 is Match->Match(0), Up->Match(0)... wait.
        # STOP is 3. So we set it to 3|3<<2|3<<4 = 63
        curr_trace_row[0] = (STOP | (STOP << 2) | (STOP << 4))

        for j in range(1, m + 1):
            char2 = seq2[j-1]
            score_match = BLOSUM62[char1][char2]

            # --- 1. Calculate Match State (State 0) ---
            # Sources: Match(0), Upper(1), Left(2), or Reset(STOP/3)
            
            m_from_m = prev_scores[j-1][0] + score_match
            m_from_u = prev_scores[j-1][1] + score_match
            m_from_l = prev_scores[j-1][2] + score_match
            
            # Find max for Match state
            # Priority: 0 (Local Reset) -> Match -> Upper -> Left (arbitrary tie-break)
            best_m_val = 0
            best_m_src = STOP
            
            if m_from_m >= best_m_val:
                best_m_val = m_from_m
                best_m_src = MATCH
            if m_from_u > best_m_val: # Strict > prefers Match on ties
                best_m_val = m_from_u
                best_m_src = UPPER
            if m_from_l > best_m_val:
                best_m_val = m_from_l
                best_m_src = LEFT
            
            curr_scores[j][0] = best_m_val

            # --- 2. Calculate Upper Gap State (State 1) ---
            # Vertical: Depends on PREVIOUS row [i-1][j]
            # Sources: Match(0)-Open, Upper(1)-Extend, Left(2)-Switch
            
            u_open_m = prev_scores[j][0] - g_open
            u_ext_u  = prev_scores[j][1] - g_ext
            u_open_l = prev_scores[j][2] - g_open
            
            best_u_val = 0 # Local reset possible? Usually Gap doesn't reset to 0 directly, but score can be 0
            best_u_src = STOP
            
            # Check Reset first (if score < 0, clamp to 0)
            if u_open_m >= 0:
                best_u_val = u_open_m
                best_u_src = MATCH
            if u_ext_u >= best_u_val: # Extension usually preferred or equal
                best_u_val = u_ext_u
                best_u_src = UPPER
            if u_open_l > best_u_val:
                best_u_val = u_open_l
                best_u_src = LEFT
                
            curr_scores[j][1] = best_u_val

            # --- 3. Calculate Left Gap State (State 2) ---
            # Horizontal: Depends on CURRENT row [i][j-1]
            
            l_open_m = curr_scores[j-1][0] - g_open
            l_open_u = curr_scores[j-1][1] - g_open
            l_ext_l  = curr_scores[j-1][2] - g_ext
            
            best_l_val = 0
            best_l_src = STOP
            
            if l_open_m >= 0:
                best_l_val = l_open_m
                best_l_src = MATCH
            if l_open_u > best_l_val:
                best_l_val = l_open_u
                best_l_src = UPPER
            if l_ext_l >= best_l_val:
                best_l_val = l_ext_l
                best_l_src = LEFT
                
            curr_scores[j][2] = best_l_val

            # --- Check Global Max ---
            if curr_scores[j][0] > max_score:
                max_score = curr_scores[j][0]
                max_pos = (i, j, 0)
            if curr_scores[j][1] > max_score:
                max_score = curr_scores[j][1]
                max_pos = (i, j, 1)
            if curr_scores[j][2] > max_score:
                max_score = curr_scores[j][2]
                max_pos = (i, j, 2)

            # --- Pack Bits ---
            # Format: | Left_Src (2) | Upper_Src (2) | Match_Src (2) |
            packed_trace = (best_m_src) | (best_u_src << 2) | (best_l_src << 4)
            curr_trace_row[j] = packed_trace

        # Store trace row and swap score rows
        trace_matrix.append(curr_trace_row)
        prev_scores = [row[:] for row in curr_scores] # Deep copy values

    # --- Traceback ---
    print(f"T{max_score}\n")
    output_file.write(f"{max_score}\n")
    
    align1 = ""
    align2 = ""
    
    curr_i, curr_j, curr_state = max_pos
    
    while True:
        # Check stop condition (Hit origin or Hit Local Alignment 0-score boundary)
        # Note: We don't have the score matrix anymore to check '== 0', 
        # but we stored 'STOP' (3) in the trace matrix when score reset to 0.
        
        packed = trace_matrix[curr_i][curr_j]
        
        # Extract source for the CURRENT state
        src = (packed >> (curr_state * 2)) & 3
        
        if src == STOP:
            break
            
        if curr_state == MATCH: # State 0
            # Came from (i-1, j-1)
            align1 = seq1[curr_i-1] + align1
            align2 = seq2[curr_j-1] + align2
            curr_i -= 1
            curr_j -= 1
            curr_state = src # Update state to what it was BEFORE
            
        elif curr_state == UPPER: # State 1 (Vertical)
            # Came from (i-1, j)
            align1 = seq1[curr_i-1] + align1
            #align2 = "-" + align2
            curr_i -= 1
            # curr_j stays same
            curr_state = src
            
        elif curr_state == LEFT: # State 2 (Horizontal)
            # Came from (i, j-1)
            #align1 = "-" + align1
            align2 = seq2[curr_j-1] + align2
            # curr_i stays same
            curr_j -= 1 
            curr_state = src

    print(align1)
    print(align2)
    output_file.write(f"{align1}\n{align2}")

# --- Execution ---
input_path = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
s = ""
seq = []

try:
    with open(input_path, 'r') as f1, open("output.OUT", 'w') as f2:
        for line in f1:
            line = line.strip()
            if line.startswith('>'):
                if s != "":
                    seq.append(s)
                    s = ""
            else:
                s += line
        if s: seq.append(s)

        if len(seq) >= 2:
            linear_space_alignment(seq[0], seq[1], f2)
            
except Exception as e:
    print(f"Error: {e}")