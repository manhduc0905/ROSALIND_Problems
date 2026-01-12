#!/usr/bin/env/python
import os
import numpy as np
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_in = os.path.join(script_dir, "input.INP")
file_path_out = os.path.join(script_dir, "output.OUT")
f1 = open(file_path_in, "r")
f2 = open(file_path_out, "w")

def get_string(path):
    start = path[0]
    for x in path[1:]:
        start += x[-1]
    return start 

class reads:
    def __init__(self, reads):
        self.reads = reads
        self.kmer = len(reads[0])
        self.deBru_graph = {}   
        for read in self.reads:
            prefix = read[:-1]
            suffix = read[1:]
            if (prefix not in self.deBru_graph):
                self.deBru_graph[prefix] = []
            self.deBru_graph[prefix].append(suffix)
        print(self.deBru_graph)
        #self.seq = self.Seq_eulerian_path()
    def contigs(self):
        nodes = set()
        in_deg = {}
        out_deg = {}
        paths = []
        for u in self.deBru_graph:
            nodes.add(u)
            out_deg[u] = len(self.deBru_graph[u])
            if (u not in in_deg): in_deg[u] = 0
            for v in self.deBru_graph[u]:
                nodes.add(v)
                if (v not in in_deg): in_deg[v] = 0
                if (v not in out_deg): out_deg[v] = 0
                in_deg[v] += 1

        for u in nodes:
            if (in_deg[u] !=1 or out_deg[u] != 1):
                if out_deg[u] >= 1:
                    for v in self.deBru_graph[u]:
                        curr_path = [u, v]
                        next_node = v
                        while (in_deg[next_node] == 1 and out_deg[next_node] == 1):
                            next_node = self.deBru_graph[next_node][0]
                            curr_path.append(next_node)
                        paths.append(curr_path)
        contigs_set = []
        for path in paths:
            contigs_set.append(get_string(path))
        return contigs_set     

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
            if (idx == len(path) - 1): sequence += node
            else:
                sequence += node[0]
        return sequence

reads_set = reads(f1.read().strip().split('\n'))
f2.write(' '.join(map(str,reads_set.contigs())))








