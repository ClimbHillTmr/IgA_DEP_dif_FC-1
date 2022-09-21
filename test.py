import os

%matplotlib inline 
%config InlineBackend.figure_format='retina' 
%load_ext autoreload 
%autoreload 2

import csv 
import numpy as np 
import pandas as pd 
import gseapy as gp 
import matplotlib.pyplot as plt

import gseapy

import os
import sys

names = gseapy.get_library_name()
names

#设置文件夹的路径
filePath = r"/Users/cht/Documents/GitHub/IgA_DEP_dif_FC-1/IgA_DEP_dif_FC-1"  # 文件夹目录
#获取文件夹下的所有文件名称
nameList = os.listdir(filePath)

for i in nameList:

    temp1 = temp['geneName'].values.tolist()
    
    gene_sets=['KEGG_2021_Human','GO_Molecular_Function_2021']

    # Enrichr analysis of upregulated
    iga_GOBP = gp.enrichr(gene_list=temp1,
                        gene_sets=gene_sets,
                        organism='Human',
                        outdir='test/iga',
                        cutoff=0.5,
                        format='pdf' 
                    )
    iga_GOBP.results.to_csv("/Users/cht/Documents/GitHub/IgA_DEP_dif_FC-1/result/result "
                    +i+ ".csv"
                    )