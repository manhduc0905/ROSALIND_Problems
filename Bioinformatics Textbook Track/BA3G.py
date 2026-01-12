#!/usr/bin/env/python
import os
import numpy as np
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_in = os.path.join(script_dir, "input.INP")
file_path_out = os.path.join(script_dir, "output.OUT")
f1 = open(file_path_in, "r")
f2 = open(file_path_out, "w")
D = f1.read().strip().split('\n')
graph = {}
in_deg = {}
out_deg = {}
nodes = set()
def eulerian_cycle(graph, start_node):
    print(start_node)
    stack = [start_node]
    path = []
    while stack:
        u = stack[-1]
        if graph.get(u):
            v = graph[u].pop() 
            stack.append(v)
        else:
            path.append(stack.pop())
    path.reverse()
    f2.write("->".join(path))
    return

for line in D:
    u,v = line.strip().split(" -> ")
    v = v.split(',')
    graph[u] = []
    out_deg[u] = len(v)
    nodes.add(u)
    
    for neighbor in v:
        nodes.add(neighbor)
        graph[u].append(neighbor)
        if (neighbor not in in_deg): in_deg[neighbor] = 0
        in_deg[neighbor] += 1
for node in nodes:
    if node not in out_deg: out_deg[node] = 0
    if (out_deg[node] > in_deg[node]):
        start_node = node
eulerian_cycle(graph, start_node)