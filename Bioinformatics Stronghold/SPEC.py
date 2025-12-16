f1 = open('input.INP','r')
f2 = open('output.OUT','w')
num = 0
table = """A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333 """
mass = {}
for line in table.splitlines():
    line = line.split()
    mass[float(line[1])] = line[0]

print(mass)
a = []
prev = 0
for line in f1:
    if (prev != 0):
        diff = float(line.strip()) - prev
        min_dif = 1000
        minus = 0
    
        for val,key in mass.items():
            dif = abs(val - diff)
            if (dif < min_dif):
                min_dif = dif
                minus = key
        print(diff, prev, minus)
        f2.write(minus)
        print(diff)
        prev = float(line.strip())
    else:
        prev = float(line.strip())