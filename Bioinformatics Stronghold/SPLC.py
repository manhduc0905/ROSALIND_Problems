f1 = open('input.INP','r')
f2 = open('output.OUT','w')
string = """TTT F      CTT L      ATT I      GTT V
TTC F      CTC L      ATC I      GTC V
TTA L      CTA L      ATA I      GTA V
TTG L      CTG L      ATG M      GTG V
TCT S      CCT P      ACT T      GCT A
TCC S      CCC P      ACC T      GCC A
TCA S      CCA P      ACA T      GCA A
TCG S      CCG P      ACG T      GCG A
TAT Y      CAT H      AAT N      GAT D
TAC Y      CAC H      AAC N      GAC D
TAA Stop   CAA Q      AAA K      GAA E
TAG Stop   CAG Q      AAG K      GAG E
TGT C      CGT R      AGT S      GGT G
TGC C      CGC R      AGC S      GGC G
TGA Stop   CGA R      AGA R      GGA G
TGG W      CGG R      AGG R      GGG G 
"""
codon = string.split()
protein = dict(zip(codon[0::2], codon[1::2]))
MOD = 1e7 
flag = False
introns =  []
temp = ""
seq = []
DNA_string = ""
for line in f1:
    if line[0] == '>':
        if (temp != ""):
            seq.append(temp)
        temp = ""   
    else:
        temp += line.strip()
if (temp != ""):
    seq.append(temp)
DNA_string = seq[0]
introns = seq[1:]
flag = True
n1 = len(DNA_string)
i = 0
#while i < len(DNA_string):
#    for j in range(i+1,len(DNA_string)):
#        if (DNA_string[i:j] in introns):
#            DNA_string = DNA_string[:i] + DNA_string[j:]
#    i+=1
for intron in introns:
    DNA_string = DNA_string.replace(intron, "")

n = len(DNA_string)
for i in range(0,n,3):
    k = DNA_string[i:i+3]
    if k in protein:
        if (protein[k] == "Stop"):
            break
        f2.write(protein[k])


   