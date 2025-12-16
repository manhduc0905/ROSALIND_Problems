import sys

n = int(sys.stdin.readline().strip())
edges = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for line in sys.stdin:
	line = line.strip()
	u, v = map(int, line.split())
	edges[u].append(v)
	edges[v].append(u)
	
def dfs(u):
	visited[u] = 1
	for v in edges[u]:
		if (visited[v] == 0):
			dfs(v)
dfs(1)
ans = 0
for i in range(2,n):
	if (visited[i] == 0):
		ans += 1
		dfs(i)
print(ans)
	