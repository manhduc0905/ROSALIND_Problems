f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")

def build_tree(t, graph, d, rd):
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
                rd[name] = prev
            else:
                node_cnt +=1
                
                leaf_node = node_cnt
                d[leaf_node] = name
                rd[name] = leaf_node
                graph[curr_node].append(leaf_node)
                graph[leaf_node] = []
        i+=1

def revcomp(s):
    return s.translate(s.maketrans("ATCG","TAGC"))[::-1]

def len_align(s1,s2):   
    n = len(s1)
    diff = 0
    new_set = []
    for i in range(n):
        a = s1[i]
        b = s2[i] 
        inter = a&b
        if inter:
            new_set.append(inter)
        else:
            diff += 1
            new_set.append(a | b)

    return diff, new_set

calculated_sets = {}
def dfs(par):
    if (not graph[par]):    
            leaf_sets = [{c} for c in dna_node[par]]
            calculated_sets[par] = leaf_sets
            return 0, [leaf_sets]
    cur1, seq1 = dfs(graph[par][0])
    cur2, seq2 = dfs(graph[par][1])
    ans = float('inf')
    seq_new = []
    for s1 in seq1:
        for s2 in seq2:
            score, s1_new = len_align(s1,s2)
            if (score < ans):
                ans = score
                seq_new = [s1_new]
            elif (score == ans):
                seq_new.append(s1_new)
    #print(ans, seq_new)
    calculated_sets[par] = seq_new[0]
    return cur1 + cur2 + ans, seq_new

def reconstruct(node, parent_seq=None):
    my_sets = calculated_sets[node]
    my_seq_chars = []
    
    for i in range(len(my_sets)):
        child = my_sets[i]
        if parent_seq and (parent_seq[i] in child):
            my_seq_chars.append(parent_seq[i])
        else:
            my_seq_chars.append(list(child)[0])
            
    my_seq = "".join(my_seq_chars)
    if graph[node]:
        node_name = d.get(node, f"Node_{node}")
        f2.write(f">{node_name}\n{my_seq}\n")
        
    for child in graph[node]:
        reconstruct(child, my_seq)

taxa = f1.readline().strip()
graph = {}
d = {}
rd = {}
dna_node = {}
build_tree(taxa, graph, d, rd)
dna = ""
name = ""
for line in f1:
    if (line.startswith(">")):
        #print(name, dna)
        if (name != ""):
            dna_node[rd[name]] = dna
           # print(rd[name], dna, dna_node)
        name = line[1:-1]
        dna = ""
    else:
        dna += line.strip()
dna_node[rd[name]] = dna
#print(graph)
#print(rd["robot"])
ans, tree = dfs(1)
f2.write(f"{ans}\n")
reconstruct(1)
