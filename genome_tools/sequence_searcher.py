# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 17:14:28 2025

@author: Shijian
"""

# === Script: sequence_searcher.py ===
# Purpose: Search large DNA fragments across genome split .mat chromosome files and output results as CSV
# Date: April 28, 2025 (JST)
# Author: Shijian

import os
import pandas as pd
from scipy.io import loadmat
import tkinter as tk
from tkinter import simpledialog, filedialog, messagebox

def search_sequence_across_genome(mat_dir, output_folder, query_seq, min_len=50, max_len=5000):
    """
    Search for a large DNA fragment in the specified genome .mat files.
    Parameters:
        mat_dir: str, directory containing split .mat files
        output_folder: str, directory to save search results
        query_seq: str, the DNA sequence to search
        min_len: int, minimum length warning threshold
        max_len: int, maximum length warning threshold
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    query_seq = query_seq.strip().upper()
    query_seq = query_seq.replace(" ", "").replace("\n", "")

    # Length check
    if len(query_seq) < min_len:
        print(f"⚠️ Warning: The search sequence is too short ({len(query_seq)} bp), which may result in too many matches!")
    if len(query_seq) > max_len:
        print(f"⚠️ Warning: The search sequence is relatively long ({len(query_seq)} bp), which may increase search time.")

    mat_files = [f for f in os.listdir(mat_dir) if f.endswith('.mat')]
    print(f"🧬 Starting search across {len(mat_files)} chromosome files...")

    results = []
    for file in mat_files:
        mat_path = os.path.join(mat_dir, file)
        try:
            data = loadmat(mat_path)
            chrname = str(data['chrname'][0])
            chrseq = str(data['sequence'][0])
        except Exception as e:
            print(f"❌ Error reading {file}, skipped. Reason: {e}")
            continue

        idx = chrseq.find(query_seq)
        match_count = 0
        while idx != -1:
            results.append({
                'Gene': '-',   # Currently no GFF annotation, placeholder
                'Chromosome': chrname,
                'Start': idx + 1,
                'End': idx + len(query_seq),
                'MatchedSeq': query_seq,
                'SourceFile': file
            })
            match_count += 1
            idx = chrseq.find(query_seq, idx + 1)

        print(f"✅ Search completed: {file:<20} | Matches found: {match_count}")

    if results:
        df = pd.DataFrame(results)
        csv_path = os.path.join(output_folder, 'matched_results.csv')
        df.to_csv(csv_path, index=False)
        print(f"\n🎯 Total {len(results)} matches found. Results saved to: {csv_path}")
    else:
        print("\n⭕ No matches found.")

def user_gui_input_and_search():
    """
    Obtain user input through simple GUI windows and perform the search
    """
    root = tk.Tk()
    root.withdraw()

    # Select the folder containing .mat genome files
    mat_dir = filedialog.askdirectory(title="Select the genome .mat folder")
    if not mat_dir:
        messagebox.showinfo("Notice", "No folder selected. Operation cancelled.")
        return

    # Enter the DNA sequence
    query_seq = simpledialog.askstring("Input Sequence", "Please enter the DNA sequence to search (only A/T/C/G):")
    if not query_seq:
        messagebox.showinfo("Notice", "No sequence entered. Operation cancelled.")
        return

    # Select the output directory
    output_folder = filedialog.askdirectory(title="Select the output directory for search results")
    if not output_folder:
        messagebox.showinfo("Notice", "No output folder selected. Operation cancelled.")
        return

    # Perform search
    search_sequence_across_genome(mat_dir, output_folder, query_seq)

if __name__ == "__main__":
    user_gui_input_and_search()
