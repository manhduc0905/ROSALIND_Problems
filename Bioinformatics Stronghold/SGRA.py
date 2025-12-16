import sys

input_path = input_path = r"C:\Users\admin\OneDrive - Grinnell College\Documents\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
f1 = open(input_path,'r')
f2 = open('output.OUT','w')

table = """A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333 """
mass = {}
for line in table.splitlines():
    line = line.split()
    mass[float(line[1])] = line[0]


L = []
for line in f1:
    line = line.strip()
    L.append(float(line))
L = sorted(L)
n = len(L)
graph = {}
cur_node = 0
node = {}
for right in range(n):
    for left in range(0,right):
        rd = 5
        m = round(L[right] - L[left], rd)
        diff = [-0.00001, 0 , 0.00001]
        for x in diff:
            m1 = round(m + x, rd)
            if m1 in mass:
                if L[left] not in node: 
                    cur_node+=1
                    node[L[left]] = cur_node
                    graph[cur_node] = []

                if L[right] not in node:
                    cur_node+=1
                    node[L[right]] = cur_node
                    graph[cur_node] = []
                
                u = node[L[left]]
                v = node[L[right]]
                graph[u].append((v, mass[m1]))
def dfs(par, curr):
    if par not in graph:
        return curr
    
    max_cur = curr
    for child, val in graph[par]:
        child_curr = dfs(child, curr + val)
        if len(child_curr)> len(max_cur):
            max_cur = child_curr
    return max_cur

print(dfs(1,""))
    