import sys
import pandas as pd
input_path = input_path = r"C:\Users\admin\OneDrive - Grinnell College\Documents\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
#print(input_path)
f1 = open(input_path,'r')
f2 = open('output.OUT','w')
    
taxa = f1.readline().strip().split()

def print_C(lenx, a1, d1, v, ind):	
    if (lenx == len(a1)):
        v.append(a1[:])
        return
    for i in range(ind, len(d1)):
        # print(a1)
        # print(i, d1[i])
        tx_idx = taxa[d1[i]]
        print_C(lenx, a1 + [tx_idx], d1,v, i+1)
        
    return v
                        
    
final_quartets = set()
for line in f1:
    line = line.strip()
    d = {}
    d[1] = []
    d[0] = []
    n = len(line)
    #print(line)
    for i in range(n):
        if line[i] != "x":
            d[int(line[i])].append(i)
    
    if (len(d[0]) <= 1 or len(d[1]) <= 1):
        continue
    #print(len1,len2)
    set1 = print_C(2,[],d[1],[], 0)
    set2 = print_C(2,[],d[0],[], 0)
    
    for x in set1:
        for y in set2:
            str_x = tuple(sorted(x))
            str_y = tuple(sorted(y))
        
            quartet = tuple(sorted((str_x, str_y)))
            final_quartets.add(quartet)
for q in final_quartets:
    pair1 = q[0]
    pair2 = q[1]
    
    print(f"{{{pair1[0]}, {pair1[1]}}} {{{pair2[0]}, {pair2[1]}}}")