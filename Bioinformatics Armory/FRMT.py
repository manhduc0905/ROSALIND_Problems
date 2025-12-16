from Bio import Entrez
from Bio import SeqIO
Entrez.email = "hacker@edu.org"

f2 = open("output.OUT", "w")
id_inp = input().split()
#id_inp = "FJ817486 JX069768 JX469983".split()
n = len(id_inp)
#print(n)
handle = Entrez.efetch(db = "nucleotide", id = id_inp, rettype = "fasta")
records = list (SeqIO.parse(handle, "fasta"))
min1 = 1000000
for i in range(n):
    if (min1 > len(records[i].seq)):
        min1 = len(records[i].seq)
        ind = i
f2.write(f">{records[ind].description}" + "\n")
f2.write(f"{records[ind].seq}")
