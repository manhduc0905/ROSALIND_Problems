f1 = open('input.INP','r')
f2 = open('output.OUT','w')
seq = []
temp = ""
for line in f1:
    if line[0] == '>':
        if (temp != ""):
            seq.append(temp)
        temp = ""   
    else:
        temp += line.strip()
if (temp != ""):
    seq.append(temp)

seq1 = " " + seq[0]
seq2 = " " + seq[1]   

n = len(seq1)
m = len(seq2)
dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(1,n):
    for j in range(1,m):
        if (seq1[i] == seq2[j]):
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            if dp[i-1][j] < dp[i][j-1]:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = dp[i-1][j]

ans_seq = ""
print(dp[n-1][m-1])

i = n-1
j = m-1
while i> 0 and j >0:
    if (seq1[i] == seq2[j]):
        ans_seq = seq1[i] + ans_seq
        i-=1
        j-=1
    elif (dp[i-1][j] > dp[i][j-1]):
        i-=1
    else:
        j-=1
f2.write(ans_seq)




