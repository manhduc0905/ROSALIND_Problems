n = int(input())
ans = 1
mod = 1e6
for i in range(1, 2*(n-2), 2):
    ans = (ans * (i%mod))%mod
number_nodes = 2*n - 3
ans = (ans * (number_nodes%mod))%mod
print(ans)