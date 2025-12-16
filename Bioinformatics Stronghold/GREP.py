from collections import deque
f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")
D = f1.read().split("\n")
n = len(D)
graph = {}
cnt = {}
#print(n)

end = (1 << n) - 1
ans = set()
def dfs(u, cur, seq):
    #print(bin(cur))
    global ans
    if (cur == end):
        #print(seq)
        ans.add(seq)
        return
    for [v,i] in graph[u]:
        if not (cur & (1 << i)):
            next_mask = cur | (1 << i)
            dfs(v, next_mask, seq + u[0])
for i in range(n):
    u = D[i][:-1]
    v = D[i][1:]
    if (u not in graph):
        graph[u] = []
    graph[u].append((v,i))
#print(graph)
dfs(D[0][1:], 1 << 0, D[0][0])
for x in ans:
    f2.write(x + "\n")

