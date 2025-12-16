import sys
import os
from collections import deque

input_path = input_path = r"C:\Users\admin\OneDrive - Grinnell College\Documents\College\Coding\Bioinformatics Learning\input.INP"
#print(input_path)
f1 = open(input_path,'r')
f2 = open('output.OUT','w')
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

seq1 = " " + seq[0]
seq2 = " " + seq[1]   

n = len(seq1)
m = len(seq2)
dp = [[0 for _ in range(m)] for _ in range(n)]
for i in range(1,n):
	dp[i][0] = i
for j in range(1,m):
	dp[0][j] = j

for i in range(1,n):
	for j in range(1,m):
		#print(i,j)
		if (seq1[i] == seq2[j]):
			dp[i][j] =  dp[i-1][j-1]
		else:
			dp[i][j] = 1+ min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
print(dp[n-1][m-1])
#print(dp[1][1])
