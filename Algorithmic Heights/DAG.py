input_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\input.INP"
output_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\output.OUT"
f1 = open(input_path, 'r')
f2 = open(output_path,'w')

k = int(f1.readline().strip())
n = 0
m = 0
edges = {}
vis = {}
col = {}
flag = True
def dfs(par, vis2):
    global flag
    if (par in vis2):
        flag = False
        return
    if (par in vis):
        return
    vis[par] = 1
    vis2[par] = 1
    for x in edges[par]:
            dfs(x, vis2)
    del vis2[par]
    
for line in f1:   
    print()                                                                                                                                                         
    n,m = map(int, f1.readline().strip().split())
    edges = { _:[] for _ in range(1,n+1)}
    vis = {}
    vis2 = {}
    flag = True
    
    for i in range(m):
        u,v = map(int, f1.readline().strip().split())
        edges[u].append(v)
    print(edges)
    flag2 = True
    for i in range(1,n+1):
        if (i not in vis):
            dfs(i, vis2)
    if (flag == False): 
        f2.write(f"{-1} ")
    else:
        f2.write(f"1 ")
        
            
        

