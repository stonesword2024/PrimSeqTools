# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 16:47:43 2025

@author: Shijian
"""

# === Script: primer_checker.py ===
# Purpose: Search primers and their reverse complements in genome chromosome files,
#          locate matched positions, and monitor multiple matching risks
# Date: April 28, 2025 (JST)
# Author: Shijian

import os
import pandas as pd
from scipy.io import loadmat

# Assume the utils module is properly prepared
from genome_tools.utils import reverse_complement, load_primers_from_file

def check_primers(indir, outdir, primers):
    """
    Parameters:
        indir: str, directory containing the split .mat chromosome files
        outdir: str, directory to save match results
        primers: list of (sequence, direction) tuples
                 direction can be "forward", "reverse", or "unknown"
    Function:
        Searches for each primer and its necessary reverse complement,
        records match positions, outputs results to CSV files,
        and prints multiple match warnings to the terminal.
    """
    
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    # Initialize hit counter for each primer-direction combination
    hit_counter = {}

    # Standardize primer list (assuming load_primers_from_file ensures standard structure)
    search_primers = []
    for seq, direction in primers:
        seq = seq.strip().upper()
        if direction.lower() == 'forward':
            search_primers.append((seq, 'forward'))
            hit_counter[(seq, 'forward')] = 0
        elif direction.lower() == 'reverse':
            rc_seq = reverse_complement(seq)
            search_primers.append((rc_seq, 'reverse_complement'))
            hit_counter[(rc_seq, 'reverse_complement')] = 0
        elif direction.lower() == 'unknown':
            # If direction is unknown, search both orientations
            search_primers.append((seq, 'forward'))
            search_primers.append((reverse_complement(seq), 'reverse_complement'))
            hit_counter[(seq, 'forward')] = 0
            hit_counter[(reverse_complement(seq), 'reverse_complement')] = 0
        else:
            raise ValueError(f"Unknown primer direction: {direction}")

    files = [f for f in os.listdir(indir) if f.endswith('.mat')]
    print(f"🧬 Starting search across {len(files)} chromosomes...")

    for file in files:
        data = loadmat(os.path.join(indir, file))
        chrname = str(data['chrname'][0])
        chrseq = str(data['sequence'][0])

        results = []
        for primer_seq, direction in search_primers:
            idx = chrseq.find(primer_seq)
            while idx != -1:
                results.append({
                    'Chromosome': chrname,
                    'Position': idx + 1,
                    'Primer': primer_seq,
                    'Direction': direction
                })
                hit_counter[(primer_seq, direction)] += 1
                idx = chrseq.find(primer_seq, idx + 1)

        if results:
            out_file = os.path.join(outdir, f"{chrname}_matches.csv")
            df = pd.DataFrame(results)
            df.to_csv(out_file, index=False)
            print(f"✅ Completed: {chrname:<8} | Matches: {len(results)} | Saved to: {out_file}")
        else:
            print(f"⭕ No match found: {chrname:<8} | No output file generated")

    print(f"\n🎯 All chromosome searches completed! Results saved in: {outdir}")

    # Multiple match warning
    multi_match_found = False
    print("\n⚠️ Multiple match warning:")
    for (primer_seq, direction), count in hit_counter.items():
        if count > 1:
            print(f"- Primer: {primer_seq} ({direction}) matched {count} times")
            multi_match_found = True

    if not multi_match_found:
        print("No multiple matches detected. All primers are specific.")
    
    print("🎉 primer_checker completed.")
