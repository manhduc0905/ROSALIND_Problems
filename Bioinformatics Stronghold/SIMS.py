f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")
def printM(matrix, seq1, seq2):
	n = len(seq1)
	m = len(seq2)
	for i in range(n):
		if (i == 0):
			print(" ", end = " ")
			for j in range(m):
				print(seq2[j], end = " ")
			print()
		for j in range(m):
			if (j == 0):
				print(seq1[i], end = " ")
			print(matrix[i][j], end = " ")
		print()
def aligning(seq1, seq2):
    seq1 = " " + seq1
    seq2 = " " + seq2
    n = len(seq1)
    m = len(seq2)
    dp = [[0 for _ in range(m)] for _ in range(n)]
    Trace = [["" for _ in range(m)] for _ in range(n)]
    for i in range(1,n):
        Trace[i][0] = "."
    for j in range(1,m):
        dp[0][j] = dp[0][j-1] - 1
        Trace[0][j] = "."
    Trace[0][0] = "X"
    maxer = (-1,0,0)
    for i in range(1,n):
        for j in range(1,m):
            score_i_j = 1 if seq1[i] == seq2[j] else -1
            dp[i][j], Trace[i][j] = max((dp[i-1][j-1] + score_i_j, "D"),(dp[i][j-1] - 1, "L"), (dp[i-1][j] - 1, "U"))
            if (j == 0):
                dp[i][j], Trace[i][j] = max((0, "."),(dp[i][j], Trace[i][j]))
            maxer = max(maxer, (dp[i][j],i,j))
    i = maxer[1]
    j = maxer[2]
    aligned_seq1 = ""
    aligned_seq2 = ""
    while (j != 0):
        if (Trace[i][j] == 'L'):
            aligned_seq2 = seq2[j] + aligned_seq2
            aligned_seq1 = "-" + aligned_seq1
            j-=1
        elif (Trace[i][j] == 'U'):
            aligned_seq2 = "-" + aligned_seq2
            aligned_seq1 = seq1[i] + aligned_seq1
            i-=1
        else:
            aligned_seq1 = seq1[i] + aligned_seq1
            aligned_seq2 = seq2[j] + aligned_seq2
            i-=1
            j-=1
    x = maxer[1]
    y = maxer[2]
    return(dp[x][y], aligned_seq1, aligned_seq2)

D = f1.read().split(">")[1:]
seq = "".join(map(str,D[0].split("\n")[1:-1]))
motif = "".join(map(str,D[1].split("\n")[1:]))
k = len(motif)

score, seq1, seq2 = (aligning(seq, motif))
f2.write(f"{score}\n")
f2.write(seq1 + "\n")
f2.write(seq2 + "\n")
