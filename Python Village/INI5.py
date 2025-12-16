f1 = open('rosalind_ini5.txt', 'r')
f2 = open('output.txt', 'w')
i = 0
for line in f1:
    if (i % 2 == 1):
          f2.write(line)
    i+=1
f1.close()
f2.close()