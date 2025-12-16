import sys
import os
input_path = input_path = r"C:\Users\admin\OneDrive - Grinnell College\Documents\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
f1 = open(input_path, 'r')
f2 = open('output.OUT','w')
seq = []
temp = ""
mod = 134217727
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
d = 1
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
        min_align = max((L[i-1][j-1] + score_i_j, "D"), (L[i-1][j] - d, "U"), (L[i][j-1] -d, "L"))
        L[i][j],Trace[i][j] = min_align
        
            
#print(abs(L[n-1][m-1]))	
#printM(L,seq1,seq2)		
i1 = n-1
j1 = m-1
aligned_seq1 = ""
aligned_seq2 = ""

ways = [[0 for _ in range(m)] for _ in range(n)]
def count_all_ways(L, s1, s2):
    n = len(s1)
    m = len(s2)
    ways = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    ways[0][0] = 1
    for i in range(1,n):
        ways[i][0] = 1
    for j in range(1,m):
        ways[0][j] = 1
    for i in range(1,n):
        for j in range(1,m):
        
            if i == 0 and j == 0:
                continue 
            cost = 0 if s1[i] == s2[j] else -d
            if i > 0 and L[i][j] == L[i-1][j] -1:
                ways[i][j] = (ways[i][j] + ways[i-1][j])%mod
                
            if j > 0 and L[i][j] == L[i][j-1] - 1 :
                ways[i][j] = (ways[i][j] + ways[i][j-1])%mod
                
            if i > 0 and j > 0 and L[i][j] == L[i-1][j-1] + cost:
                ways[i][j] = (ways[i][j] + ways[i-1][j-1])%mod
            
    #printM(ways,seq1,seq2)
                
    return ways[n-1][m-1]
        
#print(aligned_seq1)
#print(aligned_seq2)
print(count_all_ways(L, seq1,seq2))
            
            
            
            
            
            
            
            
            
            