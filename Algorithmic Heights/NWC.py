import heapq
input_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\input.INP"
output_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\output.OUT"
f1 = open(input_path, 'r')
f2 = open(output_path,'w')

k = int(f1.readline().strip())

def bellmanford(n,graph, start):
        dist = [0]*(n+1)
        dist[start] = 0
        for i in range(n-1):
            up = False
            for w, u, v in graph:
            # print(w,u,v)
                if (dist[v] > dist[u] + w ):
                    dist[v] = dist[u] + w
                    up = True
            if not up:
                break
        for w, u, v in graph:
                if (dist[v] > dist[u] + w ):
                    return 1
        return -1

for _ in range(k):
   # blank = f1.readline()
    n,m = (map(int, f1.readline().strip().split()))
    #print(n,m)
    graph = []

    for i in range(m):
        u,v,w = (map(int, f1.readline().strip().split()))
        graph.append((w,u,v))
        
    f2.write(f"{bellmanford(n,graph,1)} ")