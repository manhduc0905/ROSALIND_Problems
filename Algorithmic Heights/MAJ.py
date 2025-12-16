input_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\input.INP"
output_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\output.OUT"
f1 = open(input_path, 'r')
f2 = open(output_path,'w')

k,n = map(int,f1.readline().strip().split())

for line in f1:
    a = list(map(int, line.strip().split()))
    mapp = {}
    occ = -1
    ans = -1
    for j in range(n):
        if a[j] not in mapp:
            mapp[a[j]] = 0
        mapp[a[j]] += 1
        if occ < mapp[a[j]]:
            occ = mapp[a[j]]
            ans = a[j]
    if (occ > n//2):
        f2.write(f"{ans} ")
    else: 
        f2.write(f"{-1} ")
