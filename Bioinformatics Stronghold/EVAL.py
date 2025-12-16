n = int(input())
dna = input()
a = list(map(float,input().split()))
number_dna = n - len(dna) +1
d = {
	'A':'A',
	'G':'G',
	'T':'A',
	'C':'G',
}
d1 = {
	'A':0,
	'G':0
}

for GC_content in a:
	prob = 1.0
	for nu in dna:
		if (d[nu] == 'A'):
			prob *= (1 - GC_content)/2.0
		else:
			#print(prob, GC_content/2.0)
			prob *=  GC_content/2.0
			#print(prob)
	
	print(prob*number_dna,end = " ")
	