#!/usr/bin/env/python
import os
import numpy as np
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_in = os.path.join(script_dir, "input.INP")
file_path_out = os.path.join(script_dir, "output.OUT")
f1 = open(file_path_in, "r")
f2 = open(file_path_out, "w")

class reads:
    def __init__(self, reads, k):
        self.reads = reads
        self.kmer = k
        self.deBru_graph = {}   
        for read in self.reads:
            prefix = read[:-1]
            suffix = read[1:]
            if (prefix not in self.deBru_graph):
                self.deBru_graph[prefix] = []
            self.deBru_graph[prefix].append(suffix)
        self.seq = self.Seq_eulerian_path()
        
    def Seq_eulerian_path(self):
        nodes = set()
        in_deg = {}
        out_deg = {}

        for u in self.deBru_graph:
            nodes.add(u)
            out_deg[u] = len(self.deBru_graph[u])
            if (u not in in_deg): in_deg[u] = 0
            for v in self.deBru_graph[u]:
                nodes.add(v)
                if (v not in in_deg): in_deg[v] = 0
                in_deg[v] += 1
        start_node = '0'*(self.kmer-1)
        for node in nodes:
            if (node not in out_deg): continue
            if (out_deg[node] > in_deg[node]):
                start_node = node
                break
        
        stack = [start_node]
        dummy_graph = self.deBru_graph.copy()
        path = []
        while stack:
            curr_node = stack[-1]
            if (dummy_graph.get(curr_node)):
                next_node = dummy_graph[curr_node].pop()
                stack.append(next_node)
            else:
                path.append(stack.pop())
        path.reverse()
        sequence = ""
        for idx, node in enumerate(path):
            if (idx == len(path) - 2): sequence += node
            else:
                sequence += node[0]
        sequence = sequence[:2**self.kmer]
        return sequence

k = int(f1.readline().strip())
reads_set = reads([format(i, f'0{k}b') for i in range(2**(k))], k)
print(reads_set.reads)
f2.write(reads_set.seq)








