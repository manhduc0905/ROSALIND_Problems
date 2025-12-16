input_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
output_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\output.OUT"
f1 = open(input_path, 'r')
f2 = open(output_path,'w')

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
                d[prev] = name
            else:
                node_cnt += 1

                leaf_node = node_cnt
                d[leaf_node] = name

                graph[cur_node].append(leaf_node)
                graph[leaf_node] = []
            
        i+=1

build_tree(tree)

cross = [
    [
        [1.0, 0.5, 0.0],   # P(AA | AA × AA), (AA × Aa), (AA × aa)
        [0.5, 0.25, 0.0],  # (Aa × AA), (Aa × Aa), (Aa × aa)
        [0.0, 0.0, 0.0]    # (aa × AA), (aa × Aa), (aa × aa)
    ],
    [
        [0.0, 0.5, 1.0],   # AA × AA, AA × Aa, AA × aa
        [0.5, 0.5, 0.5],   # Aa × AA, Aa × Aa, Aa × aa
        [1.0, 0.5, 0.0]    # aa × AA, aa × Aa, aa × aa
    ],
    [
        [0.0, 0.0, 0.0],
        [0.0, 0.25, 0.5],
        [0.0, 0.5, 1.0]
    ]
]

sign = {"AA": 0, "Aa": 1, "aa": 2   }
def compute(P1, P2):
    new = [0.0]*3
    for cg in range(3):
        child_prob = 0.0
        for i in range(3):
            for j in range(3):
                child_prob += cross[cg][i][j] * P1[i] * P2[j]
        new[cg] = child_prob

    return tuple(new)
        
def dfs(par):
    if (len(graph[par]) == 0):
        geno = d[par]   
        probs = [0.0, 0.0, 0.0]
        probs[sign[geno]] = 1.0
        return tuple(probs)
    
    p1, p2 = graph[par]
    P1 = dfs(p1)
    P2 = dfs(p2)
    
    child = compute(P1, P2)
    #print(P1, P2, par, child)
    return child
        
f2.write(" ".join(map(str, dfs(1))))
