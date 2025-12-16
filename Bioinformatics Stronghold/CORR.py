from collections import deque
f1 = open('input.INP','r')
f2 = open('output.OUT','w')

key =''
edge = []
num = -1
temp = ""        
d = {}
def revcomp(s):
    return s.translate(str.maketrans('ACTG','TGAC'))[::-1]

def Hamming(s1,s2):
    n = len(s1)
    count = 0
    for i in range(n):
        if (s1[i] != s2[i]):
            count+=1
    return count

def checker(cur_seq,c):
    rev = revcomp(c)
    if (Hamming(cur_seq,c) == 1):
            printer = cur_seq + "->" + c + "\n"
            f2.write(printer)
            return True
    elif (Hamming(cur_seq, rev) == 1):
            printer = cur_seq + "->" + rev + "\n"
            f2.write(printer)
            return True
    elif (Hamming(cur_seq,rev) == 0 or Hamming(cur_seq,c) == 0):
            return True
    return False
            


for line in f1:
    if line[0] == '>':
        if temp != "":
            edge.append(temp)
            if temp not in d:
                d[temp] = 1
            else:
                d[temp] += 1
        temp = ""
    else:
        temp += line.strip()

edge.append(temp)
if temp not in d:
    d[temp] = 1
else:
    d[temp] += 1
correct = []
incor = []
incorrect = deque()
for key, value in d.items():
    rev = revcomp(key)
    if (value >= 2):
        correct.append(key)
    elif (rev in d and d[rev] >= 2):
        correct.append(key)
    else : 
        incorrect.append(key)
        incor.append(key)
n = len(incorrect)

while incorrect:
    cur_seq = incorrect[0]
    print(cur_seq)
    flag = False
    for c in correct:
        flag = checker(cur_seq,c)
        if flag:
            incorrect.popleft()
            break
    if not flag:
        for c in incorrect:
            if (c == cur_seq):
                continue
            flag = checker(cur_seq,c)
            if flag:
                incorrect.popleft()
                break
    if not flag:
        incorrect.popleft()
    