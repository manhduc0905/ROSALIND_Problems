from Bio import SeqIO
import numpy as np
file_path = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Armory\input.INP"
pos = []
f2 = open("output.OUT", "w")
with open(file_path, "r") as f1:
    threshold = int(f1.readline().strip())
    #print(threshold)
    for records in SeqIO.parse(f1, "fastq"):    
            pos.append(records.letter_annotations["phred_quality"])
pos = np.array(pos)
mean_pos = np.mean(pos, axis = 0)
count = np.sum(mean_pos < threshold)
f2.write(f"{count}")