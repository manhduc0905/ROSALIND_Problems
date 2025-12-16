from Bio import SeqIO
file_path = r"C:\Users\admin\Downloads\rosalind_tfsq (1).txt"
#out_path = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Armory"
record = list(SeqIO.parse(file_path, "fastq"))
f2 = open("output.OUT", "w")
for i in range(len(record)):
    f2.write(f">{record[i].id}\n")
    f2.write(f"{record[i].seq}\n")
    # print(f">{record.id}")
    # print(record.seq)


