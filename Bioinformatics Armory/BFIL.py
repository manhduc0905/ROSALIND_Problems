#usr/bin/env/python
from Bio import SeqIO
file_path = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Armory\input.INP"
pos = []
f2 = open("output.OUT", "w")
with open(file_path, "r") as f1:
    threshold = int(f1.readline().strip())
    for records in SeqIO.parse(f1, "fastq"):
        temp = records.letter_annotations["phred_quality"].copy()
        dna_seq = []
        score_seq = []
        start = 0
        f2.write("@"+ records.id + "\n")
        while (start < len(temp)):
            if (temp[start] >= threshold):
                break
            start+=1
        end = len(temp) - 1
        while (end >= 0):
            if (temp[end] >= threshold):
                break
            end -= 1
        #print(start,end)
        #print(records.seq)
        f2.write("".join(map(str,records.seq[start:end+1])) + "\n")
        f2.write("+\n")
        f2.write("".join(map(str,(chr(x + 33) for x in temp[start:end+1]))) + "\n")
