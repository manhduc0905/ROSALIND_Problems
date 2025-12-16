s = input()
s1 = input()
n = len(s)
k = len(s1)
i = 0
j = 0
def check(j,n,k,v):
	return (j < n) and (j < j + k) and (v < k)and (s[j] == s1[v])
while i < n:
	if (s[i] == s1[0]):
		j = i+1
		v = 1
		while check(j,n,k,v):
			v+=1
			j+=1
	if (i + k == j):
		print(i+1, end = " ")
	i+=1
			
		
	