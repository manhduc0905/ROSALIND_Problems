import sys
import os

# --- 1. Data Structures -----------------------------------------------

class DSU:
    """Disjoint Set Union (Union-Find) class."""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        
    def find(self, i):
        """Find the root of the component for node i."""
        if self.parent[i] == i:
            return i
        # Path compression
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        """Merge the components of x and y."""
        xRoot = self.find(x)
        yRoot = self.find(y)
        
        if xRoot == yRoot:
            return False # They are already in the same set
        
        # Union by rank
        if self.rank[xRoot] < self.rank[yRoot]:
            self.parent[xRoot] = yRoot
        elif self.rank[xRoot] > self.rank[yRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[yRoot] = xRoot
            self.rank[xRoot] += 1
        return True

# --- 2. Pairwise Alignment (Needleman-Wunsch) -------------------------
# This function is used to build the initial distance matrix.

def get_pairwise_alignment(seq1, seq2):
    s1 = " " + seq1
    s2 = " " + seq2
    n = len(s1)
    m = len(s2)
    
    L = [[0 for _ in range(m)] for _ in range(n)]
    Trace = [["" for _ in range(m)] for _ in range(n)]

    d = 1 
    
    for i in range(1, n):
        L[i][0] = i * d
        Trace[i][0] = "U"
    for j in range(1, m):
        L[0][j] = j * d
        Trace[0][j] = "L"
        
    Trace[0][0] = "X"
    
    for i in range(1, n):
        for j in range(1, m):
            score_i_j = 0 if (s1[i] == s2[j]) else d
            
            diag = L[i-1][j-1] + score_i_j
            up   = L[i-1][j] + d
            left = L[i][j-1] + d
            
            min_dist = min(diag, up, left)
            L[i][j] = min_dist
            
            if min_dist == diag:
                Trace[i][j] = "D"
            elif min_dist == up:
                Trace[i][j] = "U"
            else:
                Trace[i][j] = "L"
                
    aligned_seq1 = ""
    aligned_seq2 = ""
    i, j = n - 1, m - 1 # Start at the bottom-right

    while i > 0 or j > 0: # Loop until we are at the top-left
        if i > 0 and j > 0 and Trace[i][j] == "D":
            aligned_seq1 = s1[i] + aligned_seq1
            aligned_seq2 = s2[j] + aligned_seq2
            i -= 1
            j -= 1
        elif i > 0 and (j == 0 or Trace[i][j] == "U"):
            aligned_seq1 = s1[i] + aligned_seq1
            aligned_seq2 = "-" + aligned_seq2
            i -= 1
        else: # j > 0 and (i == 0 or Trace[i][j] == "L")
            aligned_seq1 = "-" + aligned_seq1
            aligned_seq2 = s2[j] + aligned_seq2
            j -= 1

    return L[n-1][m-1], aligned_seq1, aligned_seq2

def build_profile(seqs):
    L = len(seqs[0]) if seqs else 0
    profile = []

    for i in range(L):
        freq = {c:0 for c in "ACGT-"}
        for s in seqs:
            if i < len(s): 
                freq[s[i]] += 1
        profile.append(freq)
    return profile


def col_score(c1, c2, match=0, mismatch=1, gap_char=1):
    """
    Scores two profile columns (frequency dicts) using SOP.
    """
    score = 0
    for x in "ACGT": # Only iterate over real characters
        for y in "ACGT":
            # Add match/mismatch score
            score += (c1[x] * c2[y]) * (match if x == y else mismatch)
        
        # Add gap penalties
        score += (c1[x] * c2['-']) * gap_char # x vs. gap
        score += (c1['-'] * c2[x]) * gap_char # gap vs. x
        
    # score(gap, gap) is 0
    return score


def profile_profile_dp(p1, p2, N1, N2):
    """
    Needleman–Wunsch on two profiles (p1, p2) using Sum-of-Pairs.
    N1, N2: Number of sequences in each profile.
    """
    n = len(p1)
    m = len(p2)

    DP = [[0]*(m+1) for _ in range(n+1)]
    TR = [[""]*(m+1) for _ in range(n+1)]

    # Scoring parameters
    match = 0
    mismatch = 1
    gap_penalty = 1 # This is the gap-char penalty

    # Create frequency dicts for "all gap" columns
    gap_col_1 = {c: 0 for c in "ACGT-"}
    gap_col_1['-'] = N1
    
    gap_col_2 = {c: 0 for c in "ACGT-"}
    gap_col_2['-'] = N2

    # Initialize DP table
    for i in range(1, n+1):
        DP[i][0] = DP[i-1][0] + col_score(p1[i-1], gap_col_2, match, mismatch, gap_penalty)
        TR[i][0] = "U"
    for j in range(1, m+1):
        DP[0][j] = DP[0][j-1] + col_score(gap_col_1, p2[j-1], match, mismatch, gap_penalty)
        TR[0][j] = "L"

    # Fill the DP table
    for i in range(1, n+1):
        for j in range(1, m+1):
            d = DP[i-1][j-1] + col_score(p1[i-1], p2[j-1], match, mismatch, gap_penalty)
            u = DP[i-1][j] + col_score(p1[i-1], gap_col_2, match, mismatch, gap_penalty)
            l = DP[i][j-1] + col_score(gap_col_1, p2[j-1], match, mismatch, gap_penalty)
            
            # Use min() because we are calculating distances/penalties
            DP[i][j], TR[i][j] = min((d, "D"), (u, "U"), (l, "L"))

    actions = []
    i, j = n, m
    while i > 0 or j > 0:
        move = TR[i][j]
        if i > 0 and j > 0 and move == "D":
            actions.append("D")
            i -= 1
            j -= 1
        elif i > 0 and (j == 0 or move == "U"):
            actions.append("U")
            i -= 1
        else: # j > 0 and (i == 0 or move == "L")
            actions.append("L")
            j -= 1

    return actions[::-1] # Return actions from start to finish

def apply_profile_actions(seqs1, seqs2, actions):
    new1 = [""] * len(seqs1)
    new2 = [""] * len(seqs2)

    i = j = 0 # Pointers to columns in original profiles

    for a in actions:
        if a == "D":
            # take next column from each profile
            for k in range(len(seqs1)):
                new1[k] += seqs1[k][i]
            for k in range(len(seqs2)):
                new2[k] += seqs2[k][j]
            i += 1
            j += 1
        elif a == "U":
            # profile1 column; profile2 gets gap column
            for k in range(len(seqs1)):
                new1[k] += seqs1[k][i]
            for k in range(len(seqs2)):
                new2[k] += "-"
            i += 1
        elif a == "L":
            # profile2 column; profile1 gets gap column
            for k in range(len(seqs1)):
                new1[k] += "-"
            for k in range(len(seqs2)):
                new2[k] += seqs2[k][j]
            j += 1
            
    # Return the merged set of new, aligned sequences
    return new1 + new2

def profile_profile_alignment(seqs1, seqs2):
    """
    Wrapper function to align two profiles.
    """
    p1 = build_profile(seqs1)
    p2 = build_profile(seqs2)
    N1 = len(seqs1)
    N2 = len(seqs2)

    actions = profile_profile_dp(p1, p2, N1, N2)
    return apply_profile_actions(seqs1, seqs2, actions)

# --- 4. Final Score Calculation ---------------------------------------

def get_sop_score(aligned_sequences, match=0, mismatch=1, gap_char=1):
    """
    Calculates the Sum-of-Pairs (SOP) *distance* for a final alignment.
    """
    if not aligned_sequences:
        return 0
    
    num_seqs = len(aligned_sequences)
    align_len = len(aligned_sequences[0])
    total_score = 0

    for j in range(align_len): # Loop over each column
        col_score = 0
        for i in range(num_seqs): # Loop over every unique pair
            for k in range(i + 1, num_seqs):
                char1 = aligned_sequences[i][j]
                char2 = aligned_sequences[k][j]
                
                if char1 == '-' and char2 == '-':
                    pass # gap-gap score is 0
                elif char1 == '-' or char2 == '-':
                    col_score += gap_char # e.g., +1
                elif char1 == char2:
                    col_score += match # e.g., +0
                else:
                    col_score += mismatch # e.g., +1
        total_score += col_score
    
    return total_score

# --- 5. Main Execution ------------------------------------------------

# Read sequences from file
input_path = r"C:\Users\admin\OneDrive - Grinnell College\Documents\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
f1 = open(input_path, 'r')
seq = []
temp = ""
for line in f1:
    if line.startswith('>'):
        if (temp != ""):
            seq.append(temp)
        temp = ""   
    else:
        temp += line.strip()
if (temp != ""):
    seq.append(temp)
f1.close()

def build_edge_list(seqs):
    edge_list = []
    for i in range(len(seqs)):
        for j in range(i + 1, len(seqs)):
            dist, _, _ = get_pairwise_alignment(seqs[i], seqs[j])
            edge_list.append((dist, i, j))
            
    edge_list.sort() 
    return edge_list

graph_edges = build_edge_list(seq)

N = len(seq)
dsu = DSU(N)

cls = {i: [seq[i]] for i in range(N)}

edge_count = 0
for (dist, node1, node2) in graph_edges:
    root1 = dsu.find(node1)
    root2 = dsu.find(node2)
    
    if root1 != root2:	
        profile1 = cls[root1]
        profile2 = cls[root2]
        
        new_merged_profile = profile_profile_alignment(profile1, profile2)
        
        dsu.union(root1, root2)
        
        new_root = dsu.find(root1)
        
        cls[new_root] = new_merged_profile
        if new_root != root1: del cls[root1]
        if new_root != root2: del cls[root2]

        edge_count += 1
        if edge_count == N - 1:
            break
            
final_root = dsu.find(0)
final_alignment = cls[final_root]

final_score = get_sop_score(final_alignment)
print(-final_score)

for s in final_alignment:
    print(s)