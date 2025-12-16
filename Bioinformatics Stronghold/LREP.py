import sys
input_path = input_path = r"C:\Users\admin\OneDrive - Grinnell College\Documents\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
f1 = open(input_path, 'r')

s = f1.readline().strip()
k = int(f1.readline().strip())

graph = {}
visited = {}
count = {}
best = ""
def dfs(par, w):
	global best
	if par not in graph:
		return 1
	
	total_leaves = 0
	for child in graph[par]:
		total_leaves += dfs(child[0], w + child[1])
	if total_leaves >= k:
		if len(best) < len(w):
			best = w
	return total_leaves
				
for line in f1:
	line = line.strip()
	line = list(line.split())
	
	node1 = int(line[0][4:])	
	node2 = int(line[1][4:])
	pos = int(line[2]) - 1
	length = int(line[3])
	
	weight = s[pos:pos + length]
	
	if (node1 not in graph): graph[node1] = []
	graph[node1].append((node2, weight))
	
dfs(1, "")
print(best)