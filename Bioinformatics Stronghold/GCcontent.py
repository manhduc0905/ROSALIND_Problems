#GC-content is used to distinguish species with each other
#This problem needs to find the DNA with highest GC-content

f1 = open('input.INP','r')
f2 = open('output.OUT','w')
key =''
d = {}

def GCcontent(s):
    cnt = 0
    length = len(s)
    for c in s:
        if (c == 'G' or c == 'C'):
            cnt+=1
    return ((cnt/length)*100)


for line in f1:
    if line[0] == '>':
        key = line[1:]
        d[key] = ""
    elif key:
        d[key] += line.strip() 
ans = [0, -1]
GC = 0
for key,value in d.items():
    GC = GCcontent(value)
    if ans[1] < GC:
        ans = [key,GC]
output_string = f"{ans[0]}{ans[1]}"
f2.write(output_string)

        
          
