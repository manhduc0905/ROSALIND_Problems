#!/usr/bin/env/python
from itertools import product
f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")
k, d = map(int, f1.readline().strip().split())
seqs = [s for s in f1.read().split('\n') if s]  
nu = ["A", "C", "G", "T"]   
all_kmer = [''.join(p) for p in product(nu, repeat=k)]
n = len(seqs[0])
final = set()
eliminated = set()
def hamming(seq1, seq2):
    #print(seq1,seq2)
    cnt = 0
    for idx, base in enumerate(seq1):
        if (seq2[idx] != base):
            cnt +=1
    return cnt

def check(kmer, d):
    flag = [False]*len(seqs)
    for idx,seq in enumerate(seqs):
        for i in range(n - k + 1):
            if (hamming(kmer, seq[i:i+k]) <= d):
                flag[idx] = True
                break
    return all(flag)
        
def motif_enumeration(seq, k, d):
    global final, eliminated
    for i in range(n - k + 1):  
        cur_kmer = seq[i:i+k]
        for _kmer in all_kmer: 
            if (_kmer in final or _kmer in eliminated): 
                continue
            elif (hamming(_kmer, cur_kmer) <= d):
                if (check(_kmer, d)):
                    final.add(_kmer)
                else:
                    eliminated.add(_kmer)
    return final
for seq in seqs:
    final = motif_enumeration(seq, k , d)
f2.write(" ".join(map(str,final)))



