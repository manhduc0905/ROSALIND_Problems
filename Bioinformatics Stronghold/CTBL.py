import re
input_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
output_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\output.OUT"
f1 = open(input_path, 'r')
f2 = open(output_path,'w')
ions = []
num = 0

graph = {}
curr = 0
stk = []
d = {}
node = []
def build_tree(t):
	curr_node = 0
	node_cnt = 0
	graph[curr_node] = []
	i = 0
	prev = 0
	n = len(t)
	while i < n:
		char = t[i]
		if (char == ';'):
			return
		elif (char == '('):
			node_cnt+=1
			new_node = node_cnt
			
			graph[curr_node].append(new_node)
			graph[new_node] = []
			stk.append(curr_node)
			node.append(new_node)
			curr_node = new_node
		elif (char == ','):
			pass
		elif (char == ')'):
			prev = curr_node
			curr_node = stk.pop()
		else:
			name_start = i
			while (i+1 < n) and (t[i+1] not in "(),;"):
				i+=1
			name = t[name_start:i+1]
			#print(name)
			internal_label = (name_start > 0 and t[name_start-1] == ')')
			if (internal_label):
				d[name] = prev
			else:
				node_cnt +=1
				
				leaf_node = node_cnt
				d[name] = leaf_node
				
				graph[curr_node].append(leaf_node)
				graph[leaf_node] = []
		i+=1

def dfs(visited, par):
	for x in graph[par]:
		if (x not in visited):
			visited[x] = 1
			dfs(visited,x)
	return visited

tree = f1.readline()

build_tree(tree)
print(graph)
d = sorted(d.items())

for i in range(len(node)-1,0,-1):
	#print(graph[node[i]])
	visited = {}
	for child in graph[node[i]]:
		visited[child] = 1
		visited = dfs(visited,child)
	for x in d:
		#print(x[1], end = " ")
		if (x[1] not in visited):
			print("0", end = "")
		else:
			print("1", end = "")
	print()