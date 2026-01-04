f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")
import heapq
D = f1.read().split("\n")
k = int(D[0])
def dijkstra(start, graph):
    pq = []
    dist = {}
    dist[start] = 0
    heapq.heappush(pq, (0, start))
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        if (u in graph):
            #print(graph[u])
            for w, v in graph[u]:
                if (v not in dist or dist[u] + w < dist[v]):
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
    return dist

i = 1
while i < len(D)-1:
    graph = {}
    #print(D[i])
    n,m = map(int,D[i].split())
    for j in range(i+ 1,i + m + 1):
        #print(j, D[j].split())
        u,v,w = map(int, D[j].split())
        if (u not in graph):
            graph[u] = []
        graph[u].append((w,v))
    u, v, weight = map(int, D[i+1].split())
    dist = dijkstra(v, graph)
    if (u in dist):
        ans = weight + dist[u]
        f2.write(f"{ans} ")
    else:
        f2.write("-1 ")
    i = j + 1