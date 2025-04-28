# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 16:32:58 2025

@author: 93901
"""

# === 脚本：split_example.py ===
# 功能：示范如何使用fasta_splitter模块拆分大型FASTA文件
# 时间：2025年4月28日 (JST)
# 作者：Shijian

from genome_tools import fasta_splitter

# 配置输入输出路径
input_fasta = r"D:\RNA-seq\v2.1\assembly\Crichardii_676_v2.0.fa"
output_dir = r"D:\RNA-seq\genome_split_chromosomes_all"

# 调用模块执行
fasta_splitter.split_fasta_to_mat(input_fasta, output_dir)
