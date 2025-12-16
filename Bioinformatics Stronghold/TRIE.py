f1 = open('input.INP', 'r')
f2 = open('output.OUT', 'w')


adj = {}
adj[1] = {}
trace = {}
trace[1] = {}
cur = 1

def build_tree(par, dna, index, up):
    global cur
    if (index == up):
        return
    #print(par, dna[index], cur+1)
    nu = dna[index]
    
    if (par not in adj):
        adj[par] = {}
        #trace[par] = {}

    if (nu in adj[par]):
        next_node = adj[par][nu]
        build_tree(next_node, dna, index + 1, up)
    else:
        cur += 1
        next_node = cur
        adj[par][nu] = next_node  
        #trace[cur-1][cur+1] = nu
        build_tree(next_node, dna, index + 1, up)

visited = {}
def dfs(par):
    if (par in visited) or (par not in adj):
        return
    for nu, node in adj[par].items():
        f2.write(f"{par} {node} {nu}\n")
        dfs(node)
    visited[par] = 1
        
    
num = 0
for line in f1:
    line = line.strip()
    #print(line)
    build_tree(1, line, 0, len(line))
dfs(1)
