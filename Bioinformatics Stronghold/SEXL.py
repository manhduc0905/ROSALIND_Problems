a = list(map(float,input().split()))
for x in a:
	q = x
	p = (1-x)
	pq = 2*p*q
	print(2*x*(1-x), end = " ")