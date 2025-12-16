f1 = open('input.INP','r')
f2 = open('output.OUT','w')
seq = []
temp = ""
for line in f1:
    if line[0] == '>':
        if (temp != ""):
            seq.append(temp)
        temp = ""   
    else:
        temp += line.strip()
if (temp != ""):
    seq.append(temp)

DNA_string = seq[0]
motif = seq[1]   
n = len(DNA_string)
num = 0
pos = []
for i in range(n):
    if (DNA_string[i] == motif[num]):
        pos.append(i+1)
        num+=1
    if (num == len(motif)):
        for c in pos:
            f2.write(str(c) + " ")
        break
    


