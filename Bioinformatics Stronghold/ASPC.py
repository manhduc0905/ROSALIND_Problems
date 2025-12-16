f1 = open('input.INP','r')
f2 = open('output.OUT','w')
mod = 1000000
n,m = map(int, f1.readline().split())
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j])%mod
sum = 0
for i in range(m,n+1):
    sum = (sum + dp[n][i])%mod
f2.write(str(sum))

