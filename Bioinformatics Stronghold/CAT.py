import sys
sys.setrecursionlimit(2000)
input_path = input_path = r"C:\Users\admin\OneDrive - Grinnell College\Documents\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
f1 = open(input_path,'r')
f2 = open('output.OUT','w')
rna = ""
for line in f1:
    if not line.startswith('>'): 
        rna += line.strip() 
def revcomp(s):
    return s.translate(str.maketrans('ACUG','UGAC'))[::-1]

n = len(rna)
pair = {'A':'U', 'U':'A', 'C':'G', 'G':'C'}
mod = 1000000
#approach 1
dp ={}
def count(i,j):
    if (i >= j):
        return 1
    if (i,j) in dp: 
        return dp[(i,j)]%mod

    sum = 0
    for k in range(i+1,j+1,2):
        if (rna[k] == pair[rna[i]]):
            sum = (sum + (count(i+1,k-1)*count(k+1,j))%mod)%mod
    dp[(i,j)] = sum % mod
    return dp[(i,j)]

def count2(i,j):
    dp = [[0] * (n+1) for _ in range(n+1)]
    #empty match has length = 1
    for i in range(n):
        for j in range(i):
            if (j - i + 1) == 0:
                dp[i][j] = 1

    for length in range(0, n + 1, 2):  
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i + 1, j + 1, 2):  
                if rna[i] == pair[rna[k]]:
                    left = 1 if k - 1 < i + 1 else dp[i + 1][k - 1]
                    right = 1 if j < k + 1 else dp[k + 1][j]

                    dp[i][j] = (dp[i][j] + left * right) % mod

    return dp[i][j]

answer = str(count(0,n-1))
f2.write(answer)
