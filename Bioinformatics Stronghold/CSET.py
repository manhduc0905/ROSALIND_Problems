f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")

D = f1.read().split('\n')[:-1]
print(D)
def conflict(x,y, x1,y1):
    return ((x & y) and (x & y1) and (x1 & y) and (x1&y1))
def check(graph):
    flag = True
    n = (1 << len(graph[0])) -1
    cols = [int(_, 2) for _ in graph]
    n1 = len(cols)
    for i in range(n1):
        for j in range(i+1, n1):
            S1 = cols[i]
            S1c = n^S1
            S2 = cols[j]
            S2c = n^S2
            if conflict(S1, S2, S1c, S2c):
                return False
    return True
                


for i in range(len(D)):
    graph = D[:i] + D[i+1:]
    #print(check(graph))
    if check(graph):
        f2.write("\n".join(map(str,(graph))))
        break