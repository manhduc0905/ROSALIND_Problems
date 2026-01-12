#!/usr/bin/env/python
import os
import numpy as np
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "dors_seqs.txt")

class Sequences:
    def __init__(self, seqs):
        self.seqs = seqs
        self.number_seqs = len(seqs)
        self.seq_len = len(seqs[0])
        self.nu = ["A", "G", "C", "T"]

    def build_kmer_sets(self, k):
        self.kmer_sets = {}
        for i, seq in enumerate(self.seqs):
            self.kmer_sets[i] = [
                seq[j:j+k] for j in range(self.seq_len - k + 1)
            ]
    def hamming(self, seq1, seq2):
        return sum(a != b for a,b in zip(seq1, seq2))
    
    def consensus_seq(self, motifs, k):
        css_seq = ""
        counts = {base:[0]*k for base in self.nu}

        for motif in motifs:
            for idx, base in enumerate(motif):
                counts[base][idx] += 1
            
        for i in range(k):
            max_count = -1
            max_base = ""
            for base in self.nu:
                if counts[base][i] > max_count:
                    max_count = counts[base][i]
                    max_base = base
            css_seq += max_base
        return css_seq

    def score(self, motifs, k):
        consensus_seq = self.consensus_seq(motifs, k)
        return sum(self.hamming(motif, consensus_seq) for motif in motifs)
        
    def form_profile(self, motifs, k, eliminate = None):
        profile = {base:[1.0]*k for base in self.nu}
        minus = 0 if eliminate == None else 1
        for id, motif in enumerate(motifs):
            if (id == eliminate): continue
            for idx, base in enumerate(motif):  
                profile[base][idx] += 1

        for base in self.nu:
            for i in range(k):
                profile[base][i] = profile[base][i] / (len(motifs) + 4.0 - minus)

        return profile 
    
    def cal_prob(self, profile, seq):
        prob = 1
        for idx, base in enumerate(seq):
            prob *= profile[base][idx]
        return prob

    def gibbs_random_kmer(self, profile, i):
        probs = np.array([self.cal_prob(profile, seq) for seq in self.kmer_sets[i]])
        if probs.sum() == 0:
            idx = np.random.randint(0, len(probs))
        else:   
            probs = probs / probs.sum()
            idx = np.random.choice(len(probs), p= probs)
        return self.kmer_sets[i][idx]

    def GibbsSampler_MotifSearch(self, k, N_loops = 1000, N_starts = 20):
        self.build_kmer_sets(k)
        global_best = (float('inf'), "")
        for _ in range(N_starts):
            motifs = []
            for seq in self.seqs:
                r = np.random.randint(0, self.seq_len - k + 1)
                motifs.append(seq[r:r+k])

            best_motifs = (self.score(motifs, k), motifs)

            for _ in range(N_loops):
                i = np.random.randint(self.number_seqs)
                profile = self.form_profile(motifs, k, eliminate=i)
                motifs[i] = self.gibbs_random_kmer(profile, i)
                new_score = self.score(motifs, k)
                if (best_motifs[0] > new_score):
                    best_motifs = (new_score, motifs)
            if (global_best[0] > best_motifs[0]):
                global_best = best_motifs
        return global_best
    
    def output(self, k, time, out_file="search_results.html"): 
            out_file = f"search_results_try{time}.html"
            out_file = os.path.join(script_dir, out_file) 
            score, motifs = self.GibbsSampler_MotifSearch(k)
            css_seq = self.consensus_seq(motifs, k)

            RED_START = "<span style='color: #ff5555; font-weight: bold;'>" # Red for matches
            GREEN_START = "<span style='color: #50fa7b;'>" # Green for mutations
            CLOSE_TAG = "</span>"

            with open(out_file, "w") as f:
                f.write("<html><body style='background-color: #282a36; color: #f8f8f2; font-family: monospace;'>\n")
                f.write("<pre>\n")

                f.write("# Gibbs Sampler Motif Search Results\n")
                f.write(f"# k = {k}\n")
                f.write(f"# number of sequences = {self.number_seqs}\n")
                f.write(f"# best score = {score}\n\n")

                f.write("Consensus:\n")
                f.write(css_seq + "\n\n")

                f.write("Motifs:\n")
                for i, motif in enumerate(motifs):
                    f.write(f"Seq{i+1}\t{motif}\n")
                
                f.write("\nPutative occurrences:\n")
                for idx, seq in enumerate(self.seqs):
                    f.write(f"Seq{idx+1}\t")
                    i = 0
                    while i < self.seq_len:
                        if (i + k <= self.seq_len and motifs[idx] == seq[i:i+k]):
                            for j, base in enumerate(seq[i:i+k]):
                                if (base == css_seq[j]):
                                    f.write(f"{RED_START}{base.upper()}{CLOSE_TAG}")
                                else:
                                    f.write(f"{GREEN_START}{base.lower()}{CLOSE_TAG}")
                            i += k
                        else:    
                            f.write(seq[i].lower())
                            i += 1
                    f.write('\n')
                f.write("</pre></body></html>")


with open(file_path, "r") as f:
    seqs = f.read().split('\n')

seqs = Sequences(seqs)
for i in range(10):
    seqs.output(k = 20, time=i+1)
