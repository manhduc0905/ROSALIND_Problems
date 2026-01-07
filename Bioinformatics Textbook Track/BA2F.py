#!/usr/bin/env/python
f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")
import numpy as np

k, t = map(int, f1.readline().strip().split())
sequences = [s for s in f1.read().split('\n') if s]
nu = ["A", "C", "G", "T"]
seq_len = len(sequences[0])
kmer_set = {idx: [] for idx in range(t)}

for idx, seq in enumerate(sequences):
    for i in range(seq_len - k + 1):
        kmer_set[idx].append(seq[i:i+k])

def hamming(seq1, seq2):
    cnt = 0
    for idx, base in enumerate(seq1):       
        if (seq2[idx] != base):
            cnt +=1
    return cnt

def form_profile(motifs):
    profile = {base:[1.0]*k for base in nu}
    for motif in motifs:
        for idx, base in enumerate(motif):
            profile[base][idx] += 1

    for base in nu:
        for i in range(k):
            profile[base][i] = profile[base][i] / (len(motifs)+4.0)

    return profile  

def cal_prob(profile, seq):
    prob = 1
    for idx, base in enumerate(seq):
        prob *= profile[base][idx]
    return prob

def find_best_kmer(profile, seq):
    best_kmer = (-1, "")
    #print(profile, seq)
    for i in range(seq_len - k + 1):
        new_prob = cal_prob(profile, seq[i:i+k])
        if (best_kmer[0] < new_prob):
            best_kmer = (new_prob, seq[i:i+k])
        #print((cal_prob(profile, seq[i:i+k]), seq[i:i+k]))
    return best_kmer[1]

def score(motifs):
    consensus_seq = ""
    counts = {base:[0]*k for base in nu}
    for motif in motifs:
        for idx, base in enumerate(motif):
            counts[base][idx] += 1
    for i in range(k):
        max_count = -1
        max_base = ""
        for base in nu:
            if counts[base][i] > max_count:
                max_count = counts[base][i]
                max_base = base
        consensus_seq += max_base
    #print(consensus_seq)
    cal = 0
    for motif in motifs:
        #print(cal, motif, consensus_seq)
        cal += hamming(motif, consensus_seq)
    return cal

def gen_motif(profile):
    new_motifs = []
    for i in range(t):
        new_motifs.append(find_best_kmer(profile, sequences[i]))
    return new_motifs

def randomized_search():
    global_best = (float('inf'), "")
    for i in range(1000):
        motifs = []
        for i in range(t):
            rand = np.random.randint(0, seq_len - k + 1)
            motifs.append(kmer_set[i][rand])
            best_motifs = (score(motifs), motifs)
        while 1:
            profile = form_profile(motifs)
            motifs = gen_motif(profile)
            new_score = score(motifs)
            if (best_motifs[0] > new_score):
                best_motifs = (new_score, motifs)
            else:
                break
        if (global_best[0] > best_motifs[0]):
            global_best = best_motifs
    return global_best
f2.write('\n'.join(randomized_search()[1]))