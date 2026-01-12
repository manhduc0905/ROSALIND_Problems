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
deg_out = {}
deg_in = {}
nodes = set()
def get_string(path):
    start = path[0]
    for x in path[1:]:
        start += x[-1]
    return start 

for line in D:
    u,v = line.strip().split(" -> ")
    v = v.split(',')
    nodes.add(u)
    graph[u] = []
    if (u not in deg_in): deg_in[u] = 0
    deg_out[u] = len(v)
    for neighbor in v:
        nodes.add(neighbor)
        graph[u].append(neighbor)
        if (neighbor not in deg_out): deg_out[neighbor] = 0
        if (neighbor not in deg_in): deg_in[neighbor] = 0
        deg_in[neighbor] += 1
        
paths = []
contigs = []
vis = set()
for node in nodes:
    if (deg_in[node] == 1 and deg_out[node] == 1): continue
    #if (deg_in[node] == 1 and deg_out[node] == 1 and node in vis): continue
    if (deg_out[node] >= 1):
        vis.add(node)
        for v in graph[node]:
            next_node = v
            curr_path = [node, v]
            while (deg_in[next_node] == 1 and deg_out[next_node] == 1):
                vis.add(next_node)
                next_node = graph[next_node][0]
                curr_path.append(next_node)
                if (next_node == node):
                    break
            paths.append(curr_path)

for node in nodes:
    if (node in vis): continue
    if (deg_out[node] >= 1):
        vis.add(node)
        for v in graph[node]:
            next_node = v
            curr_path = [node, v]
            while (deg_in[next_node] == 1 and deg_out[next_node] == 1):
                vis.add(next_node)
                next_node = graph[next_node][0]
                curr_path.append(next_node)
                if (next_node == node):
                    break
            paths.append(curr_path)
    
for path in paths:
    print(path)
    contigs.append(' -> '.join(map(str,path)))

f2.write('\n'.join(map(str,contigs)))








