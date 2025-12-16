input_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\input.INP"
output_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\output.OUT"
f1 = open(input_path, 'r')
f2 = open(output_path,'w')

n = int(f1.readline().strip())
a = list(map(int, f1.readline().strip().split()))
cnt = 0
for i in range(1,n):
    j = i
    while j > 0 and a[j-1] > a[j]:
        a[j-1],a[j] = a[j], a[j-1]
        j = j-1
        cnt += 1
f2.write(f"{cnt}")