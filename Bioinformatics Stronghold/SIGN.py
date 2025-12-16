f2 = open('output.OUT','w')
n = int(input())
total = 0
ans = set()
def perm(a):
    global total
    if len(a) == n:
        total +=1
        ans.add(tuple(a.copy()))
        #print(a)
        return 
    for i in range (1, n+1):
        if i not in a and -i not in a:
            a.append(i)
            perm(a)
            a.pop()	
            a.append(-i)
            perm(a)
            a.pop()	
    
a = []
perm(a)
f2.write(str(total)+"\n")
for p in ans:
    f2.write(" ".join(map(str, p)))
    f2.write("\n")