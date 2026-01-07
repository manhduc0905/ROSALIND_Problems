#!/usr/bin/env/python
f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")
idx = int(f1.readline().strip())
k = int(f1.readline().strip())

mp = {0:"A",
      1:"C",
      2:"G",
      3:"T"}
ans = []

# for i in range(k-1, -1, -1):
#     base = 4**i
#     #print(idx, ans)
#     for j in range(3, -1, -1):
#         letter = base*j
#         #print(letter)
#         if (letter <= idx):
#             ans.append(mp[j])
#             idx -= letter
#             break
for i in range(k):
        #print(letter)
        ans.append(mp[idx % 4])
        idx = idx // 4
f2.write(''.join(map(str,ans[::-1])))