import math
f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")
n,m,g,k = (map(int,f1.readline().split()))
print(n,m,g,k)
al = 2*n
current_probs = [0.0] * (al + 1)
current_probs[m] = 1.0
for gen in range(1,g+1):
    next_probs = [0.0]*(al + 1)
    for j in range(al + 1):
        if (current_probs[j] == 0): continue
        p = j/al
        for x in range(al + 1):
            next_probs[x] += current_probs[j]*math.comb(al,x)*(p**x)*((1-p)**(al - x))
    current_probs = next_probs

ans = sum(current_probs[:al - k + 1])
print(ans)
    

