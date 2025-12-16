import sys
import os
import io
import pandas as pd
input_path = input_path = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
f1 = open(input_path, 'r')
f2 = open("output.OUT",'w')
seq = []
temp = ""
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
Y -2 -2 -3 -2  3 -3  2 -1 -2 -1 -1 -2 -3 -1 -2 -2 -2 -1  2  7 """
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

sub_matrix = parse_matrix(raw_matrix)
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

seq1 = " " + seq[0]
seq2 = " " + seq[1]   

n = len(seq1)
m = len(seq2)

L = [[0 for _ in range(m)] for _ in range(n)]
Trace = [["" for _ in range(m)] for _ in range(n)]
#printM(L,seq1,seq2)
#Needleman-Wunsch
d = 5
for i in range(1,n):
	L[i][0] = L[i-1][0] -d
	Trace[i][0] = "U"
for j in range(1,m):
	L[0][j] = L[0][j-1] -d
	Trace[0][j] = "L"

Trace[0][0] = "X"


for i in range(1,n):
	for j in range(1,m):
		score_i_j = sub_matrix[seq1[i]][seq2[j]]
		min_align = max((L[i-1][j-1] + score_i_j, "D"), (L[i-1][j] - d, "U"), (L[i][j-1] -d, "L"))
		L[i][j],Trace[i][j] = min_align
		
			
print(abs(L[n-1][m-1]))	
printM(L,seq1,seq2)		
i1 = n-1
j1 = m-1
aligned_seq1 = ""
aligned_seq2 = ""
while (i != 0) and (j!=0):
	if (Trace[i][j] == 'L'):
		aligned_seq1 = "-" + aligned_seq1
		aligned_seq2 = seq2[j] + aligned_seq2
		j-=1
	elif (Trace[i][j] == 'U'):
		aligned_seq1 = seq1[i] + aligned_seq1
		aligned_seq2 = "-" + aligned_seq2
		i-=1
	else:
		aligned_seq1 = seq1[i] + aligned_seq1
		aligned_seq2 = seq2[j] + aligned_seq2
		i-=1
		j-=1

print(aligned_seq1)
print(aligned_seq2)
# 			
# 			
			
			
			
			
			
			
			
			