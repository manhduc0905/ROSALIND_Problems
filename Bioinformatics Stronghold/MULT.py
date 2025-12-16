import sys
import os
input_path = input_path =  r"C:\Users\admin\OneDrive - Grinnell College\Documents\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
#print(input_path)
f1 = open(input_path,'r')
f2 = open('output.OUT','w')
seq = []
temp = ""
graph = []
class LeafNode:
    def __init__(self, seq):
        self.seq = seq
        
class AlignmentProfile:
    def __init__(self, sequences):
        self.sequences = sequences
        self.length = len(sequences[0]) if sequences else 0
        self.count = len(sequences)
        
class DSU:
    def __init__(self,n):
        self.rank = [0]*n
        self.parent = list(range(n))
    def find(self, i):
        root = self.parent[i]
        
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i]) # Path compression
        return self.parent[i]
        
    def union(self,x,y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        
        if (xRoot == yRoot):
            return
        
        if self.rank[xRoot]< self.rank[yRoot]:
            self.parent[xRoot] = yRoot
        elif self.rank[xRoot] > self.rank[yRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[yRoot] = xRoot
            self.rank[xRoot] += 1
    
        
def printM(matrix, seq1, seq2):
    n = len(seq1)
    m = len(seq2)
    for i in range(n):
        if (i == 0):
            print(" ", end = " ")
            for j in range(m):
                print(seq2[j], end = " ")
            print()
        for j in range(m):
            if (j == 0):
                print(seq1[i], end = " ")
            print(matrix[i][j], end = " ")
        print()
    
for line in f1:
    if line.startswith('>'):
        if (temp != ""):
            seq.append(temp)
        temp = ""   
    else:
        temp += line.strip()
if (temp != ""):
    seq.append(temp)

def global_alignment(seq1,seq2):
    #print(seq1,seq2)
    seq1 = " " + seq1
    seq2 = " " + seq2

    n = len(seq1)
    m = len(seq2)
    
    L = [[0 for _ in range(m)] for _ in range(n)]
    Trace = [["" for _ in range(m)] for _ in range(n)]
    #printM(L,seq1,seq2)
    #Needleman-Wunsch
    d = -1
    for i in range(1,n):
        L[i][0] = L[i-1][0] -d
        Trace[i][0] = "U"
    for j in range(1,m):
        L[0][j] = L[0][j-1] -d
        Trace[0][j] = "L"
    
    Trace[0][0] = "X"
    
    
    for i in range(1,n):
        for j in range(1,m):
            score_i_j = 0 if (seq1[i] == seq2[j]) else -d
            min_align = min((L[i-1][j-1] + score_i_j, "D"), (L[i-1][j] - d, "U"), (L[i][j-1] -d, "L"))
            L[i][j],Trace[i][j] = min_align
            
                
   # print(abs(L[n-1][m-1]))	
    #printM(L,seq1,seq2)		
    i1 = n-1
    j1 = m-1
    aligned_seq1 = ""
    aligned_seq2 = ""
    while (i1 != 0) and (j1 != 0):
        if (Trace[i1][j1] == 'L'):
            aligned_seq1 = "-" + aligned_seq1
            aligned_seq2 = seq2[j1] + aligned_seq2
            j1-=1
        elif (Trace[i1][j1] == 'U'):
            aligned_seq1 = seq1[i1] + aligned_seq1
            aligned_seq2 = "-" + aligned_seq2
            i1-=1
        else:
            aligned_seq1 = seq1[i1] + aligned_seq1
            aligned_seq2 = seq2[j1] + aligned_seq2
            i1-=1
            j1-=1
    print(seq1, seq2)
    print(aligned_seq1)
    print(aligned_seq2)
    return L[n-1][m-1]
    
    
seq = sorted(seq, key = len, reverse = True)

def build_tree(seq):
    for i in range(len(seq)):
        for j in range(i+1,len(seq)):
            if (i != j):
                #print(i,j)
                dist = global_alignment(seq[i],seq[j])
                graph.append((dist,i,j))
                
def build_profile(seqs):
    """
    seqs: list of ALIGNED sequences (same length)
    returns: list of dicts giving column frequencies
    """
    L = len(seqs[0])
    profile = []

    for i in range(L):
        freq = {c:0 for c in "ACGT-"}
        for s in seqs:
            freq[s[i]] += 1
        profile.append(freq)

    return profile


def col_score(c1, c2, match=0, mismatch=1):
    """
    Scores two profile columns.
    """
    score = 0
    for x in "ACGT-":
        for y in "ACGT-":
            if x == "-" and y == "-":
                continue
            score += (c1[x] * c2[y]) * (match if x == y else mismatch)
    return score


def profile_profile_dp(p1, p2, N1, N2):
    """
    Needleman–Wunsch on two profiles using Sum-of-Pairs DISTANCE.
    
    p1, p2: The profiles (lists of frequency dicts)
    N1, N2: The number of sequences in prof1 and prof2
    """
    n = len(p1)
    m = len(p2)

    DP = [[0]*(m+1) for _ in range(n+1)]
    TR = [[""]*(m+1) for _ in range(n+1)]

    # --- THIS IS THE FIX ---
    # Define the scoring parameters (from your col_score)
    match = 0
    mismatch = 1
    gap_penalty = 1 # This is the gap-char penalty

    # Create frequency dicts for "all gap" columns
    # These are used to calculate the SOP gap score
    gap_col_1 = {c: 0 for c in "ACGT-"}
    gap_col_1['-'] = N1 # A column of N1 gaps
    
    gap_col_2 = {c: 0 for c in "ACGT-"}
    gap_col_2['-'] = N2 # A column of N2 gaps
    # -----------------------

    # Initialize DP table (base cases)
    for i in range(1, n+1):
        # Cost of aligning profile 1's column with N2 gaps
        DP[i][0] = DP[i-1][0] + col_score(p1[i-1], gap_col_2, match, mismatch)
        TR[i][0] = "U"
    for j in range(1, m+1):
        # Cost of aligning profile 2's column with N1 gaps
        DP[0][j] = DP[0][j-1] + col_score(gap_col_1, p2[j-1], match, mismatch)
        TR[0][j] = "L"

    for i in range(1, n+1):
        for j in range(1, m+1):
            print(p1)
            d = DP[i-1][j-1] + col_score(p1[i-1], p2[j-1])
            u = DP[i-1][j] + col_score(p1[i-1], gap_col_2) # SOP gap
            l = DP[i][j-1] + col_score(gap_col_1, p2[j-1]) # SOP gap
            DP[i][j], TR[i][j] = min((d, "D"), (u, "U"), (l, "L"))

    # Corrected traceback loop (handles edges)
    actions = []
    i, j = n, m
    while i > 0 or j > 0:
        if i > 0 and j > 0 and TR[i][j] == "D":
            actions.append("D")
            i -= 1
            j -= 1
        elif i > 0 and (j == 0 or TR[i][j] == "U"):
            actions.append("U")
            i -= 1
        else: # j > 0 and (i == 0 or TR[i][j] == "L")
            actions.append("L")
            j -= 1

    return actions[::-1] 

def apply_profile_actions(seqs1, seqs2, actions):
   
    new1 = ["" for _ in seqs1]
    new2 = ["" for _ in seqs2]

    i = j = 0
    L1 = len(seqs1[0])
    L2 = len(seqs2[0])

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

    return new1 + new2


def profile_profile_alignment(seqs1, seqs2):
    """
    Align two profiles and return one merged profile.
    This is the wrapper that calls the DP function.
    """
    p1 = build_profile(seqs1)
    p2 = build_profile(seqs2)
    
    # Get the number of sequences in each profile
    N1 = len(seqs1)
    N2 = len(seqs2)

    actions = profile_profile_dp(p1, p2, N1, N2)
    return apply_profile_actions(seqs1, seqs2, actions)
    
build_tree(seq)
graph = sorted(graph)

num_edge = 0
N = len(seq)
dsu = DSU(N)
cls = {i: [seq[i]] for i in range(N)}
edge_count = 0
for (val, node1, node2) in graph:
    root1 = dsu.find(node1)
    root2 = dsu.find(node2)
    print(cls)
    # print(root1,root2, seq[root1], seq[root2])
    if (root1 != root2):	
        new_node = profile_profile_alignment(cls[root1],cls[root2])
        dsu.union(root1,root2)
        new_root = dsu.find(root1)
        cls[new_root] = new_node
        #print(val)
        edge_count += 1
        if edge_count == N - 1:
            break
    
def get_sop_score(aligned_sequences, match = 0, mismatch =-1, gap_char =-1):
    """
    Calculates the Sum-of-Pairs (SOP) score for an alignment.
    
    - 'gap_char' is the score for a character-gap pair.
    - 'gap-gap' score is assumed to be 0.
    """
    if not aligned_sequences:
        return 0
    
    num_seqs = len(aligned_sequences)
    align_len = len(aligned_sequences[0])
    total_score = 0

    # Loop over each column
    for j in range(align_len):
        col_score = 0
        
        # Loop over every unique pair of sequences (i, k)
        for i in range(num_seqs):
            for k in range(i + 1, num_seqs):
                
                char1 = aligned_sequences[i][j]
                char2 = aligned_sequences[k][j]
                
                # Add the score for this pair
                if char1 == '-' and char2 == '-':
                    pass # gap-gap score is 0
                elif char1 == '-' or char2 == '-':
                    col_score += gap_char
                elif char1 == char2:
                    col_score += match
                else:
                    col_score += mismatch
        
        total_score += col_score
    
    return total_score

print(get_sop_score(cls[0]))
for x in cls[0]:
    print(x)

            
            
            
                        