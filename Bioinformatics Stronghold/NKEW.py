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
        for child, val in graph[cur_node].items():
            if (child not in dist):
                #print(par, goal, cur_node, dist[cur_node], child, val)
                dist[child] = dist[cur_node] + val
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
        graph = {}
        graph[curr_node] = {}
        stk = [curr_node]
        d = {}
        i = 0
        prev = 0
        while i < len(s):
            char = s[i]
            #print(stk)
            if char == '(':
                
                node_count += 1
                #print(node_count)
                new_node = node_count
                
                graph[new_node] = {}
                    
                graph[stk[-1]][new_node] = 1
                graph[new_node][stk[-1]] = 1
                
                stk.append(new_node)
                
            elif char == ',':
                pass
                
            elif char == ')':
                prev = stk.pop()
    
                #print("T",prev)
            elif char == ':':
                i+=1
                start = i
                val = ""
                while i < len(s) and s[i] not in "(),;":
                    val += s[i]
                    i+=1
                val = int(val)
                #print("HIHI",prev,stk[-1], val)
                
                graph[prev][stk[-1]] = val
                graph[stk[-1]][prev] = val
                
            else:
                
                name_start = i
                name_end = -1
                while i + 1 < len(s) and s[i+1] not in "(),;":
                    #print(i, s[i])
                    if (s[i] == ':'):
                        name_end = i
                    i+=1
                if name_end > name_start:
                    name = s[name_start:name_end]
                    #print("MEOW", name_start, name_end)
                    #print(s[name_end+1:i+1])
                    val = int(s[name_end+1:i+1])
                    #print(val)
                    internal_label = (name_start>0 and s[name_start-1] == ")")
                    if (internal_label):
                        #print(name,curr)
                        d[name] = prev
                        graph[prev][stk[-1]] = val
                        graph[stk[-1]][prev] = val
                    else:
                        node_count += 1
                        
                        leaf_node = node_count
                        d[name] = leaf_node
                        #print(curr_node, leaf_node, val)
                        graph[leaf_node] = {}
                        graph[stk[-1]][leaf_node] = val
                        graph[leaf_node][stk[-1]] = val
                        prev = leaf_node
            #print(graph)
            i+=1
    else:
        node1, node2 = line.split()
        # print(d[node1], d[node2])
        # print(d)
        #print(graph)
        # print("START")
        print(bfs(d[node1], d[node2]), end = " ")