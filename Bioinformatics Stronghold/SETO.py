f1 = open('input.INP','r')
f2 = open('output.OUT','w')
num = 0
a = set()
b = set()
for line in f1:
    if (num == 0):
        n = int(line.strip())
    elif line.startswith('{'):
        curr = ""
        for ch in line.strip():
            if (ch.isdigit()):
                curr += ch
            else:
                if (curr != ""):
                    if (curr.isdigit()):
                        if (num == 1):
                            a.add(int(curr))
                        else:
                            b.add(int(curr))
                curr = ""
    num+=1
n1 = len(a)
n2 = len(b)
c = set()
for ch in a:
    c.add(ch)
for ch in b:
    c.add(ch)

d = set()
for ch in a:
    if ch in b:
        d.add(ch)

e = set()
for ch in a:
    if ch not in b:
        e.add(ch)

f = set()
for ch in b:
    if ch not in a:
        f.add(ch)

g = set()
for i in range(1, n+1):
    if i not in a:
        g.add(i)

h = set()
for i in range(1, n+1):
    if i not in b:
        h.add(i)
f2.write('{' + ', '.join(map(str, c)) +'}' + "\n")
f2.write('{' + ', '.join(map(str, d)) +'}' + "\n")
f2.write('{' + ', '.join(map(str, e)) +'}' + "\n")
f2.write('{' + ', '.join(map(str, f)) +'}' + "\n")
f2.write('{' + ', '.join(map(str, g)) +'}' + "\n")
f2.write('{' + ', '.join(map(str, h)) +'}' + "\n")