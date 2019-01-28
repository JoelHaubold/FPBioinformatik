import seaborn as sns
import pandas as pd
import yaml

with open("../config.yaml", 'r') as yamlfile:
    config = yaml.load(yamlfile)

testdir = ""
if config["testing"]:
    testdir = "Tests/"

# Open Sampleconfig to get third value of samples
with open("../sampleconfig.yaml", 'r') as ymlfile:
    sample_config = yaml.load(ymlfile)
samples = sample_config['samples']
first = ""
sample_dict = {}
for sample in samples:
    if first == "" or first == samples[sample][2]:
        first = samples[sample][2]
        sample
    sample_dict[sample] = samples[sample][2]

sns.set_color_codes()
tips = sns.load_dataset("tips")
pal = {}
# Read Table from File
samples = pd.read_table("../sleuthResults/normCounts.tsv")

# Get Colors of conigfile

# Drop Gene-Names because they are unnecessary
samples = samples.drop(samples.columns[0], axis=1)
print(pd.melt(samples))
boxplot = sns.boxplot(x="variable", y="value", data=pd.melt(samples))
boxplot.set(xlabel='Samples', ylabel="log (base 2) read counts + 0.5")
figure = boxplot.get_figure()
figure.savefig("../plots/boxplot_sample_counts.png")