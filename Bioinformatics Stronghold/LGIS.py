n = int(input())
a = list(map(int, input().split()))
ans = [a[0]]
d = {}
for i in range(1,n+1):
	d[i] = 0
for i in range(1,n):
	if a[i] > ans[-1]:
		d[a[i]] = ans[-1]
		ans.append(a[i])

	else:
		left = 0
		right = len(ans) -1
		while left <= right:
			mid = left + (right - left)//2
			if (ans[mid] < a[i]):
				left = mid +1
			else:
				right = mid - 1
	
		ans[left] = a[i]
		if (left != 0):
			d[a[i]] = ans[left-1]

x = ans[-1]
s = []
s.append( str(x))
while d[x]:
	s.append( str(d[x]))
	x = d[x]

for i in range(len(s)-1,-1,-1):
	print(s[i], end = " ")
print()
ans = [a[0]]
for i in range(1,n+1):
	d[i] = 0
for i in range(1,n):
	if a[i] < ans[-1]:
		d[a[i]] = ans[-1]
		ans.append(a[i])
	else:
		left = 0
		right = len(ans) -1
		while left <= right:
			mid = left + (right - left)//2
			if (ans[mid] > a[i]):
				left = mid +1
			else:
				right = mid - 1
		ans[left] = a[i]
		if (left != 0):
			d[a[i]] = ans[left-1]
x = ans[-1]
s1 = []
s1.append( str(x))
while d[x]:
	s1.append( str(d[x]))
	x = d[x]
for i in range(len(s1)-1,-1,-1):
	print(s1[i], end = " ")