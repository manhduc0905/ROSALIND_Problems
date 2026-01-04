from Bio import SeqIO
f1 = open("input.INP", "r")
q,p = map(int,f1.readline().strip().split())
total = 0
for record in SeqIO.parse(f1, "fastq"):
    flag = True
    good = 0
    lst = (record.letter_annotations["phred_quality"])
    avg_qual = sum(lst)/len(lst)
    for x in lst:
        if (x >= q):
            good += 1
    if good/len(lst)*100 >= p and avg_qual >= q:    
        total +=1
print(total)
