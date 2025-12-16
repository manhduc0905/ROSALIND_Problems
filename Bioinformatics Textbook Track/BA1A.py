f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")

seq1 = f1.readline().strip()
seq2 = f1.readline().strip()

n = len(seq2)
cnt = 0
for i in range(len(seq1)):
    if (i + n <= len(seq1)):
        if (seq1[i: i + n] == seq2):
            cnt += 1
print(cnt)