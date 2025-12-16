import math
n,k = map(int,input().split())
sum = 0
mod = 1000000
def nPr(n, r):
    if r < 0 or r > n:
        return 0
    f = [0]*(n+1)
    f[0] = 1
    for i in range (1, n):
        f[i] = i* f[i-1]
        f[i] %= mod
    
    return f[n]/(f[n-r])    

print(nPr(n,k))