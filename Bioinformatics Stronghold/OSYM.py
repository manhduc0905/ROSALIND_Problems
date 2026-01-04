f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")

def align(seq1, seq2):
    seq1 = " " + seq1
    seq2 = " " + seq2

    n = len(seq1)
    m = len(seq2)

    pre = [[0 for _ in range(m+1)] for _ in range(n+1)]
    suf = [[0 for _ in range(m+1)] for _ in range(n+1)]
  
    d = 1
    for i in range(1,n):
        pre[i][0] = i*(-d)
        suf[i][m] = (n - i)*(-d)
    for j in range(1,m):
        pre[0][j] = j*(-d)  
        suf[n][j] = (m - j)*(-d)

    #print(pre)
    #print(suf)
    for i in range(1,n):
        for j in range(1,m):
            score_i_j = 1 if (seq1[i] == seq2[j]) else -d
            min_align =  min_align = max(pre[i-1][j-1] + score_i_j, pre[i-1][j] - d, pre[i][j-1] -d)
            pre[i][j] = min_align

    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            score_i_j = 1 if (seq1[i] == seq2[j]) else -d
            min_align =  min_align = max(suf[i+1][j+1] + score_i_j, suf[i+1][j] - d, suf[i][j+1] -d)
            suf[i][j] = min_align
    sum = 0
    for i in range(1,n):
        for j in range(1,m):
            score_i_j = 1 if (seq1[i] == seq2[j]) else -d
            sum += pre[i-1][j-1] + suf[i+1][j+1] + score_i_j
            #print(pre[i-1][j-1] + suf[i+1][j+1] + score_i_j, end = " ")
        #print()
    f2.write(f"{(pre[n-1][m-1])}\n")
    f2.write(f"{(sum)}\n")
D = f1.read().split(">")[1:]
seq1 = "".join(map(str,D[0].split("\n")[1:-1]))
seq2 = "".join(map(str,D[1].split("\n")[1:]))

align(seq1,seq2)