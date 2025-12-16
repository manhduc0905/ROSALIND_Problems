input_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\input.INP"
output_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\output.OUT"
f1 = open(input_path, 'r')
f2 = open(output_path,'w')
visited = set()
def dfs(par):
    global visited
    visited.add(par)
    for child in graph[par]:
        if child not in visited:
            dfs(child)

n,m = map(int,f1.readline().strip().split())
graph = {}
for line in f1:
    line = list(map(int,line.strip().split()))
    for x in line: 
        if x not in graph:
            graph[x] = []
    graph[line[0]].append(line[1])
    graph[line[1]].append(line[0])

cnt = 0
for i in range(1, n+1):
    if i not in graph:
        cnt+= 1
    elif i not in visited:
        cnt += 1
        dfs(i)
f2.write(f"{cnt}")

