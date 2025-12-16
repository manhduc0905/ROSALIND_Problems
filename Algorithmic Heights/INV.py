input_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\input.INP"
output_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Algorithmic Heights\output.OUT"
f1 = open(input_path, 'r')
f2 = open(output_path,'w')
cnt = 0
def merge(a, l, m , r):
    global cnt
    n1 = m - l + 1
    #print(a,l,m,r, n1)
    n2 = r - m
    L = [0]*(n1)
    R = [0]*(n2)
    for i in range(n1):
        L[i] = a[l + i]
    for j in range(n2):
        R[j] = a[m + j + 1]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if (L[i] <= R[j]):
            a[k] = L[i]
            i+=1
        else:
            a[k] = R[j]
            cnt += (len(L) - i)
            j+=1
        k+=1

    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1

def ms(a,l,r):
    if l < r:
        m = l + (r - l)//2
        ms(a,l,m)
        ms(a, m+1,r)
        merge(a, l, m , r)
    
n = int(f1.readline())
a = list(map(int, f1.readline().strip().split()))
ms(a, 0, n-1)
f2.write(f"{cnt}")
