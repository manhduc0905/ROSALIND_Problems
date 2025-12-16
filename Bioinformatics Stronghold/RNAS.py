input_path = input_path = r"C:\Users\admin\OneDrive - Grinnell College\Documents\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
#print(input_path)
f1 = open(input_path,'r')
f2 = open('output.OUT','w')
rna = ""
pair = {
    'A':'U',
    'U':'AG',
    'C':'G',
    'G':'CU'
}
MOD =  1000000


for line in f1:
    if (line.startswith(">")):
        continue
    rna += line.strip()

n = len(rna)
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
        for j in range(i):
            if (j - i + 1) == 0:
                dp[i][j] = 1

for length in range(0,n+1):
    for i in range(0,n - length + 1):
        j = i + length - 1
        #print(i,j)
        for k in range(i+4, j+1):
            if (rna[i] in pair[rna[k]]):
                dp[i][j] = (dp[i][j] + dp[i + 1][k - 1]*dp[k + 1][j])
        remain = 1 if (i+1 > n) else dp[i+1][j]
        dp[i][j] = (dp[i][j] + remain)
        
print(dp[0][n-1])
                
    