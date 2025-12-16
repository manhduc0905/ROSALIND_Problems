s = input().split()
k = int(input())
s.sort()

def gen(s1, n):
	if (n == k):
		print(s1)
		return
	for c in s:
		gen(s1 + c, n+1)
		
gen("", 0)
