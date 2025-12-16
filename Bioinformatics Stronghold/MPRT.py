import urllib.request
f1 = open('input.INP','r')
f2 = open('output.OUT','w')
d = {}
ans = {}
def getData(id):
    url = f"http://www.uniprot.org/uniprot/{id}.fasta"
    data = urllib.request.urlopen(url)
    #print("https://rest.uniprot.org/uniprotkb/{id}.fasta")
    protein_seq = ""
    for line in data:
        line = line.decode('utf-8').strip()
        if not line[0] == '>': 
            protein_seq += line.strip()
    return protein_seq

def N_glyco(s):
    return (s[0] == 'N') and (s[1] != 'P') and (s[2] == 'T' or s[2] == 'S') and (s[3] != 'P')

for line in f1:
    key = line[:6]
    d[line.strip()] = getData(key)

for key,seq in d.items():
    n = len(seq)
    ans[key] = []
    for i in range (0,n):
        if (seq[i] == 'N'):
            if (N_glyco(seq[i:i+4])):
                ans[key].append(i+1)

for key,val in ans.items():
    if (len(val) >= 1):
        f2.write(key + "\n")
        f2.write(" ".join(map(str, val)))
        f2.write("\n")


        
          
