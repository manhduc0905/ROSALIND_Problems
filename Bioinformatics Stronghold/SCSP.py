from collections import deque

input_path = input_path = r"C:\Users\admin\OneDrive - Grinnell College\Documents\College\Coding\Bioinformatics Learning\input.INP"
#print(input_path)
#f1 = open(input_path,'r')
#f2 = open('output.OUT','w')

seq1 = input()
seq2 = input()

seq1 = " " + seq1
seq2 = " " + seq2

n = len(seq1)
m = len(seq2)

dp = [[0 for _ in range(m)] for _ in range(n)]
Trace = [[0 for _ in range(m)] for _ in range(n)]
dp[1][1] = 0 if seq1[0] == seq2[0] else 2

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
Trace[0][0] = "X"
for i in range(1,n):
	dp[i][0] = i
	Trace[i][0] = "U"
for j in range(1,m):
	dp[0][j] = j
	Trace[0][j] = "L"
	
for i in range(1,n):
	for j in range(1,m):
		if (seq1[i] == seq2[j]):
			dp[i][j] = dp[i-1][j-1]+1
			Trace[i][j] = "D"
		else:
			min_1 = min(dp[i-1][j], dp[i][j-1])
			dp[i][j], Trace[i][j] = min((dp[i-1][j] + 1, "U"), (dp[i][j-1] + 1, "L"))
			
#printM(Trace, seq1, seq2)
#print(dp[n-1][m-1])
i = n-1
j = m-1

ans_seq = ""
while (Trace[i][j] != "X"):
	if (Trace[i][j] == "L"):
		ans_seq = seq2[j] + ans_seq
		j-=1
	elif (Trace[i][j] == "U"):
		ans_seq = seq1[i] + ans_seq
		i-=1
	else:
		ans_seq = seq1[i] + ans_seq
		i-=1
		j-=1
print(ans_seq)



