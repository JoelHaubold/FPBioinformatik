import seaborn as sns
import pandas as pd
import numpy as np
import os

path_counts = os.path.abspath('../sleuthResults/normCounts.tsv')
path_sheet = os.path.abspath('../samplesheet.tsv')
path_results = os.path.abspath('../sleuthResults/sleuth_results.tsv')

sns.set(style="whitegrid")
quants = pd.read_table(path_results, nrows=20).sort_values(by=['pval'], ascending=False)
quants.set_index('target_id', inplace=True)

counts = pd.read_table(path_counts, index_col=0)

sample_sheet = pd.read_table(path_sheet)

conditions = {}
for index, row in sample_sheet.iterrows():
    conditions[row['sample']] = row['condition']


# Make Dictonary with Samplename as key and Condition as value
conditions = {}
first = ""
for index, row in sample_sheet.iterrows():
    conditions[row['sample']] = row['condition']
    first = row['condition']




			
			

x = counts.columns.values[1:]
print(x)
print("\n")
print(conditions)

gene_name = pd.read_table
# print(quants.head())
# print(counts.head())
# target_id = pd.read_table(("FPBioinformatik/sleuthResults/sleuth_results.tsv"), index_col="target_id")
concat = pd.concat([quants, counts], axis=1, join='inner').sort_values(by=['pval'], ascending=False)

top20 = concat.drop(concat.columns[range(14)], axis=1)
top20 = top20.transpose()

print(concat)
print(top20) 

#top20.columns['NIPSNAP1','ARID3A','NOTCH2','PLHDA1','NT5E','EN01','ANXA1','SOX4','SCG2','TNFRSF21','SLC2A3','PGM2L1','VCAN','MBTPS1','PLK2','CDKN1A','PARP1','STOM','F2RL1','EPAS1']


expr = concat.get(['pval'])
count = concat.get(['SRR493366'])
expr = np.reshape(expr.values, len(expr))
count = np.reshape(count.values, len(count))

test = pd.melt(top20)

name = concat.get(['ext_gene'])

top20test=top20




ax = sns.stripplot(data=top20, jitter=False, orient="h",palette="Set2")
ax.set_xlabel("Normalized counts")
ax.set_ylabel("Transcript")


fig = ax.get_figure()
fig.set_size_inches(16, 10.5)
fig.suptitle('Stripchart der top20 differentiell exprimierten Gene ')
fig.savefig('../plots/stripchart_normalized_counts.pdf')


