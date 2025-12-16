import heapq
input_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\input.INP"
output_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\output.OUT"
f1 = open(input_path, 'r')
f2 = open(output_path,'w')

n,m = (map(int, f1.readline().strip().split()))
graph = {_:[] for _ in range(1,n+1)}


def dijkstra(start):
    dist = [float('inf') for _ in range(n+1)]
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        cur_dist, cur_node = heapq.heappop(pq)
        #print(cur_dist, cur_node)
        if (cur_dist> dist[cur_node]):
            continue
        for w, neighbor in graph[cur_node]:
            #print(w, neighbor, dist[neighbor], dist)
            if (dist[neighbor] > dist[cur_node] + w):
                dist[neighbor] = dist[cur_node] + w
                heapq.heappush(pq, (dist[neighbor], neighbor))
    for i in range(1,n+1):
        if (dist[i] != float('inf')):
            f2.write(f"{dist[i]} ")
        else:
            f2.write(f"{-1} ")

for i in range(m):
    u,v,k = (map(int, f1.readline().strip().split()))
    graph[u].append((k,v))
    
dijkstra(1)