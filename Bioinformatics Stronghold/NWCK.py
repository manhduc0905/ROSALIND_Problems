from collections import deque

input_path = input_path = r"C:\Users\admin\OneDrive - Grinnell College\Documents\College\Coding\Bioinformatics Learning\input.INP"
#print(input_path)
f1 = open(input_path,'r')
f2 = open('output.OUT','w')

graph = {}
curr = 0
stk = [curr]
d = {}
def bfs(par, goal):
    q = deque()
    dist = {}
    dist[par] = 0
    trace = {}
    trace[par] = -1
    q.append(par)
    while q:
        cur_node = q.popleft()
        for child in graph[cur_node]:
            if (child not in dist):
                #print(par, goal, cur_node, dist[cur_node], child)
                dist[child] = dist[cur_node] + 1
                trace[child] = par
                if (child == goal):
                    break
                q.append(child)
    #print("GO", dist[goal])
    # child = goal
    # while (trace[child] != -1):
        # print(child)
        # child = trace[child]
    return dist[goal]
        


for line in f1:
    line = line.strip()
    if not line: 
        continue
    
    if (line[-1:] == ";"):
        s = line
        curr_node = 0
        node_count =0
        graph[curr_node] = []
        stk = []
        d = {}
        i = 0
        prev = 0
        while i < len(s):
            char = s[i]
            print(stk)
            if char == '(':
                node_count += 1
                new_node = node_count
                
                graph[curr_node].append(new_node)
                graph[new_node] = [curr_node]
                
                stk.append(curr_node)
                curr_node = new_node
                
            elif char == ',':
                pass
                
            elif char == ')':
                prev = curr_node
                curr_node = stk.pop()
                
            else:
                
                name_start = i
                while i + 1 < len(s) and s[i+1] not in "(),;":
                    i+=1
                name = s[name_start:i+1]
                #print(curr_node,name)
                internal_label = (name_start>0 and s[name_start-1] == ")")
                #print(name[::-1], i, s[i-1], internal_label)
                if (internal_label):
                    #print(name,curr)
                    d[name] = prev
                else:
                    node_count += 1
                    
                    leaf_node = node_count
                    d[name] = leaf_node
                    
                    graph[curr_node].append(leaf_node)
                    graph[leaf_node] = [curr_node]
            
            i+=1
    else:
        node1, node2 = line.split()
        # print(d[node1], d[node2])
        # print(d)
        # print(graph)
        # print("START")
        print(bfs(d[node1], d[node2]), end = " ")