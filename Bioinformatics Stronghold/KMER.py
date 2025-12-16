import sys

head = (sys.stdin.readline().strip())
dna = ""
for line in sys.stdin:
	dna += line.strip()
nu = "ACGT"
ans = []
d = {}
def mer_4(a):
	if (len(a) == 4):
		d[a] = 0
		ans.append(a)
		return
	for char in nu:
		a += char
		mer_4(a)
		a = a[:-1]
mer_4("")

for i in range(len(dna) - 4 + 1):
	d[dna[i:i+4]]+=1
for mer in ans:
	print(d[mer], end = " ")
