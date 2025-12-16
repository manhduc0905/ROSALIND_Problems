n,k = input().split()
n = int(n)
k = int(k)
f = [0]*(n+1)
f[0] = 0
f[1] = 1

for i in range (2,n+1):
	f[i] = f[i-1] + f[i-2]*k
print(f[n])