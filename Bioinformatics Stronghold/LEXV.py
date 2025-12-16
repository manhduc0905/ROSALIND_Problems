f2 = open('output.OUT','w')
s = input().split()
k = int(input())

def gen(s1, n):
	f2.write(s1 + "\n")
	if (n == k):
		return
	for c in s:
		gen(s1 + c, n+1)
		
gen("", 0)
