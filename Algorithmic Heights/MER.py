input_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\input.INP"
output_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\output.OUT"
f1 = open(input_path, 'r')
f2 = open(output_path,'w')

n = int(f1.readline().strip())
a = list(map(int,f1.readline().strip().split()))
m = int(f1.readline().strip())
b = list(map(int,f1.readline().strip().split()))

i = 0
j = 0
ans = []
while i < n and j < m:
    if (a[i] <= b[j]):
        ans.append(a[i])
        i+=1
    else:
        ans.append(b[j])
        j+=1
ans += a[i:] +  b[j:]
f2.write(" ".join(map(str,ans)))