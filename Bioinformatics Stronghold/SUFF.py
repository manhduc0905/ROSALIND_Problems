import sys
input_path = input_path = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
f1 = open(input_path, 'r')
f2 = open("output.OUT",'w')

s = f1.readline().strip()

class Node:
    def __init__(self, start, end_ref):
        self.start = start
        self.end = end_ref
        self.children = {}
        self.suffix_link = None

global_end = [-1]
root = Node(-1, [-1])
root.suffix_link = root

n = len(s)

graph = {}
visit = {}

def splitter(active_node, active_edge, active_length, pos, s):
    next_node = active_node.children[active_edge]
    split_end = [next_node.start + active_length -1]
    split_node = Node(next_node.start, split_end)
    split_node.suffix_link = root
    active_node.children[active_edge] = split_node
    next_node.start += active_length
    char = s[next_node.start]
    split_node.children[char] = next_node
    split_node.children[s[pos]] = Node(pos, global_end)
    return split_node

def print_tree(node, s, indent=0):
    for char in sorted(node.children.keys()):
        child = node.children[char]
        start = child.start
        end = child.end[0]
        f2.write(s[start : end + 1] + "\n")
        print_tree(child, s)

remainder = 0
temp = ""

active_node = root
active_edge = None
active_length = 0

for i in range(n):
    global_end[0] = i
    remainder += 1
    print(active_length, i , active_edge)
    prev_node = None
    while remainder > 0:
        if active_length == 0:
            active_edge = s[i]

        if active_edge not in active_node.children:
            active_node.children[active_edge] = Node(i, global_end)
            if prev_node:
                prev_node.suffix_link = active_node
                prev_node = None
            
            if active_node != root:
                active_node = active_node.suffix_link
                remainder-=1
            else:
                active_length = max(0, active_length - 1)
                remainder -=1
                if remainder > 0:
                    active_edge = s[i - remainder + 1]
        else:
            edge_node = active_node.children[active_edge]
            edge_len = edge_node.end[0] - edge_node.start + 1
            
            if active_length >= edge_len:
                active_node = edge_node
                active_length -= edge_len
                active_edge = s[i - active_length]
                continue 
            
            existing_char = s[edge_node.start + active_length]
            
            if existing_char == s[i]:
                active_length += 1
                if prev_node and active_node != root:
                    prev_node.suffix_link = active_node
                break 
            
            else:
                split_node = splitter(active_node, active_edge, active_length, i, s)
                if prev_node:
                    prev_node.suffix_link = split_node
                prev_node = split_node
                
                if active_node == root:
                    active_length -= 1
                    remainder -= 1
                    if remainder > 0:
                        active_edge = s[i - remainder + 1]
                else:
                    if active_node.suffix_link:
                        active_node = active_node.suffix_link
                    else:
                        active_node = root
                    remainder -= 1
print_tree(root,s)
    
    
        
