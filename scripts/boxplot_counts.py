import seaborn as sns
import pandas as pd
import os

path_sheet = os.path.abspath(snakemake.input[0])
sample_sheet = pd.read_table(path_sheet)

# Make Dictonary with Samplename as key and Condition as value
conditions = {}
first = ""
for index, row in sample_sheet.iterrows():
    conditions[row['sample']] = row['condition']
    first = row['condition']
palette = {condition: "r" if conditions[condition] == first else "g" for condition in conditions}

sns.set_color_codes()

# Read Table from File
samples = pd.read_table(snakemake.input[1])

# Drop Gene-Names because they are unnecessary
samples = samples.drop(samples.columns[0], axis=1)
# Melt Dataframe into two Columns variable (Samplename) and the value
melt_samples = pd.melt(samples)
# Remove 0 values
samples = melt_samples.loc[melt_samples.value != 0]
# Create Boxplot
boxplot = sns.boxplot(x="variable", y="value", data=samples, palette=palette, fliersize=0)
boxplot.set(xlabel='Samples', ylabel="log (base 2) read counts + 0.5")
boxplot.set(ylim=(0, 20))

figure = boxplot.get_figure()
figure.savefig(snakemake.output[0])
