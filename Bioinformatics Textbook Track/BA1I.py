#!/usr/bin/env/python
f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")
seq = f1.readline().strip()
n = len(seq)
k, d = map(int, f1.readline().strip().split())
k_mer = []
def hamming(s1, s2):
    cnt = 0
    for i in range(len(s1)):
        if (s1[i] != s2[i]):
            cnt += 1
    return cnt
def neighbors(s1, d):
    mismatches = {}
    nu = ["A", "C", "G", "T"]
    mismatches[0] = [s1]
    patterns = {s1:1}
    for i in range(1, d + 1):
        mismatches[i] = []
        for father_string in mismatches[i-1]:
            for k in range(len(s1)):
                for x in nu:
                    if (father_string[k] != x):
                        tmp = list(father_string)
                        tmp[k] = x
                        pattern = "".join(map(str,tmp))
                        mismatches[i].append(pattern)
                        if (pattern not in patterns):
                            patterns[pattern] = 1
    return list(patterns.keys())
for i in range (n - k + 1):
    k_mer.append(seq[i:i+k])
mp = {}
for i in range(n - k + 1):
    neighborhood = neighbors(k_mer[i],d)
    for j in neighborhood:
        if j not in mp:
            mp[j] = 1
        else:
            mp[j] += 1
max1 = max(mp.values())
for k,v in mp.items():
    if (v == max1):
        f2.write(k + " ")


