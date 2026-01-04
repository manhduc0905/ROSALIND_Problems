import math
f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")

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
    
D = f1.read().split('\n')
taxa = D[0].split()
n = len(taxa)

tree1 = D[1]
tree2 = D[2]
graph1 = {}
graph2 = {}
d1 = {}
d2 = {}
split_node1 = []
split_node2 = []

build_tree(tree1, graph1, d1, split_node1)
build_tree(tree2, graph2, d2, split_node2)
rd = {name:idx for idx, name in enumerate(taxa)}
FULL_MASK = (1 << n)-1
def dfs(par, graph, d, cur, split):
    if (len(graph[par]) == 0):
        return (1 << rd[d[par]])

    mask = 0
    for child in graph[par]:
        mask |= dfs(child, graph, d, cur, split)
    normalized = 0
    if par != 0 and mask != 0 and mask != FULL_MASK:
        normalized = min(mask, mask ^ FULL_MASK)
        split.add(normalized)
    return mask
split1 = set()
split2 = set()
dfs(1, graph1, d1, 0, split1)
dfs(1, graph2, d2, 0, split2)
sum = 0
common_splits = split1.intersection(split2)
for x in common_splits:
            g1 = bin(x).count("1")
            g2 = n - g1
            sum += math.comb(g1, 2)*math.comb(g2, 2)

f2.write(f"{(2*math.comb(n,4)-2*sum)}")
            

        