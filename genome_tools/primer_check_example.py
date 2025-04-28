# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 16:50:29 2025

@author: 93901
"""

# === 脚本：primer_check_example.py ===
# 功能：示范如何使用primer_checker模块检查引物特异性
# 时间：2025年4月28日 (JST)
# 作者：Shijian

from genome_tools import primer_checker

# 配置路径
indir = r"D:\RNA-seq\genome_split_chromosomes_all"  # 分割后的mat文件目录
outdir = r"D:\RNA-seq\primer_search_results"        # 输出目录

# 引物序列列表（每条自动正向+反向互补搜索）
primers = [
    "TAAGTGTAAAGTCACTGGCACCAAGTG",
    "GTTGGCAGTAGCACGAATAAGAAATCAC",
    "GGGTTTGATCTGTGTGCCTGGAG",
    "CAAGCTAAACTGCCTACCCAACATGT"
]

# 调用搜索
primer_checker.check_primers(indir, outdir, primers)
