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
def eulerian_cycle(graph):
    start_node = '0' if '0' in graph else next(iter(graph))
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
    for neighbor in v:
        graph[u].append(neighbor)

eulerian_cycle(graph)