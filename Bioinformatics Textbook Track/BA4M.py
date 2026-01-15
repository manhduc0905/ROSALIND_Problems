#!/usr/bin/env/python
import os
from collections import Counter
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_in = os.path.join(script_dir, "input.INP")
file_path_out = os.path.join(script_dir, "output.OUT")
f1 = open(file_path_in, "r")
f2 = open(file_path_out, "w")

a = list(map(int,f1.readline().strip().split()))
mp = Counter(a)
a.sort()
b = list(x for x in a if x > 0)
b.pop()
path = [0, a[-1]]

def check(path, b, x):
    a = []
    for p in path:
            a.append(abs(p - x))
    kk = Counter(a)
    b = Counter(b)
    for key,val in kk.items():
        if (kk[key] > b[key]):
            return False
    return a

def choose(path, b):
    if (len(b) == 0):
        return sorted(path)
    y = b[-1]
    flag = check(path,b,y)
    if (flag):
        path.append(y)
        for x in flag:
            b.remove(x)
        res = choose(path, b)
        if (res):
            return res
        for x in flag:
            b.append(x)
        path.pop()
        b.sort()
    y = max(path) - b[-1]
    flag = check(path,b,y)
    if (flag):
        path.append(y)
        for x in flag:
            b.remove(x)
        res = choose(path, b)
        if (res):
            return res
        for x in flag:
            b.append(x)
        path.pop()
        b.sort()
    return None

f2.write(' '.join(map(str,choose(path, b))))



