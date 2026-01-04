f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")
n = int(f1.readline().strip())
a = list(map(int,f1.readline().strip().split()))

def partition(a, l , r):
    pivot = a[r]
    i = l - 1
    for j in range(l, r):
      if (a[j] < pivot):
        i+=1
        swap(a, i , j)
    swap(a, i+1, r)
    return i+1
    
def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def qs(a, l, r):
    if l < r:
        pi = partition(a,l,r)
        qs(a, l, pi-1)
        qs(a, pi+1, r)
    return a
      
ans = qs(a, 0, n-1)
f2.write(f"{" ".join(map(str,ans))}")  