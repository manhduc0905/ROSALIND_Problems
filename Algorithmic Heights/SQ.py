input_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\input.INP"
output_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\output.OUT"
f1 = open(input_path, 'r')
f2 = open(output_path,'w')

k = int(f1.readline().strip())
emp = f1.readline()
graph = {}
nodes = []
vis = set()
n = 0
m = 0
cnt = 0
def count():
    for x in nodes:
            for y in nodes:
                if (x != y):
                    common_neighbors = len(graph[x].intersection(graph[y]))
                    if common_neighbors == 2:
                    #  print(nodes[i], nodes[j],graph[nodes[i]], graph[nodes[j]])
                        return 1   
    return -1

for line in f1:
    if (line == "\n"):
        f2.write(f"{count()} ")
        graph = {}
        nodes = []
        vis = set()
        cnt = 0
    else:
        line = line.strip()
        if (cnt == 0):
            n, m = map(int,line.split())
        else:
            u,v = map(int,line.split())
            if (u not in graph):
                graph[u] = set()
                nodes.append(u)
            if (v not in graph):
                graph[v] = set() 
                nodes.append(v)
            graph[u].add(v)
            graph[v].add(u)
        cnt+=1
        
f2.write(f"{count()} ")


