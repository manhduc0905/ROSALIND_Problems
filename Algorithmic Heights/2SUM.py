input_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\input.INP"
output_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\output.OUT"
f1 = open(input_path, 'r')
f2 = open(output_path,'w')

k,n = map(int,f1.readline().strip().split())

for line in f1:
    a = list(map(int,line.strip().split()))
    mp = {}
    flag = True
    for i in range(n):
        if (-a[i]) in mp:
            f2.write(f"{mp[-a[i]]} {i+1}\n")
            flag = False
            break
        if a[i] not in mp:
            mp[a[i]] = i + 1
    if (flag):
        f2.write(f"-1\n")