mod = 1000000

n = int(input())
result = pow(2, n, mod)
f = [0]*(n+1)
f[0] = 1
f[1] = 1

for i in range(2,n+1):
    f[i] = ((i%mod)*f[i-1])%mod


def nCr(n, r):
    if r < 0 or r > n:
        return 0
    return f[n] // (f[r] * f[n - r])

#### MODULAR INVERSE
sum = 0
for i in range(n+1):
    sum += nCr(n,i)

print(result)