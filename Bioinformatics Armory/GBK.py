from Bio import Entrez
name = input()
Entrez.email = 'anonymous@example.org'
time1 = input()
time2 = input()
search = f'"{name}"[Organism] AND "{time1}":"{time2}"[PDAT]'
handle = Entrez.esearch(db = "nucleotide",term= search )
record = Entrez.read(handle)
print(record["Count"])