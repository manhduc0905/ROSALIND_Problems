import math
k,n = map(int,input().split())
sum = 0
def nCr(n, r):
    if r < 0 or r > n:
        return 0
    f = math.factorial
    return f(n) // (f(r) * f(n - r))
pop = 2**k
for i in range(n, pop + 1):
	sum += nCr(pop,i)*(0.25**i)*(0.75**(pop-i))
print(sum)