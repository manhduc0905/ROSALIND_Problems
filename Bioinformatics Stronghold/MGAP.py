import sys
import os
sys.setrecursionlimit(100000)
input_path = input_path = r"C:\Users\admin\OneDrive - Grinnell College\Documents\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
f1 = open(input_path, 'r')
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
def lcs(seq1,seq2):
	n = len(seq1)
	m = len(seq2)
	
	prev = [0]*(m+1)
	curr = [0]*(m+1)
	for i in range(1,n):
	    for j in range(1,m):
	        if (seq1[i] == seq2[j]):
	        	curr[j] = prev[j-1] + 1
	        else:
	        	curr[j] = prev[j] if prev[j] > curr[j-1] else curr[j-1]
	        	
	    prev, curr = curr, prev
	print(n + m - 2*prev[m-1] - 2)	

lcs(seq1,seq2)
            
            
            
            
            
            
        