input_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
output_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\output.OUT"
f1 = open(input_path, 'r')
f2 = open(output_path,'w')
ions = []
num = 0


def build_tree(t, graph, d, split_node):
    stk = []
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
            split_node.append(new_node)
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
                d[prev] = name
            else:
                node_cnt +=1
                
                leaf_node = node_cnt
                d[leaf_node] = name
                
                graph[curr_node].append(leaf_node)
                graph[leaf_node] = []
        i+=1
    

taxa = f1.readline().strip().split()
n = len(taxa)
tree1 = f1.readline().strip()
tree2 = f1.readline().strip()
graph1 = {}
graph2 = {}
d1 = {}
d2 = {}
split_node1 = []
split_node2 = []

build_tree(tree1, graph1, d1, split_node1)
build_tree(tree2, graph2, d2, split_node2)
split1 = []
split2 = []
def dfs(graph, d, par, split):
    #print(par)
    if (len(graph[par]) == 0):
        return [d[par]]
    taxon_par = []
    for child in graph[par]:
        taxon = dfs(graph, d, child, split)
        if (len(taxon) != 1):
            taxon1 = []
            for x in taxon:
                taxon1.append(x)
            taxon1.sort()
            split.append(tuple(taxon1))
        taxon_par += taxon
        #print(taxon, taxon_par)
    return taxon_par
    
dfs(graph1, d1, split_node1[0], split1)
dfs(graph2, d2, split_node2[0], split2)
cnt = 0
print(split1)
print(split2)
for x in split1:
    for y in split2:
        if (x == y): cnt +=1
print(2*(n-3) - 2*cnt)

