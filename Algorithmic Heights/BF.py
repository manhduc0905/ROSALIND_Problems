import heapq
input_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\input.INP"
output_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\output.OUT"
f1 = open(input_path, 'r')
f2 = open(output_path,'w')

n,m = (map(int, f1.readline().strip().split()))
graph = []


def bellmanford(start):
    dist = [float('inf') for _ in range(n+1)]
    dist[start] = 0
    print(dist)
    for i in range(1,n):
        for w, u, v in graph:
           # print(w,u,v)
            if (dist[u] != float('inf') and dist[v] > dist[u] + w ):
                if i == n - 1:
                    return [-1]
                dist[v] = dist[u] + w

    for i in range(1,n+1):
        if (dist[i] != float('inf')):
            f2.write(f"{dist[i]} ")
        else:
            f2.write(f"x ")

for i in range(m):
    u,v,k = (map(int, f1.readline().strip().split()))
    graph.append((k,u,v))
    
bellmanford(1)