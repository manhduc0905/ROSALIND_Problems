from Bio import SeqIO
file_path = r"C:\Users\admin\Downloads\rosalind_phre (1).txt"

f2 = open("output.OUT", "w")
count = 0
with open(file_path, "r") as f1:
    threshold = int(f1.readline().strip())
    for record in SeqIO.parse(f1, "fastq"):
        quality = sum(record.letter_annotations["phred_quality"])
        q_avg = quality / len(record.seq)
        print(q_avg)
        if (q_avg < threshold): count += 1
f2.write(f"{count}\n")
        # print(f">{record.id}")
        # print(record.seq)


