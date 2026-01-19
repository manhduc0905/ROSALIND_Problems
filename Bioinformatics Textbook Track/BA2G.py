#!/usr/bin/env/python
f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")
import numpy as np
import random
from collections import Counter
k, t, N = map(int, f1.readline().strip().split())
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

def form_profile(motifs, eliminate = None):
    profile = {base:[1.0]*k for base in nu}
    if (eliminate != None):
        minus = 1
    for id, motif in enumerate(motifs):
        if (id == eliminate): continue
        for idx, base in enumerate(motif):
            profile[base][idx] += 1

    for base in nu:
        for i in range(k):
            profile[base][i] = profile[base][i] / (len(motifs) + 4.0 - minus)

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

def random(probs):
    total = sum(probs)
    if total == 0:
        return random.randint(0, len(probs)-1)
    
    normalized = [p/ total for p in probs]
    cum_probs = []
    cum_sum = 0
    for p in normalized:
        cum_sum += p
        cum_probs.append(cum_sum)
    r = random.random()
    for idx, cp in enumerate(cum_probs):
        if (r < cp):
            return idx
    
    return len(probs) - 1

def gibbs_random_kmer(profile, i):
    probs = np.array([cal_prob(profile, seq) for seq in kmer_set[i]])
    if probs.sum() == 0:
        idx = np.random.randint(0, len(probs))
    else:
        probs = probs / probs.sum()
        idx = np.random.choice(len(probs), p= probs)
    return kmer_set[i][idx]

def GibbsSampler_search(N = 1000, N_GLOB = 20):
    global_best = (float('inf'), "")
    for i in range(N_GLOB):
        motifs = []
        for i in range(t):
            rand = np.random.randint(seq_len - k + 1)
            motifs.append(kmer_set[i][rand])
            best_motifs = (score(motifs), motifs)
        for _ in range(N):
            i = np.random.randint(t)
            profile = form_profile(motifs, eliminate=i)
            motifs[i] = gibbs_random_kmer(profile, i)
            new_score = score(motifs)
            if (best_motifs[0] > new_score):
                best_motifs = (new_score, motifs)
        if (global_best[0] > best_motifs[0]):
            global_best = best_motifs
    return global_best

def consensus_string(motifs):
    if not motifs:
        return ""
    
    motif_length = len(motifs[0])
    consensus = []

    for i in range(motif_length):
        column = [motif[i] for motif in motifs]
        most_common_nucleotide, _ = Counter(column).most_common(1)[0]
        consensus.append(most_common_nucleotide)
    
    return ''.join(consensus)
final_motifs_set = GibbsSampler_search(N, N_GLOB = 100)[1]
#print(consensus_string(final_motifs_set))
f2.write('\n'.join(final_motifs_set))