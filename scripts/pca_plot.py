import os
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
# Get Paths
path_counts = os.path.abspath(snakemake.input[1])
samples = pd.read_table(path_counts)
path_sheet = os.path.abspath(snakemake.input[0])
sample_sheet = pd.read_table(path_sheet)


# Make Dictonary with Samplename as key and Condition as value
conditions = {}
for index, row in sample_sheet.iterrows():
    conditions[row['sample']] = row['condition']
# List containing sample names
features = list(samples.columns.values[1:])
# Get conditions in order
y = []
for sample in features:
    y.append(conditions[sample])
# Crate Dictionary with Sample as key and condition as value
target = []
for condition in y:
    if condition not in target:
        target.append(condition)
# Get values in order
x = samples.loc[:, features].values
x = x.transpose()
# Create pca-Arry
pca = PCA()
x_pca = pca.fit_transform(x)
# Create DataFrame from pca-Array
pca_df = pd.DataFrame(data=x_pca, columns=features)
# Transpose Dataframe
pca_df = pca_df.transpose()
# Melt it into a DataFrame with two Columns 'variable' containing the index of the transcript and 'value' for the values
melted_df = pd.melt(pca_df)
# pca_df['Condition'] = y

fig = plt.scatter(x="variable", y="value", data=melted_df)
fig.figure.savefig(snakemake.output[0])

colors = ['r', 'b']
