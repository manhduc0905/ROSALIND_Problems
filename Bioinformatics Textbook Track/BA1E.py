f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")
from collections import deque
seq = f1.readline().strip()
n, L, t = map(int, f1.readline().strip().split())
mp = {}
ans = set()
for i in range(len(seq)):
    temp = seq[i:i+n]
    if (temp not in mp): mp[temp] = []
    mp[temp].append(i)
    if (temp not in ans and len(mp[temp]) >= t):
        ans.add(temp)

def check_range1(lst, rg, t):
    lb = lst[0]
    ub = lb + rg
    cnt = 1
    stk = deque([lst[0]])
    for i in range(1,len(lst)):
        if (lb <= lst[i] and lst[i] <= ub):
            stk.append(lst[i])
            if (len(stk) >= t):
                return True
        else:
            cur = lst[i]
            stk.append(lst[i])
            while True:
                front = stk.popleft()
                if (cur <= front + rg):
                    stk.appendleft(front)
                    lb = front
                    ub = front + rg
                    break
    return False

def check_range2(lst, L, t, k_mer_len):
    for i in range(len(lst) - t + 1):
        if lst[i + t - 1] - lst[i] <= L - k_mer_len: 
            return True
    return False

for motif in ans:
    if (check_range2(mp[motif], L, t, n)):
        f2.write(motif + " ")