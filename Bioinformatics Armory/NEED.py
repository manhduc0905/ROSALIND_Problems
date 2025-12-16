from Bio import Entrez, SeqIO, Align
from Bio.Align import substitution_matrices
import numpy as np
import Bio
dnafull = """
    A   T   G   C   S   W   R   Y   K   M   B   V   H   D   N
A   5  -4  -4  -4  -4   1   1  -4  -4   1  -4  -1  -1  -1  -2
T  -4   5  -4  -4  -4   1  -4   1   1  -4  -1  -4  -1  -1  -2
G  -4  -4   5  -4   1  -4   1  -4   1  -4  -1  -1  -4  -1  -2
C  -4  -4  -4   5   1  -4  -4   1  -4   1  -1  -1  -1  -4  -2
S  -4  -4   1   1  -1  -4  -2  -2  -2  -2  -1  -1  -3  -3  -1
W   1   1  -4  -4  -4  -1  -2  -2  -2  -2  -3  -3  -1  -1  -1
R   1  -4   1  -4  -2  -2  -1  -4  -2  -2  -3  -1  -3  -1  -1
Y  -4   1  -4   1  -2  -2  -4  -1  -2  -2  -1  -3  -1  -3  -1
K  -4   1   1  -4  -2  -2  -2  -2  -1  -4  -1  -3  -3  -1  -1
M   1  -4  -4   1  -2  -2  -2  -2  -4  -1  -3  -1  -1  -3  -1
B  -4  -1  -1  -1  -1  -3  -3  -1  -1  -3  -1  -2  -2  -2  -1
V  -1  -4  -1  -1  -1  -3  -1  -3  -3  -1  -2  -1  -2  -2  -1
H  -1  -1  -4  -1  -3  -1  -3  -1  -3  -1  -2  -2  -1  -2  -1  
D  -1  -1  -1  -4  -3  -1  -1  -3  -1  -3  -2  -2  -2  -1  -1
N  -2  -2  -2  -2  -1  -1  -1  -1  -1  -1  -1  -1  -1  -1  -1
"""
table = dnafull.strip().split("\n")
header = table[0].split()
alphabet = "".join(header)
values = []
for line in table[1:]:
    row_values = [int(x) for x in line.split()[1:]]
    values.append(row_values)

values = np.array(values)
custom_matrix = substitution_matrices.Array(alphabet=alphabet, dims=2, data=values)
print(custom_matrix)
# name = input().split()
# Entrez.email = "bioinformatics@edu.org"
# handle1 = Entrez.efetch(db = "nucleotide", id = name[0], rettype = "gb", retmode = "text")
# handle2 = Entrez.efetch(db = "nucleotide", id = name[1], rettype = "gb", retmode = "text")

# rec1 = SeqIO.read(handle1, "genbank")
# rec2 = SeqIO.read(handle2, "genbank")

# handle1.close()
# handle2.close()

# aligner = Align.PairwiseAligner()
# aligner.open_gap_score = -10
# aligner.extend_gap_score = -1
# aligner.substitution_matrix = Bio.Align.substitution_matrices.load("NUC.4.4")
# #aligner.substitution_matrix = custom_matrix
# print(int(aligner.score(rec1.seq, rec2.seq)))


