f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")

n = int(f1.readline().strip())
#print(list(map(float,f1.readline().strip())))
a = list(map(float, f1.readline().strip().split()))
for x in a:
    f2.write(f"{x*n} ")
