from collections import deque
from collections import defaultdict
f1 = open('input.INP','r')
f2 = open('output.OUT','w')
temp = None
a = []

def Hamming(s1,s2):
    n = len(s1)
    count = 0
    for i in range(n):
        if (s1[i] != s2[i]):
            count+=1
    return count

def revseq(seq, i, j):
    sublist = seq[i : j + 1]
    sublist.reverse()
    seq[i : j + 1] = sublist
    return seq
        
perm_seq = []
path = {}
def perm(a,n):
    if len(a) == n:
        perm_seq.append(a.copy())
        #print(a)
        return 
    for i in range (1, n+1):
        if i not in a:
            a.append(i)
            perm(a,n)
            a.pop()	

for line in f1:
    if line == "\n":
        continue  
    line = line.strip()
    if temp is None:
        temp = list(map(int, line.split()))  
    else:
        a.append([temp, list(map(int, line.split()))])  
        temp = None
        
def minpath(seq, target,path):
    target = tuple(target)
    seq = tuple(seq)
    n = len(seq)
    if target == seq:
        return 0
    visited = {}
    visited[seq] = 1
    lst = deque([(seq, 0)])  

    while lst:
        print(curr_seq)
        curr_seq, curr_dist = lst.popleft()
        print(curr_seq, curr_dist)
        print(path[curr_seq])
        for next_seq in path[curr_seq]:
                if next_seq == target:
                    return curr_dist + 1
                if next_seq not in visited:
                    visited[next_seq] = 1
                    lst.append((next_seq, curr_dist + 1))

def min_get(target, seq):
    target = tuple(target)
    seq = tuple(seq)
    n = len(seq)
    if target == seq:
        return 0
    visited_start = {}
    visited_start[seq] = 0
    visited_target = {}
    visited_target[target] = 0
    trace_s = {}
    trace_t = {}
    trace_s[seq] = ('X', 0, 0)
    trace_t[target] = ('X',0,0)
    lst_start = deque([(seq)])  
    lst_target = deque([(target)])
    depth = 0
    while lst_start and lst_target:
        depth+=1
        sz_start = len(lst_start)
        if (sz_start == 0):
            break
        for _ in range(sz_start):
            curr_seq = tuple(lst_start.popleft())
            for i in range(n):
                for j in range(i + 1, n):
                    next_seq = tuple(revseq(list(curr_seq).copy(), i, j))   
                    if next_seq in visited_target:
                        trace_s[next_seq] = (curr_seq, i+1, j+1)
                        return (depth + visited_target[next_seq], trace_t, trace_s, next_seq)
                    if next_seq not in visited_start:
                        trace_s[next_seq] = (curr_seq, i+1, j+1)
                        visited_start[next_seq] = depth 
                        lst_start.append((next_seq))
        sz_target = len(lst_target)
        if (sz_target == 0):
            break
        for _ in range(sz_target):
            curr_seq1 = tuple(lst_target.popleft())
            for i in range(n):
                for j in range(i + 1, n):
                    next_seq = tuple(revseq(list(curr_seq1).copy(), i, j))   
                    if next_seq in visited_start:
                        trace_t[next_seq] = (curr_seq1, i+1, j+1) 
                        return (depth + visited_start[next_seq], trace_t, trace_s, next_seq)
                    if next_seq not in visited_target:
                        trace_t[next_seq] = (curr_seq1, i+1, j+1) 
                        visited_target[next_seq] = depth
                        lst_target.append((next_seq))
    return -1, None, None, None

#len_seq = 10
#b = []
#perm(b,len_seq)
path = defaultdict(list)
for target,seq in a:
    #print(target,seq)
    #print(perm_seq)
    #for c in perm_seq:
    #    if (c != target):
    #        for length in range(1, n):
    #            for i in range(n - length) :
    #                rev = tuple(revseq(c.copy(),i,i+ length))
    #                path[tuple(c)].append(rev)
    #                print(i,length, c, rev)
    #print(path[tuple(seq)])
    #print(minpath(seq,target, path))
    ans = min_get(target,seq)
    f2.write(str(ans[0]))
    f2.write("\n")

    trace_s = ans[1]
    trace_t = ans[2]
    backer = tuple(ans[3])
    printer = deque()
    
    print(backer)
    while trace_s[backer][0] != 'X':
        predecessor, left, right = trace_s[backer]
        #print(predecessor)
        printer.appendleft(f"{left} {right}\n")
        backer = predecessor

    backer = tuple(ans[3])
    while trace_t[backer][0] != 'X':
        predecessor, left, right = trace_t[backer]
        #print(predecessor)
        printer.append(f"{left} {right}\n")
        backer = predecessor
    for positions in printer:
        f2.write(positions)
                    
