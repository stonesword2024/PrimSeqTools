# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 17:17:31 2025

@author: Shijian
"""

# === Script: main_controller.py ===
# Purpose: Manage all modules (FASTA splitting, primer specificity check, large fragment search)
# Date: April 28, 2025 (JST)
# Author: Shijian

import os
import sys
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

# Assume these modules are located under genome_tools package
from genome_tools import fasta_splitter, primer_checker, sequence_searcher, utils

def choose_directory(prompt_title="Select a folder"):
    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory(title=prompt_title)
    if not folder:
        messagebox.showinfo("Notice", "No folder selected. Operation cancelled.")
        sys.exit()
    return folder

def choose_file(prompt_title="Select a file", filetypes=[("All files", "*.*")]):
    root = tk.Tk()
    root.withdraw()
    file = filedialog.askopenfilename(title=prompt_title, filetypes=filetypes)
    if not file:
        messagebox.showinfo("Notice", "No file selected. Operation cancelled.")
        sys.exit()
    return file

def input_sequence(prompt_title="Enter the DNA sequence"):
    root = tk.Tk()
    root.withdraw()
    seq = simpledialog.askstring("Input Sequence", prompt_title)
    if not seq:
        messagebox.showinfo("Notice", "No sequence entered. Operation cancelled.")
        sys.exit()
    return seq

def run_fasta_splitter():
    print("\n🔵 [1] Split large FASTA file")
    fasta_file = choose_file("Select the large FASTA file", filetypes=[("FASTA files", "*.fa *.fasta")])
    output_dir = choose_directory("Select the output directory for split results")
    utils.mkdir_if_not_exists(output_dir)

    print("\nStarting to split the FASTA file...")
    fasta_splitter.split_fasta_to_mat(fasta_file, output_dir)
    print("🎉 FASTA splitting completed.\n")

def run_primer_checker():
    print("\n🔵 [2] Primer specificity check")
    mat_dir = choose_directory("Select the folder containing genome .mat files")
    primer_file = choose_file("Select the primer file (txt or csv)", filetypes=[("Text files", "*.txt *.csv")])
    output_dir = choose_directory("Select the output directory for primer match results")
    utils.mkdir_if_not_exists(output_dir)

    primers = utils.load_primers_from_file(primer_file)

    print("\nStarting primer specificity check...")
    primer_checker.check_primers(mat_dir, output_dir, primers)
    print("🎉 Primer specificity check completed.\n")

def run_sequence_searcher():
    print("\n🔵 [3] Search large fragment sequence")
    mat_dir = choose_directory("Select the folder containing genome .mat files")
    query_seq = input_sequence("Enter the DNA sequence to search (only A/T/C/G characters):")
    output_dir = choose_directory("Select the output directory for search results")
    utils.mkdir_if_not_exists(output_dir)

    print("\nStarting large fragment search...")
    sequence_searcher.search_sequence_across_genome(mat_dir, output_dir, query_seq)
    print("🎉 Large fragment search completed.\n")

def main_menu():
    while True:
        print("\n=== PrimSeqTools Main Menu ===")
        print("[1] Split large FASTA file")
        print("[2] Primer specificity check")
        print("[3] Search large fragment sequence")
        print("[0] Exit program")
        choice = input("Please enter the number to select a function (0/1/2/3): ").strip()

        if choice == '1':
            run_fasta_splitter()
        elif choice == '2':
            run_primer_checker()
        elif choice == '3':
            run_sequence_searcher()
        elif choice == '0':
            print("👋 Program exited. Goodbye!")
            sys.exit()
        else:
            print("❌ Invalid input. Please enter 0, 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()
