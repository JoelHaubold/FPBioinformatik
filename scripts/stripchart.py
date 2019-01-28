import seaborn as sns
import pandas as pd
import os

path_counts = os.path.abspath('../sleuthResults/normCounts.tsv')
path_sheet = os.path.abspath('../samplesheet.tsv')
path_results = os.path.abspath('../sleuthResults/sleuth_results.tsv')

sns.set (style="whitegrid")
quants = pd.read_table(path_results, nrows=20).sort_values(by=['pval'],ascending=False)
quants.set_index('target_id',inplace=True)

counts = pd.read_table(path_counts,index_col=0)

sample_sheet = pd.read_table(path_sheet)

# Make Dictonary with Samplename as key and Condition as value
conditions = {}
for index, row in sample_sheet.iterrows():
	conditions[row['sample']] = row['condition']

x = counts.columns.values[1:]
#print(x) 
#print("\n")
#print(conditions)

gene_name = pd.read_table
#print(quants.head())
#print(counts.head())
#target_id = pd.read_table(("FPBioinformatik/sleuthResults/sleuth_results.tsv"), index_col="target_id")
concat=pd.concat([quants, counts],axis=1,join='inner').sort_values(by=['pval'],ascending=False)
name = concat.get(['ext_gene'])
expr = concat.get(['pval'])
count = concat.get(['a'])
#countb = concat.get(['b'])

#print(concat)
#print(count)
#print(countb)

ax=sns.stripplot(  y=count, data=quants ,jitter=False, orient="h")
#bx=sns.stripplot(  y=countb, data=quants ,jitter=False, orient="h")

fig = ax.get_figure()
fig.savefig('../plots/stripchart_normalized_counts.pdf')

#fig2 =bx.get_figure()
#fig2.savefig('Top20b.png')

		 
