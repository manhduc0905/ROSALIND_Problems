m,n,k = map(int,input().split())
sum = m+n+k
praaxaa = (n/sum) * (n-1)/(sum-1)
prAaxaa = (n/sum) * (m/(sum-1))*2*1/2
prAaxAa = (m/sum) * (m-1)/(sum-1)*1/4
praa = praaxaa + prAaxAa + prAaxaa
prAa = 1 - praa
print(prAa)