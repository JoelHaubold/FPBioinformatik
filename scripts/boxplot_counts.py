import seaborn as sns
import pandas as pd
import yaml
import os

path_sheet = os.path.abspath('../samplesheet.tsv')
sample_sheet = pd.read_table(path_sheet)

# Make Dictonary with Samplename as key and Condition as value
conditions = {}
first = ""
for index, row in sample_sheet.iterrows():
    conditions[row['sample']] = row['condition']
    first = row['condition']

sns.set_color_codes()
tips = sns.load_dataset("tips")

# Read Table from File
samples = pd.read_table("../sleuthResults/normCounts.tsv")

# Drop Gene-Names because they are unnecessary
samples = samples.drop(samples.columns[0], axis=1)
test = pd.melt(samples)
boxplot = sns.boxplot(x="variable", y="value", data=pd.melt(samples))
boxplot.set(xlabel='Samples', ylabel="log (base 2) read counts + 0.5")
palette = {condition: "r" if conditions[condition] == first else "g" for condition in conditions}
print(palette)

figure = boxplot.get_figure()
figure.savefig("../plots/boxplot_sample_counts.png")
