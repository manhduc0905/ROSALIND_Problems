import sys
import os
import io
import pandas as pd
input_path = input_path = r"C:\Users\admin\OneDrive - Grinnell College\Documents\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
#print(input_path)
f1 = open(input_path,'r')
f2 = open('output.OUT','w')
graph = {}
for line in f1:
	line = line.strip()
	k = len(line) - 1
	prefix = line[:-1]
	suffix = line[1:]
	graph[prefix] = suffix
	begin = prefix

curr = begin
ans = ""
while True:
	ans += curr[0]
	curr = graph[curr]
	if (curr == begin):
		break
print(ans)
