import os
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

features = list(samples.columns.values[1:])

y = []
for sample in features:
    y.append(conditions[sample])
target = []
for condition in y:
    if condition not in target:
        target.append(condition)

x = samples.loc[:, features].values

pca = PCA()

x_pca = pca.fit_transform(x)

pca_df = pd.DataFrame(data=x_pca, columns=features)
pca_df = pca_df.transpose()
melted_df = pd.melt(pca_df)
# pca_df['Condition'] = y

fig = plt.scatter(x="variable", y="value", data=melted_df)
fig.figure.savefig("../plots/pca_plot.png")

colors = ['r', 'b']
