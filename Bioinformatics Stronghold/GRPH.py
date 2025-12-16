f1 = open('input.INP','r')
f2 = open('output.OUT','w')
key =''
d = {}
count = {}
edge = {}
for line in f1:
    if line[0] == '>':
        key = line[1:].strip()
        d[key] = ""
    elif key:
        d[key] += line.strip()
k = 3
for key, value in d.items():
    prefix = value[:k]
    if prefix not in edge:
        edge[prefix] = []
    edge[prefix].append(key)

for key,value in d.items():
    line_write = key + " "
    if value[-k:] in edge:
        for c in edge[value[-k:]]:
            if (c != key):
                count[line_write + c] = 1
                f2.write(line_write + c)
                f2.write("\n")

        
          
