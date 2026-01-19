#!/usr/bin/env/python
f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")
seq = f1.readline().strip()
k,d = map(int, f1.readline().strip().split())
patterns = []
nu = ["A", "C", "T", "G"]
def gen(k, cur, seq):
    if (cur == k):
        patterns.append(seq)
        return
    for x in nu:
        gen(k, cur + 1, seq + x)
def hamming(seq1, seq2):
    cnt = 0
    for idx, base in enumerate(seq1):
        if (seq2[idx] != base):
            cnt += 1
    return cnt

def revcomp(seq):
    return str(seq).translate(str.maketrans("ACGT", "TGCA"))[::-1]

gen(k, 0, "")
freq_map = {x:0 for x in patterns}
for i in range(len(seq) - k + 1):
    for x in patterns:
        if (hamming(seq[i:i+k], x) <= d):
            freq_map[x] += 1
            freq_map[revcomp(x)] += 1

max_val = max(freq_map.values())
for key,val in freq_map.items():
    if (val == max_val):
        f2.write(key + " ")
