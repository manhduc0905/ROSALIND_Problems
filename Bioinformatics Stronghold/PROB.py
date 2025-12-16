import math
DNA_string = input()
a = list(map(float,input().split()))
d = {}

for GC_content in a:
	Cprob = GC_content/2
	Aprob = (1-GC_content)/2
	res = 1
	for char in DNA_string:
		if (char == "A" or char == "T"):
			res *= Aprob
		else:
			res*= Cprob
	print(math.log10(res), end = " ")