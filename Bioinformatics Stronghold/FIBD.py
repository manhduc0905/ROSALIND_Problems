n,m = map(int,input().split())
f = [[0, 0] for _ in range(n + 2)]
f[1] = [1,0]
f[2] = [0,1]
die = 0
for i in range (2, n+1):
	if (i - m >= 0):
		die = f[i-m][0]
	f[i][0] = f[i-1][1]
	f[i][1] = f[i-1][0] + f[i-1][1] - die 
	
print(f[n][0] + f[n][1])

def fib(n,k):
  ages = [1] + [0]*(k-1)
  print(ages)
  for i in range(0,n-1):
    ages = [sum(ages[1:])] + ages[:-1]
  return sum(ages)

fib(n,m)