f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")

D = f1.read().split("\n")
graph = {}
sum = 0
length_set = []

for x in D:
    n = len(x)
    if n not in graph:
        graph[n] = 0
    graph[n] += 1
    sum += n

def bs(l,r,a, target):
    while l <= r:
        mid = (l + r)//2
        #print(a[mid], mid, l ,r)
        if (a[mid]/sum >= target):
            l = mid + 1
        else:
            r = mid - 1
    return(l-1)
upper = max(graph.keys())
lower = min(graph.keys())

suf = [0]*(upper + 1)
for i in range(upper, -1, -1):
    sz = 0
    if (i in graph):
        sz = graph[i]
    suf[i] = suf[min(i+1, upper)] + sz*i
f2.write(f"{bs(lower,upper,suf,50/100)} {bs(lower,upper,suf,75/100)}")

