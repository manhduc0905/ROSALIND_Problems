import sys
import os
input_path = input_path = r"C:\Users\admin\OneDrive - Grinnell College\Documents\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
#print(input_path)
f1 = open(input_path,'r')
f2 = open('output.OUT','w')
seq = []
temp = ""
s1 = f1.readline().strip()
for line in f1:
    seq.append(line.strip())


n = len(seq)
n_s = len(s1)
#print(s1)

def gen(s1,s2,s3,id,i,j):
	#print(id,i,j)
	
	if (len(s1) == id):
		return (len(s2) == i and len(s3) == j)
		
	ok = False
	
	if (i < len(s2) and s1[id] == s2[i] ):
		ok = (ok or gen(s1,s2,s3,id+1,i+1,j))
	if (j < len(s3) and s1[id] == s3[j] ):
		ok = (ok or gen(s1,s2,s3,id+1,i,j+1))
	
	return ok
	
def check(seq1, seq2):
	n1 = len(seq1)
	m1 = len(seq2)
	#print(seq1,seq2)
	if (n1 + m1 > n_s):
		return 0
	flag = False
	for i in range(n_s - (n1 + m1) + 1):
		s_eg = s1[i:(i+n1+m1)]
		#print(s_eg, seq1, seq2)
		flag = gen(s_eg, seq1, seq2 , 0, 0 , 0)
		if (flag): return flag
	return flag

mat = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
	for j in range(n):
		mat[i][j] = 1 if check(seq[i],seq[j]) else 0
		print(mat[i][j], end = " ")
	print()

		