input_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\input.INP"
output_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\output.OUT"
f1 = open(input_path, 'r')
f2 = open(output_path,'w')

n = int(f1.readline().strip())
a = list(map(int, f1.readline().strip().split()))

pre = []
suf = []
mid = [a[0]]
for i in range(1,n):
    if (a[i] < a[0]):
        pre.append(a[i])
    elif (a[i] == a[0]):
        mid.append(a[i])
    else:
        suf.append(a[i])
ans = pre + mid + suf
f2.write(" ".join(map(str,ans)))