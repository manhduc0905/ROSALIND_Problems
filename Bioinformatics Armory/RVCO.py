from Bio import SeqIO
f1 = open("input.INP", "r")
total = 0
for record in SeqIO.parse(f1, "fasta"):
    dna = record.seq
    if (dna == dna.reverse_complement()):
        total += 1
print(total)
