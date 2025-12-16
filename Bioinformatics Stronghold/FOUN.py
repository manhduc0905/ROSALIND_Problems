import math
f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")

n, m = map(int, f1.readline().strip().split())
a = list(map(int, f1.readline().strip().split()))
k = len(a)
total = 2*n
cur_gen = [[0.0 for _ in range(total+1)] for _ in range(k)]


for i in range(k):
        cur_gen[i][a[i]] = 1.0
print(cur_gen)
for gen in range(m):
    new_gen = [[0.0 for _ in range(total+1)] for _ in range(k)]
    for j in range(k):
        for allele in range(2*n+1):
            p = allele/total
            if (cur_gen[j][allele] == 0): continue
            for cur in range(2*n+1):
                #print(cur)
                p1 = math.comb(total, cur)*(p**(cur))*((1-p)**(total-cur))
                #print(cur_gen[j][allele], p1)
                new_gen[j][cur] += cur_gen[j][allele]*p1
    cur_gen = new_gen
    for j in range(k):
        #print(gen)
            if (cur_gen[j][0]):
                f2.write(f"{math.log10(cur_gen[j][0])} ")
            else:
                f2.write("0.0 ")
    f2.write("\n")

#print(prob_gen)
#print(cur_gen)

