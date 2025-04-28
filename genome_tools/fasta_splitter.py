# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 16:29:33 2025

@author: Shijian
"""

# === Script: fasta_splitter.py ===
# Purpose: Extract each chromosome or scaffold sequence from a large FASTA file
#          and save them individually as .mat files (without skipping any)
# Date: April 28, 2025 (JST)
# Author: Shijian

import os
from scipy.io import savemat

def split_fasta_to_mat(input_fasta, output_dir):
    """
    Parameters:
        input_fasta: str, path to the large FASTA file
        output_dir: str, directory to save the output .mat files
    Function:
        Extracts each chromosome or scaffold from the FASTA file
        and saves them individually as .mat files.
    """

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_fasta, 'r') as f:
        chrname = ''
        seq_lines = []
        line_counter = 0

        for line in f:
            line = line.strip()
            line_counter += 1

            if line.startswith('>'):
                # Save the accumulated sequence if any
                if seq_lines:
                    sequence = ''.join(seq_lines).upper()
                    savemat(os.path.join(output_dir, f"{chrname}.mat"), 
                            {'chrname': chrname, 'sequence': sequence})
                    print(f"✅ Saved: {chrname} (Length: {len(sequence):,})")

                chrname = line[1:].strip()  # Remove ">" at the beginning
                seq_lines = []
            else:
                seq_lines.append(line)

            # Progress notification
            if line_counter % 50000 == 0:
                print(f"📄 Read {line_counter:,} lines...")

        # Handle the last sequence
        if seq_lines:
            sequence = ''.join(seq_lines).upper()
            savemat(os.path.join(output_dir, f"{chrname}.mat"), 
                    {'chrname': chrname, 'sequence': sequence})
            print(f"✅ Saved: {chrname} (Length: {len(sequence):,})")

    print(f"🎉 All sequences have been processed. Files saved in: {output_dir}")
