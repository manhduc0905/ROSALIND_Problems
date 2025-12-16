f1 = open('input.INP','r')
f2 = open('output.OUT','w')
seq = []
temp = ""
d = {}
d['A'] = 1
d['G'] = 1
d['C'] = 0
d['T'] = 0
def Rratio(s1,s2):
    transitions = 0
    transverstions = 0
    for i in range(len(s1)):
        if (s1[i] != s2[i]):
            types1 = d[s1[i]]
            types2 = d[s2[i]]
            if (types1 != types2):
                transverstions+=1
            else:
                transitions+=1     
    print(transitions, transverstions) 
    return transitions/transverstions


for line in f1:
    if line[0] == '>':
        if (temp != ""):
            seq.append(temp)
        temp = ""   
    else:
        temp += line.strip()
if (temp != ""):
    seq.append(temp)

seq1 = " " + seq[0]
seq2 = " " + seq[1]   
f2.write(str(Rratio(seq1,seq2)))
