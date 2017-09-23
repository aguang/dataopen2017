import csv
import pandas as pd
import numpy as np
import collections as c

df = pd.read_csv('/Users/zhengt/Desktop/Boston Datathon Materials/toxicogenomics_diseases.csv')
df = df.head(100)

#gene_score would be a dictionary of dictionary.
#the keys of gene_score would be the gene_id of each gene
#the values of gene_score would be a dictionary with inference score (value) mapped to each disease(key)
gene_score = {}
for index, row in df.iterrows():
   if row['gene_id'] not in gene_score:
      gene_score[row['gene_id']] = {}
   else:
      if row['disease_name'] not in gene_score[row['gene_id']]:
         gene_score[row['gene_id']][row['disease_name']] = row['inference_score']
      continue
