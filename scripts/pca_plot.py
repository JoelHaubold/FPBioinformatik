import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

path_counts = os.path.abspath('../sleuthResults/normCounts.tsv')
samples = pd.read_table(path_counts)

path_sheet = os.path.abspath('../samplesheet.tsv')
sample_sheet = pd.read_table(path_sheet)

# Make Dictonary with Samplename as key and Condition as value
conditions = {}
for index, row in sample_sheet.iterrows():
	conditions[row['sample']] = row['condition']


x = samples.columns.values[1:]
print(x) 
print("\n")
print(conditions)
