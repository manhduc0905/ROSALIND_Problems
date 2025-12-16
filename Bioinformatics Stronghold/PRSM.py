import sys
import os
input_path = input_path = r"C:\Users\admin\OneDrive - Grinnell College\Documents\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
#print(input_path)
f1 = open(input_path,'r')
f2 = open('output.OUT','w')
seq = []
temp = ""


table = """A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333 """
mass = {}
name = {}
seq = []
R = []
for line in table.splitlines():
    line = line.split()
    name[float(line[1])] = line[0]
    mass[line[0]] = float(line[1])

n = int(f1.readline().strip())

for _ in range(n):
    x = f1.readline().strip()
    sum = 0
    for chr in x:
        sum += mass[chr]
    seq.append((x,round(sum,5)))
for line in f1:
    R.append(float(line.strip()))

def get_Spec(seq, tot):
    n = len(seq)
    lst = []
    sum = 0
    for i in range(n-1):
        sum += mass[seq[i]]
        lst.append(round(sum,5))
        lst.append(round(tot-sum,5))
    lst.append(tot)

    return lst
    
max1 = (-1,"")
for x in seq:
    occur = {}
    #print(x[0])
    lst = get_Spec(x[0],x[1])
    for z in lst:
        for y in R:
            z0 = round(y - z,5)
            #print(z0)
            if z0 not in occur:
                occur[round(z0,5)] = 0
            occur[round(z0,5)] += 1
        if (max(occur.values()) > max1[0]):
            max1= (max(occur.values()),x[0])

print(max1[0])
print(max1[1])