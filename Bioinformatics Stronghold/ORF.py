f1 = open('input.INP','r')
f2 = open('output.OUT','w')
table = """TTT F      CTT L      ATT I      GTT V
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
TGG W      CGG R      AGG R      GGG G """
codons = table.split()
n = len(codons)
d = dict(zip(codons[0::2], codons[1::2]))
s = ""
for line in f1:
    if not line[0] == '>':
        s += line.strip()
n1 = len(s)

def protein(s):
    i = 0
    num = 0
    ans = []
    while i < n1-2:
        cod = s[i:i+3]
        if cod in d and d[cod] == 'M':
            num+=1
            s1 = ""
            j = i
            flag = False
            while j < n1-2 :
                curr = s[j:j+3]
                if curr not in d:
                    break
                if d[curr] == "Stop":
                    flag = True
                    break
                s1 += d[curr]
                j+=3
            if flag:
                ans.append(s1)
        i+=1
    return(ans)
rev = {}
rev['A'] = 'T'
rev['T'] = 'A'
rev['C'] = 'G'
rev['G'] = 'C'
def other_strand(s):
    s1 = s[::-1]
    res =""
    for i in range (0, len(s1)):
        c = rev[s1[i]]
        res += c
    return res

ans = set()
b1 = protein(s)
b2 = protein(other_strand(s))
for c in b2:
    ans.add(c)
for c in b1:
    ans.add(c)
for c in ans:
    print(c)
    f2.write(c + '\n')

    
