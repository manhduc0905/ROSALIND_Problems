from collections import deque

input_path = input_path = r"C:\Users\admin\OneDrive - Grinnell College\Documents\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
#print(input_path)
f1 = open(input_path,'r')
f2 = open('output.OUT','w')

def revcomp(s):
    return s.translate(str.maketrans('ACTG','TGAC'))[::-1]

kmer = set()
for line in f1:
	line = line.strip()
	revline = revcomp(line)
	k = len(line) 
	#print(hd,mid,tl)
	kmer.add(line)
	kmer.add(revline)
	
	
ans = set()
for strand in kmer:
	node1 = strand[0:k-1]
	node2 = strand[1:]
	ans.add((node1,node2))
ans = sorted(ans)
for x in ans:
	node1 = x[0]
	node2 = x[1]
	print(f"({node1}, {node2})")