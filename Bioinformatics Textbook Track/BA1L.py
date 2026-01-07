#!/usr/bin/env/python
f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")
seq = list(f1.readline().strip())
mp = {"A":0,
      "C":1,
      "G":2,
      "T":3}
n = len(seq)-1
ans = 0
for idx,base in enumerate(seq):
    ans += 4**(n-idx)*mp[base]
f2.write(f"{ans}")


