import seaborn as sns
import pandas as pd
import numpy as np
import os

path_counts = os.path.abspath('../sleuthResults/normCounts.tsv')
path_sheet = os.path.abspath('../samplesheet.tsv')
path_results = os.path.abspath('../sleuthResults/sleuth_results.tsv')

sns.set(style="whitegrid")
quants = pd.read_table(path_results, nrows=20).sort_values(by=['pval'], ascending=False)
quants.set_index('ext_gene', inplace=True)

counts = pd.read_table(path_counts, index_col=0)

sample_sheet = pd.read_table(path_sheet)

conditions = {}
for index, row in sample_sheet.iterrows():
    conditions[row['sample']] = row['condition']

x = counts.columns.values[1:]
# print(x)
# print("\n")
# print(conditions)

gene_name = pd.read_table
# print(quants.head())
# print(counts.head())
# target_id = pd.read_table(("FPBioinformatik/sleuthResults/sleuth_results.tsv"), index_col="target_id")
concat = pd.concat([quants, counts], axis=1, join='inner').sort_values(by=['pval'], ascending=False)

top20 = concat.drop(concat.columns[range(14)], axis=1)
top20 = top20.transpose()
name = concat.get(['ext_gene'])
expr = concat.get(['pval'])
count = concat.get(['SRR493366'])

expr = np.reshape(expr.values, len(expr))
count = np.reshape(count.values, len(count))

test = pd.melt(top20)



print("\n")
print("quants:")
print(quants)
print("\n")
print("expr:")
print(expr)
print("\n")
print("concat")
print(concat)
print("\n")
print("count:")
print(count)
# print(name)
# print(countb)

ax = sns.stripplot(data=top20, jitter=True, orient="h")

fig = ax.get_figure()
fig.set_size_inches(16, 10.5)
fig.savefig('../plots/stripchart_normalized_counts.pdf')

