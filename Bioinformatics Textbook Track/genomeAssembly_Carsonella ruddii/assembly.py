#!/usr/bin/env/python
import os
import numpy as np
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_in = os.path.join(script_dir, "reads.txt")
file_path_out = os.path.join(script_dir, "genome.txt")
f1 = open(file_path_in, "r")
f2 = open(file_path_out, "w")

class pair_reads:
    def __init__(self, reads, k):
        self.reads = reads
        self.kmer = k
        self.deBru_graph = {}
        self.seq_len = len(reads) + 2*k + d - 1   
        for read1, read2 in self.reads:
            prefix = (read1[:-1], read2[:-1])
            suffix = (read1[1:], read2[1:])
            if (prefix not in self.deBru_graph):
                self.deBru_graph[prefix] = []
            self.deBru_graph[prefix].append(suffix)
        #self.seq = self.Seq_eulerian_path()
        
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

        for node in nodes:
            if (node not in out_deg): continue
            if (out_deg[node] > in_deg[node]):
                start_node = node
                break

        stack = [start_node]
        seq = [""]*self.seq_len
        
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
        prefix_string = path[0][0]
        suffix_string = path[0][1]
        for i in range(1, len(path)):
            prefix_string += path[i][0][-1]
            suffix_string += path[i][1][-1]
        offset = k + d
        return prefix_string + suffix_string[-offset:]
    
k, d = [120, 1000]
reads_set = pair_reads([tuple(pread.split('|')) for pread in f1.read().strip().split('\n') ], k)
f2.write(reads_set.Seq_eulerian_path())








