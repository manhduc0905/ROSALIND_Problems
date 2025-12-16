
input_path = input_path = r"C:\Users\admin\OneDrive - Grinnell College\Documents\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
#print(input_path)
f1 = open(input_path,'r')
f2 = open('output.OUT','w')
ions = []
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


for line in f1:
    line = float(line.strip())
    if (num == 0):
        par_mass = round(line,5)
    else:
        ions.append(round(line,5))
    num+=1

ions = sorted(ions)
number_b_ions = (num-1)//2 - 1
match = ""
w1 = par_mass - ions[-1]


def matching(pos, ans, w):
    cur = 1000
    if (pos == number_b_ions):
        print(ans)
        return
    for val, key in mass.items():
        diff = val + w
        for i in range(len(ions)):
            
            dif = abs(ions[i] - diff)
            if cur > dif: 
                new_w = diff
                match = key
                cur = dif
    
    matching(pos+1,ans+match, new_w)
matching(0, "", w1)
        