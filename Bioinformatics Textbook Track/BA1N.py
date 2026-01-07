#!/usr/bin/env/python
f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")
seq = f1.readline().strip()
d = int(f1.readline().strip())
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
f2.write("\n".join(map(str,neighbors(seq,d))))