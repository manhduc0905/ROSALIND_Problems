import math
from decimal import *
n = int(input())
getcontext().prec = 1000

D_One = Decimal(1.0)
D_Half = Decimal(0.5)
D_Mul = D_Half**(2*n)
prob = [0 for _ in range(2*n + 2)]
prob[0] = D_Mul
print(0.00, end = " ")
for i in range(1,2*n+1):
    prob[i] = Decimal(math.comb(2*n, i))*D_Mul + prob[i-1]		
    prob_at_least_i = D_One - prob[i]
    
    print(round(math.log10(prob_at_least_i),3), end=" ")