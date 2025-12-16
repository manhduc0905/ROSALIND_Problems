f1 = open('input.INP','r')
f2 = open('output.OUT','w')
dna = ""
num = -1
seq = []
def Hamming(s1,s2):
    n = len(s1)
    cnt = 0
    for i in range (0,n):
        if (s1[i] != s2[i]):
            cnt +=1
    return cnt

for line in f1:
    if line[0] == '>':
        num+=1
        if (dna != ""):
            seq.append(dna)
            dna = ""
    else:
        dna += line.strip()
num +=1
seq.append(dna)
n = len(dna)
print(n)
for i in range(num):
    for j in range(num):
        if (i == j):
            f2.write("0.0 ")
        else:
            f2.write(str(Hamming(seq[i],seq[j])/(n*1.0)) + " ")
    f2.write("\n")
