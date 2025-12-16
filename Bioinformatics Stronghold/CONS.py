f1 = open('input.INP','r')
f2 = open('output.OUT','w')
key =''
d = {}
d[0] = 'A'
d[1] = 'C'
d[2] = 'G'
d[3] = 'T'
profile = []
a = []
i = -1

for line in f1:
    if line[0] == '>':  
        i+=1
        a.append("")
    else:
        a[i] += line.strip() 
seqlen = len(a[0])
for l in range (0,4):
    b = [0]*seqlen
    #print (d[l], end = ":")
    for k in range (0,seqlen):
        for j in range (0,i+1):
            #print(a[j][k], end = "")
            if (a[j][k] == d[l]):
                b[k] += 1
    #print("\n")
    profile.append(b)
s = ""
for j in range (0, seqlen):
    maxer = -1
    c = ''
    for k in range (0, 4):
        if maxer < profile[k][j]:
            maxer = profile[k][j]
            c = d[k]
    s += c
f2.write(s + '\n')
for k in range (0,4):
    line_write = d[k] + ": "
    for j in range (0, seqlen):
        line_write += str(profile[k][j]) + " "  
    line_write += '\n'
    f2.write(line_write)


    
        
          
