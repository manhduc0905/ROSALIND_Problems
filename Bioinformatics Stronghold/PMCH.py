f1 = open('input.INP','r')
f2 = open('output.OUT','w')
dna = ""
for line in f1:
    if not line.startswith('>'): 
        dna += line.strip() 
d = {
    'A': 0,
    'U': 0,
    'C': 0,
    'G': 0
}
for nu in dna:
    d[nu]+=1
n1 = min(d['A'], d['U'])
pair1 = 0
if (n1 != 0):
    pair1 = 1
n11 = d['A'] + d['U'] - n1

for i in range(1,n1+1):
    pair1*= (n11)
    n11-=1
pair2 = 0
n2 = min(d['C'], d['G'])
if (n2 != 0):
    pair2 = 1
n22 = d['C'] + d['G'] - n2
for i in range(1,n2+1):
    pair2*= (n22)
    n22-=1
# print(d)
# print(pair1,pair2)
f2.write(str(pair1*pair2))
