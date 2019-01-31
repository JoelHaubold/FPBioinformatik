import seaborn as sns
import pandas as pd
import numpy as np
import os

#set paths for results, counts and samplesheet
path_counts = os.path.abspath(snakemake.input[1])
path_sheet = os.path.abspath(snakemake.input[0])
path_results = os.path.abspath(snakemake.input[2])
#get data from the tables
quants = pd.read_table(path_results, nrows=20).sort_values(by=['pval'], ascending=False)
quants.set_index('target_id', inplace=True)
counts = pd.read_table(path_counts, index_col=0)
sample_sheet = pd.read_table(path_sheet)
#set the style of the plot
sns.set(style="whitegrid")

# Make Dictonary with Samplename as key and Condition as value
conditions = {}
first = ""
for index, row in sample_sheet.iterrows():
    conditions[row['sample']] = row['condition']
    first = row['condition']
#print(conditions)

#gene_name = pd.read_table #not used
# print(quants.head())
# print(counts.head())
# target_id = pd.read_table(("FPBioinformatik/sleuthResults/sleuth_results.tsv"), index_col="target_id")

#concat the results of sleuth and the norm counts
concat = pd.concat([quants, counts], axis=1, join='inner').sort_values(by=['pval'], ascending=False)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(concat)

#drop the unused columns
top20 = concat.drop(concat.columns[range(14)], axis=1) 
print(top20)
top20 = top20.transpose()
print(top20)



#top20.columns['NIPSNAP1','ARID3A','NOTCH2','PLHDA1','NT5E','EN01','ANXA1','SOX4','SCG2','TNFRSF21','SLC2A3','PGM2L1','VCAN','MBTPS1','PLK2','CDKN1A','PARP1','STOM','F2RL1','EPAS1']




print(top20)
test = pd.melt(top20)

#name = concat.get(['ext_gene'])

#create and save the stripchart
ax = sns.stripplot(data=top20, jitter=False, orient="h", )
ax.set_xlabel("Normalized counts") 
ax.set_ylabel("Transcript")
fig = ax.get_figure()
fig.set_size_inches(16, 10.5) #size needs to be changed, so the axis are completely visible
fig.suptitle('Stripchart der top20 differentiell exprimierten Gene ') #title of the stripchart
fig.savefig(snakemake.output[0]) #save the plot



