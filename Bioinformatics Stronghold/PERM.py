n = int(input())
total = 0
ans = []
def perm(a):
	global total
	if len(a) == n:
		total +=1
		ans.append(a.copy())
		#print(a)
		return 
	for i in range (1, n+1):
		if i not in a:
			a.append(i)
			perm(a)
			a.pop()	

a = []
perm(a)
print(total)
for p in ans:
    print(" ".join(map(str, p)))