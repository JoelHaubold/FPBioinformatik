import pandas as pd

configfile: "config.yaml"

testdr = ""
if config["testing"]:
	testdr = "Tests/"


samples = pd.read_table(config["samples"], index_col="sample")

def get_fq(wildcards):
	return samples.loc[wildcards.sample, ["fq1","fq2"]].dropna()
		

rule kallisto_index:
	input:
		testdr+"ref/transcriptome.chr21.fa"
	output:
		"genome.idx"
	conda:
		"envs/kallisto.yaml"
	shell:
		"kallisto index -i {output} {input}"

rule kallisto_quant:
	input:
		fq = get_fq,
		inp = "genome.idx"		
	output:
		directory("quantOutput/{sample}")
	shell:
		"kallisto quant -i {input.inp} -o {output} -b 100 {input.fq[0]} {input.fq[1]}"

rule sleuth_lrt:
	input:
		"quantOutput"
	output:
		"sleuth_results.tsv"
	conda:
		"envs/sleuth.yaml"
	shell:
		"Rscript sleuth1.R" 

rule boxplot_counts:
	input:
		""
