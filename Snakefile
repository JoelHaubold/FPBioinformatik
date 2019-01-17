import pandas as pd


configfile: "config.yaml"

testdr = ""
if config["testing"]:
	testdr = "Tests/"

#To get fq Wildcards
samples = pd.read_table(config["samples"], index_col="sample")
 
SAMPLES = pd.read_table(config["samples"])
SAMPLES = SAMPLES[SAMPLES.columns[0]]


def get_fq(wildcards):
	return samples.loc[wildcards.sample, ["fq1","fq2"]].dropna()
		

def get_input():
	if config["indexFlag"]:
		return config["indexPath"]
	return "genome.idx"	

rule kallisto_index:
	input:
		config["reference"]
		#testdr+"ref/transcriptome.chr21.fa"
	output:
		"genome.idx"
	conda:
		"envs/kallisto.yaml"
	shell:
		"kallisto index -i {output} {input}"

rule kallisto_quant:
	input:
		fq = get_fq,
		inp = get_input()
	output:
		directory("quantOutput/{sample}")
	shell:
		"kallisto quant -i {input.inp} -o {output} -b 100 {input.fq[0]} {input.fq[1]}"

rule sleuth_lrt:
	input:
		test=expand("quantOutput/{sample1}", sample1=SAMPLES)
		#directory("quantOutput")
	output:
		"sleuthResults/sleuth_results.tsv"
	conda:
		"envs/sleuth.yaml"
	shell:
		"Rscript sleuth1.R" 

rule sleuth_wt:
	input:
		"quantOutput"
	output:
		"sleuthResults/sleuth_wald_results.tsv"
	conda:
		"envs/sleuth.yaml"
	shell:
		"Rscript sleuthWaldTest.R"

rule boxplot_counts:
	input:
		""


rule pvalue_hist:
	input:
		directory("sleuthResults/sleuth_results.tsv")
	output:
		"plots/p-values_histogramm.pdf"
	conda:
		"envs/sleuth.yaml"
	shell:
		"Rscript scripts/p-value_histogramm.R"
