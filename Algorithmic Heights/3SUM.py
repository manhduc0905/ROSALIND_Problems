input_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\input.INP"
output_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\output.OUT"
f1 = open(input_path, 'r')
f2 = open(output_path,'w')

k,n = (map(int,f1.readline().strip().split()))

def run(a):
    mp = {}
    pos = {}
    for i in range(n):
        if (a[i]) not in pos:
            pos[a[i]] = i
    for i in range(n-1, 0, -1):
        for j in range(n-1, i, -1):
            if -(a[i] + a[j]) in pos:
                if (pos[-a[i] - a[j]] < i):
                    f2.write(f"{pos[-a[i]-a[j]] + 1} {i + 1} {j + 1}\n")
                    return
    f2.write("-1\n")
    return
for line in f1:
    a = list(map(int,line.strip().split()))
    run(a)
    



