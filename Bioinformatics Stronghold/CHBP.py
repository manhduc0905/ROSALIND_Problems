input_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
output_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\output.OUT"
f1 = open(input_path, 'r')
f2 = open(output_path,'w')

name = f1.readline().strip().split()
table = []
depth = {}
cur_depth = 0
for line in f1:
    line = line.strip()
    x = line.count('1')
    y = line.count('0')
    if (x <= 1 or y <= 1):
        continue
    if (x > y):
        line = line.translate(str.maketrans("01","10"))
    table.append(line)
print(table)
table.sort(key=lambda x: x.count('1'), reverse=True)
used_rows = [False] * len(table)
name_ind = {n:i for i,n in enumerate(name)}
n = len(table)
m = len(name)

def build_tree(cur_taxa):
    if len(cur_taxa) == 1:
        return cur_taxa[0]
    for i in range(len(table)):
        if (used_rows[i]):
            continue
        rows = table[i]
        print(cur_taxa, rows)
        group_0 = []
        group_1 = []
        for taxon in cur_taxa:
            ind = name_ind[taxon]
            if (rows[ind] == "0"):
                group_0.append(taxon)
            else:
                group_1.append(taxon)
        j = len(group_0)
        k = len(group_1)
        if j > 0 and k > 0:
            if (j + k == len(cur_taxa)):
                used_rows[i] = True
                return f"({build_tree(group_0)},{build_tree(group_1)})"
    return "(" + ",".join(cur_taxa) + ")"
  

ans = build_tree(name)
f2.write(ans + ";")

