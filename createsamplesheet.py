import os
import pandas as pd

#Get current dictonary
cwd = os.getcwd()

#Test dictonary
cwd += "/Tests/"

#Sampledict
cwd += "reads/"
files = [f for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, f))]
files.sort()

#Create Dictonary for DataFrame
sdict = {"sample" : ["a","b"], "fq1" : [files[0],files[2]], "fq2" : [files[1],files[3]], "condition" : ["treated", "untreated"]}
df = pd.DataFrame(sdict)
df.set_index("sample")
df.to_csv("samplesheet.tsv", sep='\t', encoding = 'utf-8', index = False)



