# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 17:07:35 2025

@author: Shijian
"""

# === Script: utils.py ===
# Purpose: Collection of general utility functions
# Date: April 28, 2025 (JST)
# Author: Shijian

import os
import pandas as pd

def reverse_complement(seq):
    """
    Generate the reverse complement of a DNA sequence.
    Input: 'ATGC'
    Output: 'GCAT'
    """
    complement = str.maketrans('ATCGatcg', 'TAGCtagc')
    return seq.translate(complement)[::-1]

def load_primers_from_file(filepath):
    """
    Load primer information from a file.
    Supported formats:
        - Plain txt file (one primer sequence per line, direction unknown)
        - CSV file (two columns: Direction, Sequence)
    Returns:
        primers: list of (sequence, direction) tuples
    """
    filepath_lower = filepath.lower()  # Normalize extension to lowercase

    if filepath_lower.endswith('.txt'):
        # Read plain txt
        primers = []
        with open(filepath, 'r') as fin:
            for line in fin:
                seq = line.strip()
                if seq:
                    primers.append((seq, 'unknown'))
        return primers

    elif filepath_lower.endswith('.csv'):
        # Read csv
        df = pd.read_csv(filepath)
        if 'Direction' not in df.columns or 'Sequence' not in df.columns:
            raise ValueError("CSV format error: must contain 'Direction' and 'Sequence' columns.")
        
        primers = []
        for _, row in df.iterrows():
            direction = row['Direction'].strip().lower()
            seq = row['Sequence'].strip()
            if direction not in ['forward', 'reverse']:
                raise ValueError(f"Unknown direction label: {direction}, must be 'forward' or 'reverse'.")
            primers.append((seq, direction))
        return primers
    
    else:
        raise ValueError("Unsupported file format. Must be .txt or .csv.")

def clean_sequence(seq):
    """
    Clean a DNA sequence: remove spaces, newlines, and convert to uppercase.
    """
    return seq.strip().replace(" ", "").replace("\n", "").upper()

def validate_sequence(seq):
    """
    Validate that a DNA sequence contains only A/T/C/G characters.
    """
    for char in seq.upper():
        if char not in ['A', 'T', 'C', 'G']:
            raise ValueError(f"Invalid character {char} found. Only A/T/C/G are allowed.")

def mkdir_if_not_exists(path):
    """
    Create a directory if it does not already exist.
    """
    if not os.path.exists(path):
        os.makedirs(path)
