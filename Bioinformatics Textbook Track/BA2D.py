#!/usr/bin/env/python
f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")

k, t = map(int, f1.readline().strip().split())
sequences = [s for s in f1.read().split('\n') if s]
nu = ["A", "C", "G", "T"]
seq_len = len(sequences[0])

def hamming(seq1, seq2):
    cnt = 0
    for idx, base in enumerate(seq1):       
        if (seq2[idx] != base):
            cnt +=1
    return cnt

def form_profile(motifs):
    profile = {base:[0.0]*k for base in nu}
    for motif in motifs:
        for idx, base in enumerate(motif):
            profile[base][idx] += 1

    for base in nu:
        for i in range(k):
            profile[base][i] = profile[base][i] / (len(motifs)+0.0)

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

def greedy_search():
    starting_motifs = [seq[:k] for seq in sequences]
    best_motif = (score(starting_motifs), starting_motifs)
    for i in range(seq_len - k + 1):
        motif1 = sequences[0][i:i+k]    
        current_motifs = [motif1]
        for j in range(1, len(sequences)):
            profile = form_profile(current_motifs)
            next_kmer = find_best_kmer(profile, sequences[j])
            current_motifs.append(next_kmer)
        new_score = score(current_motifs)
        if (best_motif[0] > new_score):
            best_motif = (new_score, current_motifs[:])
        #print(new_score, current_motifs)
    return best_motif
f2.write('\n'.join(greedy_search()[1]))