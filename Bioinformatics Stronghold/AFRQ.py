a = list(map(float, input().split()))

for q_geno in a:
	p_allele = 1-(q_geno)**(1/2)
	prob = 1 - p_allele**2
	print(round(prob,3), end = " ")