import seaborn as sns
import pandas as pd
import yaml

with open("../config.yaml", 'r') as yamlfile:
    config = yaml.load(yamlfile)

testdr = ""
if config["testing"]:
	testdr = "Tests/"


samples = pd.read_table("../sleuthResults/normCounts.tsv")
for sample in samples.c
