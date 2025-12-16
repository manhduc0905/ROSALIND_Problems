f1 = open('input.INP','r')
f2 = open('output.OUT','w')
d = {}
for line in f1:
    if line[0] == '>':
        key = line[1:].strip()
        d[key] = ""
    elif key:
        d[key] += line.strip()

def revcomp(s):
    return s.translate(str.maketrans('ACTG','TGAC'))[::-1]

for key,s in d.items():
    n = len(s)
    print(s[3:3+6])
    for i in range(n):
        for length in range(4,13):
            if (i + length -1< n):
                curr = s[i:i+length]
                revcurr = curr[::-1] 
                other_strcurr = revcomp(curr)
                if (curr == other_strcurr):
                    print(i+1, length)
                    f2.write(str(i+1) + " " + str(length) + "\n")
