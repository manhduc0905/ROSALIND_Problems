import sys
f1 = open('input.INP','r')
f2 = open('output.OUT','w')
dna = ""
for line in f1:
    if not line[0] == '>':
        dna += line.strip()
n = len(dna)
lps = [0]*n
length = 0
i = 1
while i < n:
	if (dna[length] == dna[i]):
		length+=1
		lps[i] = length
		i+=1
	elif (length > 0):
		length = lps[length - 1]
	else:
		length = 0
		lps[i] = 0
		i+=1
f2.write(" ".join(map(str,lps)))
