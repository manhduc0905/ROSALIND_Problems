f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")
motif = f1.readline().strip()
seq = f1.readline().strip()
for i in range(len(seq) - len(motif)):
    if (seq[i:i+len(motif)] == motif):
        f2.write(f"{i} ")
