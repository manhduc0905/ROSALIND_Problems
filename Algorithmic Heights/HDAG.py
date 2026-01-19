#!/usr/bin/env python3
import os
import numpy as np
from collections import deque
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_in = os.path.join(script_dir, "input.INP")
file_path_out = os.path.join(script_dir, "output.OUT")
f1 = open(file_path_in, "r")
f2 = open(file_path_out, "w")

k = int(f1.readline().strip())
graphs = [x.split('\n') for x in f1.read().strip().split('\n\n')]

def hamilton_path(mp, nodes, in_deg, n):
    queue = deque()
    ans = []
    for node in nodes:
        if (in_deg[node] == 0):
            queue.append(node)
    while queue:
        if (len(queue) > 1):
            return False
        top = queue.popleft()
        ans.append(top)
        for x in mp[top]:
            in_deg[x] -= 1
            if (in_deg[x] == 0):
                queue.append(x)
    print(ans)
    if len(ans) != n:
        return False
    return ' '.join(map(str, ans))

for graph in graphs:
    mp = {}
    in_deg = {}
    nodes = set()
    for idx,line in enumerate(graph):
        if not line.strip():
            continue
        u, v = map(int, line.split())
        if (idx == 0):
            total_node = u
            edge = v
            continue
        if u not in nodes: 
            mp[u] = []
            in_deg[u] = 0
        if v not in nodes: 
            mp[v] = []
            in_deg[v] = 0
        if v not in mp[u]:
            mp[u].append(v)
            in_deg[v] += 1
        nodes.add(u)
        nodes.add(v)
    ans = hamilton_path(mp, nodes, in_deg, total_node)
    if (ans):
        f2.write(f"1 {ans}\n")
    else:
        f2.write("-1\n")