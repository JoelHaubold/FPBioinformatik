#!/usr/bin/env python3

import pandas as pd
import yaml


#Get Sampledict
#If Testing is active add Test directory
try:
	con = open("config.yaml", "r")
	config = yaml.load(con)
except FileNotFoundError:
	print("The file config.yaml was not found.\nPlease check if file is present in the same directory!")
	exit(1)

cwd = ""
if config['testing']:
	cwd += "Tests/"
cwd += "reads/"

#Read Yamlfile
try:
	stream = open("sampleconfig.yaml", "r")
	doc = yaml.load(stream)
except FileNotFoundError:
	print("The file config.yaml was not found.\nPlease check if file is present in the same directory!")
	exit(1)
except yaml.scanner.ScannerError:
	print("The file sampleconfig.yaml could not be read.\nPlease check if syntax is correct!")
	exit(1)

#Import samples as stated in Configfile
samples = doc['samples']
sample_dict = {"sample" : [], "fq1" : [], "fq2" : [], "condition" : []}
for key in samples:
	if len(samples[key]) != 3:
		raise IndexError("False number of Values! Each Sample needs two reads and a condition.")
	#Import Values into Dictonary
	sample_dict["sample"].append(key)
	sample_dict["fq1"].append(cwd+samples[key][0])
	sample_dict["fq2"].append(cwd+samples[key][1])
	sample_dict["condition"].append(samples[key][2])

#Create DataFrame from Dictonary, set Samplename as index and save it as .tsv file
df = pd.DataFrame(sample_dict)
df.set_index("sample")
df.to_csv("samplesheet.tsv", sep='\t', encoding = 'utf-8', index = False)

