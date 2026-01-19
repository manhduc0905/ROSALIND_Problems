#!/usr/bin/env/python
import os
import numpy as np
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_in = os.path.join(script_dir, "input.INP")
file_path_out = os.path.join(script_dir, "output.OUT")
f1 = open(file_path_in, "r")
f2 = open(file_path_out, "w")
start_node = int(f1.readline().strip())
end_node = int(f1.readline().strip())
edges = f1.read().strip().split('\n')
in_deg = {}
weight = {}
rev_graph = {}
graph = {}

def topological_sorting(nodes):
    queue = []
    topo = []
    for node in nodes:
        if (in_deg[node] == 0):
            queue.append(node)
    while queue:
        top = queue.pop(0)
        topo.append(top)
        for v in graph[top]:
            in_deg[v] -=1
            if (in_deg[v] == 0):
                queue.append(v)
    return topo

for edge in edges: 
    uv, w = edge.split(':')
    u,v = map(int,uv.split('->'))
    if u not in in_deg: 
        in_deg[u] = 0 
        rev_graph[u] = []
        graph[u] = []
    if v not in in_deg: 
        in_deg[v] = 0
        rev_graph[v] = []
        graph[v] = []
    in_deg[v] += 1
    weight[(u,v)] = int(w)
    rev_graph[v].append(u)
    graph[u].append(v)
nodes = list(in_deg.keys())
topo = topological_sorting(nodes)
dist = {node: -float('inf') for node in nodes}
trace = {}
dist[start_node] = 0
trace[start_node] = -1
for node in topo:
    if node == start_node:
        continue
    best_val = -float('inf')
    best_prev = -1
    for prev_node in rev_graph[node]:
        best_val, best_prev = max((best_val, best_prev), (dist[prev_node] + weight[(prev_node,node)], prev_node))
    dist[node] = best_val
    trace[node] = best_prev
f2.write(f"{dist[end_node]}\n")
res = []
node = end_node
while 1:
    print(node)
    res.append(node)
    if (trace[node] == -1):
        break
    node = trace[node]
res = res[::-1]
f2.write('->'.join(map(str, res)))
