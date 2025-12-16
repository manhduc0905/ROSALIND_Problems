n = int(input())
ans = 1
mod = 1e6
for i in range(1, 2*(n-2), 2):
    ans = (ans * (i%mod))%mod
print(ans)