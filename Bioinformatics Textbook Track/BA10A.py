f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")

D = f1.read().split("\n")

seq = D[0]
print(D[-3].split('\t')[1:-1])
A_prob = list(map(float,D[-3].split('\t')[1:-1]))
B_prob = list(map(float,D[-2].split('\t')[1:]))

prob_A = {
    "A":A_prob[0],
    "B":A_prob[1]
}

prob_B = {
    "A":B_prob[0],
    "B":B_prob[1]
}


n = len(seq)
cur = 0
for i in range(n):
    if (i == 0):
        cur = 0.5
    else:
        if (seq[i-1] == "A"):
            cur *= prob_A[seq[i]]
        else:
            cur *= prob_B[seq[i]]
print(cur)
