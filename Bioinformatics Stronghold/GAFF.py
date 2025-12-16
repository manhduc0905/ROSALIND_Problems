import sys
input_path = input_path = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
f1 = open(input_path, 'r')
f2 = open("output.OUT",'w')

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

def printM(matrix, seq1, seq2, cond):
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
			print(matrix[i][j][cond], end = " ")
		print()
            
BLOSUM62 = parse_matrix(raw_matrix)
g_ext = 1
g_open = 11
def alignment(seq1,seq2):
    seq1 = " " + seq1
    seq2 = " " + seq2

    n = len(seq1)
    m = len(seq2)

    dp = [[[0 for _ in range(3)] for _ in range(m)] for _ in range(n)]
    trace = [[[None for _ in range(3)] for _ in range(m)] for _ in range(n)]

    for i in range(1,n):
        dp[i][0][2] = -float('inf')
        if (i == 1):
            dp[i][0][1] -= g_open
        else:
            dp[i][0][1] = dp[i-1][0][1] - g_ext
        dp[i][0][0] = -float('inf')
        trace[i][0][1] = (i-1,0, 1)
    for j in range(1,m):
        if (j == 1):
            dp[0][j][2] -= g_open
        else:
            dp[0][j][2] = dp[0][j-1][2] - g_ext
        dp[0][j][1] = -float('inf')
        dp[0][j][0] = -float('inf')
        trace[0][j][2] = (0, j-1, 2)
    dp[0][0][0] = 0
    dp[0][0][1] = 0
    for i in range(1,n):
        for j in range(1,m):
            score_i_j = BLOSUM62[seq1[i]][seq2[j]]
            dp[i][j][0],trace[i][j][0] = max((dp[i-1][j-1][0] + score_i_j, (i-1,j-1,0)), 
                                             (dp[i-1][j-1][1] + score_i_j, (i-1,j-1,1)),
                                             (dp[i-1][j-1][2] + score_i_j, (i-1,j-1,2)))
            dp[i][j][1],trace[i][j][1] = max((dp[i-1][j][0] - g_open, (i-1,j,0)),
                                             (dp[i-1][j][1] - g_ext,  (i-1,j,1)), 
                                             (dp[i-1][j][2] - g_open, (i-1,j,2)))
            dp[i][j][2],trace[i][j][2] = max((dp[i][j-1][0] - g_open, (i,j-1,0)),
                                             (dp[i][j-1][1] - g_open, (i,j-1,1)), 
                                             (dp[i][j-1][2] - g_ext,  (i,j-1,2)))
    #printM(dp,seq1,seq2,0)

    final_score, curr = max((dp[n-1][m-1][0], (n-1,m-1,0)), (dp[n-1][m-1][1], (n-1,m-1,1)), (dp[n-1][m-1][2], (n-1,m-1,2)))

    print(final_score)
    #f2.write(f"{final_score}")
    align1 = ""
    align2 = ""
    
    while curr is not None:
        i, j, state = curr
        if i == 0 and j == 0:
            break
            
        prev_i, prev_j, prev_state = trace[i][j][state]
        if prev_i == i - 1 and prev_j == j - 1:
            align1 = seq1[i] + align1
            align2 = seq2[j] + align2
        elif prev_i == i - 1 and prev_j == j:
            align1 = seq1[i] + align1
            align2 = "-" + align2
        elif prev_i == i and prev_j == j - 1:
            align1 = "-" + align1
            align2 = seq2[j] + align2
        curr = (prev_i, prev_j, prev_state)

    print(align1)
    print(align2)
    f2.write(f"{final_score}\n{align1}\n{align2}")
s = ""
seq = []
for line in f1:
    line = line.strip()
    if (line.startswith('>')):
        if (s != ""):
            seq.append(s)
            s = ""
    else:
        s += line
seq.append(s)
alignment(seq[0], seq[1])
