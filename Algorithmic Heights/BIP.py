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
def dfs(par):
    global flag
    vis[par] = 1
    #print(par)
    for x in edges[par]:
        if (x not in vis):
            col[x] = 1 - col[par]
            dfs(x)
        else:
            if (col[x] == col[par]):
                flag = False
    
for line in f1:
    if (line == "\n"):
        n,m = map(int, f1.readline().strip().split())
        edges = { _:[] for _ in range(1,n+1)}
        check = { False:[] for _ in range(1,n+1)}
        vis = {}
        col = {}
        flag = True
        for i in range(m):
            u,v = map(int, f1.readline().strip().split())
            edges[u].append(v)
            edges[v].append(u)
        
        for i in range(1,n+1):
            col[i] = 1
            if (i not in vis):
                dfs(i)
        if (flag): 
            f2.write(f"{1} ")
        else:
            f2.write(f"{-1} ")
        

