from Bio.Seq import translate, CodonTable, Seq
f1 = open("input.INP", "r")
D = f1.read().split("\n")
seq1 = D[0].strip()
protein = D[1].strip()
#print(protein)
dna_forward = Seq(seq1)
candidates = [dna_forward]
table_ids = CodonTable.ambiguous_generic_by_id.keys()
for dna in candidates:
    for i in table_ids:
        try:
            pro_new = dna.translate(table=i, stop_symbol="")
            if (str(pro_new) == protein):
                #print(protein[:len(pro_new)])
                print(i)
                break
        except ValueError:
            continue