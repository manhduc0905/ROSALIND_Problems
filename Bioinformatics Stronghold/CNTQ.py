import math
input_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
output_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\output.OUT"
f1 = open(input_path, 'r')
f2 = open(output_path,'w')

mod = 1000000
n = int(f1.readline().strip())
tree = f1.readline().strip()
graph = {}
node = []
d = {}
def build_tree(t):
    cur_node = 0
    node_cnt = 0
    graph[cur_node] = []
    n = len(t)
    i = 0
    stk = []
    while i < n:
        char = t[i]
        if (char == ";"):
            return
        elif (char == ","):
            pass
        elif (char == ")"):
            prev = cur_node
            cur_node = stk.pop()
        elif (char == "("):
            node_cnt+=1
            new_node = node_cnt

            graph[cur_node].append(new_node)
            graph[new_node] = []
            stk.append(cur_node)
            node.append(new_node)
            cur_node = new_node
        else:
            name_start = i
            while (i+1 < n) and (t[i+1] not in "(),;"):
                i+=1
            name = t[name_start: i+1]

            internal_label = ((name_start > 0) and (t[name_start - 1] == ")"))
            if (internal_label):
                d[name] = prev
            else:
                node_cnt += 1

                leaf_node = node_cnt
                d[name] = leaf_node

                graph[cur_node].append(leaf_node)
                graph[leaf_node] = []
            
        i+=1
sum = 0 
# def dfs(par, subsum):
#     global sum
#     cnt = 0
#     if (len(graph[par]) == 0):
#         return 1
#     for child in graph[par]:
#         subnode = dfs(child)
#         cnt += subnode
#     if cnt > 1 and n - cnt > 1:
#         sum = (sum + (math.comb(n - cnt, 2)%mod)*(math.comb(cnt, 2)%mod) - subsum +  )%mod   
#     return cnt  

# build_tree(tree)
# dfs(1)

f2.write(f"{math.comb(n, 4)%mod}")

