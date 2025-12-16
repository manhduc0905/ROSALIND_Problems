input_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\input.INP"
output_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\output.OUT"
f1 = open(input_path, 'r')
f2 = open(output_path,'w')

n = int(f1.readline().strip())
a = list(map(int,f1.readline().strip().split()))
graph = {}
def insert(pos):
    if (pos == 0):
        return
    par = (pos - 1)//2
    if (graph[par] < graph[pos]):
        graph[par],graph[pos] = graph[pos], graph[par]
        insert(par)
def update(pos, end):
    largest = pos
    child_left = pos*2 + 1
    child_right = pos*2 + 2
    if (child_left < end and graph[child_left] > graph[largest]):
        largest = child_left
    if (child_right < end and graph[child_right] > graph[largest]):
        largest = child_right
    if (largest != pos):
        graph[pos], graph[largest] = graph[largest], graph[pos]
        update(largest, end)
        

graph[0] = a[0]
for i in range(1,n):
    graph[i] = a[i]
    insert(i)
ans = []
for i in range(n-1,-1,-1):
    ans.append(graph[0])
    graph[0] = graph[i]
    graph[i] = -1
    update(0, i)
f2.write(" ".join(map(str, ans[::-1])))
