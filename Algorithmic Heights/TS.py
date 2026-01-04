f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")
n,m = map(int, f1.readline().strip().split())
graph = {_:[] for _ in range(1, n+1)}

def topo(graph):
    in_deg = {_:0 for _ in range(1,n+1)}
    for i in range(1,n+1):
        if (i in graph):
            for next in graph[i]:
                in_deg[next] += 1
    queue = []
    for i in range(1,n+1):
        if in_deg[i] == 0:
            queue.append(i)
    res = []
    while queue:
        top = queue.pop(0)
        res.append(top)
        for next in graph[top]:
            in_deg[next] -=1
            if (in_deg[next] == 0):
                queue.append(next)
    return res


for i in range(m):
    u,v = map(int, f1.readline().strip().split())
    graph[u].append(v)
ans = topo(graph)
f2.write(" ".join(map(str, ans)))
