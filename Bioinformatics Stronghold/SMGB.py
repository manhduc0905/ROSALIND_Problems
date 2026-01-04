f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")

D = f1.read().split(">")[1:]
seq = "".join(map(str,D[0].split("\n")[1:-1]))
motif = "".join(map(str,D[1].split("\n")[1:]))
k = len(motif)      

def align(seq1, seq2):
    seq1 = " " + seq1
    seq2 = " " + seq2

    n = len(seq1)
    m = len(seq2)

    L = [[0 for _ in range(m)] for _ in range(n)]
    Trace = [["" for _ in range(m)] for _ in range(n)]
    #printM(L,seq1,seq2)
    #Needleman-Wunsch
    d = 1
    for i in range(1,n):
        Trace[i][0] = "U"
    for j in range(1,m):
        L[0][j] = L[0][j-1] -d
        Trace[0][j] = "L"

    Trace[0][0] = "X"


    for i in range(1,n):
        for j in range(1,m):
            score_i_j = 1 if (seq1[i] == seq2[j]) else -d
    
            if (j == m-1):
                min_align = max((L[i-1][j], "U"), (L[i-1][j-1] + score_i_j, "D"), (L[i-1][j] - d, "U"), (L[i][j-1] -d, "L"))
            else:
                min_align = max((L[i-1][j-1] + score_i_j, "D"), (L[i-1][j] - d, "U"), (L[i][j-1] -d, "L"))
            L[i][j],Trace[i][j] = min_align	
    i = n-1
    j = m-1
    aligned_seq1 = ""
    aligned_seq2 = ""
    while (i != 0) and (j!=0):
        if (Trace[i][j] == 'L'):
            aligned_seq1 = "-" + aligned_seq1
            aligned_seq2 = seq2[j] + aligned_seq2
            j-=1
        elif (Trace[i][j] == 'U'):
            aligned_seq1 = seq1[i] + aligned_seq1
            aligned_seq2 = "-" + aligned_seq2
            i-=1
        else:
            aligned_seq1 = seq1[i] + aligned_seq1
            aligned_seq2 = seq2[j] + aligned_seq2
            i-=1
            j-=1
    while (i != 0):
        aligned_seq1 = seq1[i] + aligned_seq1
        aligned_seq2 = "-" + aligned_seq2
        i-=1
    ans = []
    ans.append(L[n-1][m-1])
    ans.append(aligned_seq1)
    ans.append(aligned_seq2)
    return ans
if (len(seq) < len(motif)):
    seq,motif = motif,seq
f2.write("\n".join(map(str,align(seq, motif))))