input_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
output_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\output.OUT"
f1 = open(input_path, 'r')
f2 = open(output_path,'w')

def rc(s):
    return s.translate(str.maketrans("ATCG", "TAGC"))


reads = []
graph = {}
for line in f1:
    line = line.strip()
    reads.append(line)
    reads.append(rc(line)[::-1])

m = len(reads[0])

def de_brujin(k):
    graph = {}
    
    for x in reads:
        for i in range(0, m - k ):
            prefix = x[i:i + k]
            suffix = x[i+1: i + k + 1]
            graph[prefix] = suffix
            
    return graph


def cycle(k):
    graph = de_brujin(k)
    start = list(graph.keys())[0]
    curr = start
    path = ""
    while True:
        if curr not in graph:
            return False
        path = path + curr[0]
        curr = graph[curr]
        if (curr == start):
            return path
    


for k in range(m-1, 1, -1):
    s = cycle(k)
    if (s):
        print(s)
        f2.write(s)
        break
    

