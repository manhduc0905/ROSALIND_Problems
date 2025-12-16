import sys
input_path = input_path = r"C:\Users\admin\OneDrive - Grinnell College\Documents\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
f1 = open(input_path, 'r')
seq = []
for line in f1:
	line = line.strip()
	seq.append(line)

n = len(seq)
m = len(seq[0])

for i in range(m):
	res = ""
	count = {}
	tot_count = 0
	cal = 0
	for j in range(n):
		#print(seq[j][i])
		if (seq[j][i] not in count):
			count[seq[j][i]] = tot_count
			tot_count+=1
		if (tot_count >= 3):
			break
		res += f"{count[seq[j][i]]}"
		cal += count[seq[j][i]]
		#print(cal,n)
	if (tot_count == 2 and cal != 1 and cal != n - 1):
		print(res)