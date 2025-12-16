from Bio.Seq import Seq
seq = input()
a = seq.count("A")
g = seq.count("G")
c = seq.count("C")
t = seq.count("T")
print(f"{a} {c} {g} {t}")