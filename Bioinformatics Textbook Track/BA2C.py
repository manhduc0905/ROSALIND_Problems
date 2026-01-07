#!/usr/bin/env/python
f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")
seq = f1.readline().strip()
k = int(f1.readline().strip())
nu = ["A", "C", "G", "T"]
table = {nu[idx]:list(map(float,s.split())) for idx,s in enumerate(f1.read().split('\n')) if s}

def prob(seq):
    ans = 1
    for idx, base in enumerate(seq):
        #print(table[base][idx])
        ans*=table[base][idx]
    return ans

max1 = -float('inf')
ans_seq= ""
for i in range(len(seq) - k + 1):
    max1,ans_seq = max((prob(seq[i:i+k]),seq[i:i+k]), (max1,ans_seq))
f2.write(ans_seq)


