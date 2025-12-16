import math
import itertools

input_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
output_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\output.OUT"
f1 = open(input_path, 'r')
f2 = open(output_path,'w')

taxa = f1.readline().strip().split()

n = len(taxa)

def get_choose(taxon):
    pinned = taxon[-1]
    others = taxon[:-1]

    groups = []
    m = len(taxon)
    for length in range(1, m):
        for j in itertools.combinations(others, length):
            left_list = list(j)
            #print(j, left_list)
            right_list = [x for x in others if x not in left_list] + [pinned]
            
            groups.append((left_list,right_list))
    #print(groups)
    return groups


def build_tree(taxon):
    m = len(taxon)
    if (m == 1):
        return [taxon[0]]
    if (m == 2):
        return [f"({taxon[0],taxon[1]})"]
    
    all_trees = []
    splits = get_choose(taxon)

    for left, right in splits:
        left_options = build_tree(left)
        right_options = build_tree(right)

        for l in left_options:
            for r in right_options:
                new_tree = f"({l},{r})"
                all_trees.append(new_tree)

    return all_trees
total = build_tree(taxa[1:])
for x in total:
    printer = str(x).replace("'", "")
    f2.write(f"({printer}){taxa[0]};\n")