f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")

D = f1.read().split("\n")[:-1]

trans = D[0]
seq = D[4]
A_prob = list(map(float,D[-2].split('\t')[1:-1]))
B_prob = list(map(float,D[-1].split('\t')[1:]))
print(B_prob)
prob_A = {
    "x":A_prob[0],
    "y":A_prob[1],
    "z":A_prob[2]
}

prob_B = {
    "x":B_prob[0],
    "y":B_prob[1],
    "z":B_prob[2]
}

n = len(seq)
cur = 1
for i in range(n):
    if (seq[i] == "A"):
        cur *= prob_A[trans[i]]
    else:
        cur *= prob_B[trans[i]]
print(cur)

