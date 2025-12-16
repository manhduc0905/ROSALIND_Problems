from collections import deque
input_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\input.INP"
output_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\output.OUT"
f1 = open(input_path, 'r')
f2 = open(output_path,'w')

graph = {}

def bfs(root):
    dist = {}
    dist[root] = 0
    visited = set()
    visited.add(root)
    queue = [root]
    while queue:
        cur = queue.pop(0)
        for neighbor in graph[cur]:
            if neighbor not in visited:
                dist[neighbor] = dist[cur] + 1
                visited.add(neighbor)
                queue.append(neighbor)
    return dist



n,m = map(int,f1.readline().strip().split())
for line in f1:
    line = list(map(int,line.strip().split()))
    for x in line: 
        if x not in graph:
            graph[x] = []
    graph[line[0]].append(line[1])

dist = bfs(1)
for i in range(1,n+1):
    if i in dist:
        f2.write(f"{dist[i]} ")
    else: f2.write("-1 ")