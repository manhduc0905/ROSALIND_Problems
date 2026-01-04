#!/usr/bin/env/python
f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")
import matplotlib.pyplot as plt
seq = f1.readline().strip()
seq = " " + seq
n = len(seq)
skew = {
    "G":[0 for x in range(n)],
    "C":[0 for x in range(n)],
    "G-C":[0 for x in range(n)]
}
for i in range(1,n):
    C_count = 1 if (seq[i] == "C") else 0
    G_count = 1 if (seq[i] == "G") else 0
    skew["C"][i] = C_count + skew["C"][i-1]
    skew["G"][i] = G_count + skew["G"][i-1]
    skew["G-C"][i] = skew["G"][i] - skew["C"][i]
low = min(skew["G-C"])
for i in range(1,n):
    if (skew["G-C"][i] == low):
        f2.write(f"{i} ")
plt.figure(figsize=(10,8))
pos = [x for x in range(1,n)]
plt.plot(pos,skew["G-C"][1:])
plt.xlabel("Position")
plt.ylabel("Skew")
plt.show()
