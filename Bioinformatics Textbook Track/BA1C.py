f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")

seq = f1.readline().strip()
revseq = seq.translate(seq.maketrans("ATCG", "TAGC"))[::-1]
f2.write(revseq)