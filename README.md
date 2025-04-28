📄 README.md（最终发布版）

# PrimSeqTools

🧬 **PrimSeqTools** is a lightweight toolkit for genome data processing, designed for researchers who need to split large genome FASTA files, check primer specificity, and search for large DNA fragments efficiently.

This toolkit is particularly suitable for small-scale manual operations and can be used alongside genome browsers such as [IGV](https://software.broadinstitute.org/software/igv/) and [JBrowse](https://jbrowse.org/).

---

## 📦 Features

- **FASTA Splitting**
  - Split a large genome FASTA file by chromosomes or scaffolds.
  - Save each sequence individually as a `.mat` file.

- **Primer Specificity Check**
  - Search for both forward primers and their reverse complements across the genome.
  - Detect multiple matching primers and generate detailed reports.

- **Large Fragment Search**
  - Search for large DNA sequences (recommended between 50–5000 bp).
  - Output matched regions across all chromosomes.

---

## 🛠️ Installation

PrimSeqTools is developed in Python.  
Python 3.8 or later is recommended.

### 1. Clone the repository

```bash
git clone https://github.com/stonesword2024/PrimSeqTools.git
cd PrimSeqTools

2. Install dependencies

Install required packages using:

pip install -r requirements.txt

    Tip: It is recommended to set up a virtual environment before installing dependencies.

🚀 Usage
Run the Main Controller Script

After entering the project directory, simply run:

python main_controller.py

You will see a menu:

    1 ➔ Split large FASTA file

    2 ➔ Primer specificity check

    3 ➔ Search large DNA fragment

    0 ➔ Exit program

All operations are GUI-assisted. You will be guided through simple dialogs to select files, input sequences, and specify output locations.
📜 Quick Start for Windows Users

If you are using Windows, you can also run the toolkit by simply double-clicking the batch file:

scripts/run_primseqtools.bat

Make sure Python is installed and correctly added to your system PATH.
📂 Input File Requirements

    FASTA Splitting

        Input: Standard FASTA format file.

        Output: One .mat file per chromosome or scaffold.

    Primer Specificity Check

        Supported primer input:

            Plain TXT file: one sequence per line (direction unknown).

            CSV file: must contain Direction (forward/reverse) and Sequence columns.

    Large Fragment Search

        Recommended query sequence length: 50–5000 bp.

        Only exact matches are reported (no mismatch allowed).

🧭 Recommended Genome Browsers

To visualize search results or nearby genes, we recommend:

    IGV - Integrative Genomics Viewer

    JBrowse

    Note: PrimSeqTools does not include built-in GFF3 annotation parsing. External genome browsers are suggested for advanced exploration.

📬 Contact

If you have any questions, suggestions, or encounter issues, feel free to contact:

    📧 stonesword2018@gmail.com

📄 License

This project is licensed under the MIT License.

See the LICENSE file for details.