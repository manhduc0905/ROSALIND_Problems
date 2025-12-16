f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")
from collections import OrderedDict
seq1 = f1.readline().strip()
k = int(f1.readline().strip())

n = len(seq1)
k_mer = set()
cnt = {}
ans = []
max_freq = -1
for i in range(n):
    read = seq1[i: i + k]
    if (read not in k_mer):
        k_mer.add(read)
        cnt[read] = 1
        
    else:
        cnt[read] += 1
    if (cnt[read] > max_freq):
        max_freq = cnt[read]
        ans = [read]
    elif (cnt[read] == max_freq):
        ans.append(read)
f2.write(' '.join(map(str, ans)))
