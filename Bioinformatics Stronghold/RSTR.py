line = input().split()
n = int(line[0])
m = float(line[1])
s = input()
GC_content = {
	'A': (1-m)/2,
	'T': (1-m)/2, #purine
	'C': m/2,
	'G': m/2 #pyridmidines
}
#Probability of generating s:
sprob = 1
for nu in s:
	sprob *= GC_content[nu]

#Probability of not generating s:
nsprob = 1 - sprob

#Probability of not s for N DNA strings
Nnsprob = nsprob**n
#Probability of at least one DNA string that equals to s
print(1-Nnsprob)
