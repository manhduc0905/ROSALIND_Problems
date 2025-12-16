import sys
input_path = input_path = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
f1 = open(input_path, 'r')
f2 = open("output.OUT",'w')

seq = []
s = ""
raw_matrix = """
   A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y
A  2 -2  0  0 -3  1 -1 -1 -1 -2 -1  0  1  0 -2  1  1  0 -6 -3
C -2 12 -5 -5 -4 -3 -3 -2 -5 -6 -5 -4 -3 -5 -4  0 -2 -2 -8  0
D  0 -5  4  3 -6  1  1 -2  0 -4 -3  2 -1  2 -1  0  0 -2 -7 -4
E  0 -5  3  4 -5  0  1 -2  0 -3 -2  1 -1  2 -1  0  0 -2 -7 -4
F -3 -4 -6 -5  9 -5 -2  1 -5  2  0 -3 -5 -5 -4 -3 -3 -1  0  7
G  1 -3  1  0 -5  5 -2 -3 -2 -4 -3  0  0 -1 -3  1  0 -1 -7 -5
H -1 -3  1  1 -2 -2  6 -2  0 -2 -2  2  0  3  2 -1 -1 -2 -3  0
I -1 -2 -2 -2  1 -3 -2  5 -2  2  2 -2 -2 -2 -2 -1  0  4 -5 -1
K -1 -5  0  0 -5 -2  0 -2  5 -3  0  1 -1  1  3  0  0 -2 -3 -4
L -2 -6 -4 -3  2 -4 -2  2 -3  6  4 -3 -3 -2 -3 -3 -2  2 -2 -1
M -1 -5 -3 -2  0 -3 -2  2  0  4  6 -2 -2 -1  0 -2 -1  2 -4 -2
N  0 -4  2  1 -3  0  2 -2  1 -3 -2  2  0  1  0  1  0 -2 -4 -2
P  1 -3 -1 -1 -5  0  0 -2 -1 -3 -2  0  6  0  0  1  0 -1 -6 -5
Q  0 -5  2  2 -5 -1  3 -2  1 -2 -1  1  0  4  1 -1 -1 -2 -5 -4
R -2 -4 -1 -1 -4 -3  2 -2  3 -3  0  0  0  1  6  0 -1 -2  2 -4
S  1  0  0  0 -3  1 -1 -1  0 -3 -2  1  1 -1  0  2  1 -1 -2 -3
T  1 -2  0  0 -3  0 -1  0  0 -2 -1  0  0 -1 -1  1  3  0 -5 -3
V  0 -2 -2 -2 -1 -1 -2  4 -2  2  2 -2 -1 -2 -2 -1  0  4 -6 -2
W -6 -8 -7 -7  0 -7 -3 -5 -3 -2 -4 -4 -6 -5  2 -2 -5 -6 17  0
Y -3  0 -4 -4  7 -5  0 -1 -4 -1 -2 -2 -5 -4 -4 -3 -3 -2  0 10
"""
def parse_matrix(raw):
    rows = [r.strip() for r in raw.strip().split("\n")]
    header = rows[0].split()
    matrix = {}
    for row in rows[1:]:
        parts = row.split()
        aa = parts[0]
        scores = list(map(int, parts[1:]))
        matrix[aa] = dict(zip(header, scores))
    return matrix

PAM250 = parse_matrix(raw_matrix)
gap_pen = 5

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


def aligning(seq1, seq2):
    seq1 = " " + seq1
    seq2 = " " + seq2
    n = len(seq1)
    m = len(seq2)
    dp = [[0 for _ in range(m)] for _ in range(n)]
    Trace = [["" for _ in range(m)] for _ in range(n)]
    for i in range(1,n):
        Trace[i][0] = "."
    for j in range(1,m):
        Trace[0][j] = "."
    Trace[0][0] = "X"
    maxer = (-1,0,0)
    for i in range(1,n):
        for j in range(1,m):
            score_i_j = PAM250[seq1[i]][seq2[j]]
            dp[i][j], Trace[i][j] = max((0, "."),   (dp[i-1][j-1] + score_i_j, "D"),(dp[i][j-1] - gap_pen, "L"), (dp[i-1][j] - gap_pen, "U"))
            maxer = max(maxer, (dp[i][j],i,j))
    #printM(dp,seq1,seq2)
    i = maxer[1]
    j = maxer[2]
    aligned_seq1 = ""
    aligned_seq2 = ""
    while (i!= 0 and j != 0 and dp[i][j] != 0):
        if (Trace[i][j] == 'L'):
            aligned_seq2 = seq2[j] + aligned_seq2
            #aligned_seq1 = "-" + aligned_seq1
            j-=1
        elif (Trace[i][j] == 'U'):
            #aligned_seq2 = "-" + aligned_seq2
            aligned_seq1 = seq1[i] + aligned_seq1
            i-=1
        else:
            aligned_seq1 = seq1[i] + aligned_seq1
            aligned_seq2 = seq2[j] + aligned_seq2
            i-=1
            j-=1
    x = maxer[1]
    y = maxer[2]
    f2.write(f"{dp[x][y]}" + "\n")
    f2.write(aligned_seq1 + "\n")
    f2.write(aligned_seq2)
    
for line in f1:
    line = line.strip()
    if (line.startswith('>')):
        if (s != ""):
            seq.append(s)
            s = ""
    else:
        s += line
seq.append(s)
aligning(seq[0], seq[1])