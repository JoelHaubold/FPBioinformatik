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
		"kallisto quant -i {input.inp} --fusion -o {output} -b 5 {input.fq[0]} {input.fq[1]}"

rule pizzly:
	input:
		gtf = config["gtfReference"],
		fa = config["reference"],
		fusion = "quantOutput/{sample}",
	output:
		json = "pizzlyOutput/{sample}/test.json"
	conda:
		"envs/pizzly.yaml"
	shell:
		"pizzly -k 31 --gtf {input.gtf} --cache index.cache.txt --align-score 2 --insert-size 400 --fasta {input.fa} --output pizzlyOutput/{wildcards.sample}/test {input.fusion}"		

rule pizzly_flatten_json:
	input:
		"pizzlyOutput/{sample}/test.json"
	output:
		"pizzlyOutput/{sample}/flattenedJson"
	script:
		"scripts/pizzly_flatten_json.py"

rule sleuth_lrt:
	input:
		test=expand("quantOutput/{sample1}", sample1=SAMPLES)
		#directory("quantOutput")
	output:
		sleuthR = "sleuthResults/sleuth_results.tsv",
		sleuthNorm = "sleuthResults/normCounts.tsv",
		sleuthObj = "sleuthResults/sleuth_object"
	conda:
		"envs/sleuth.yaml"
	script:
		"scripts/sleuth_lrt.R" 

rule sleuth_wt:
	input:
		sleuthR = "sleuthResults/sleuth_results.tsv",
		sleuthObj = "sleuthResults/sleuth_object",
		test=expand("quantOutput/{sample1}", sample1=SAMPLES)
	output:
		"sleuthResults/sleuth_wald_results.tsv",
		"sleuthResults/sleuth_wald_object"
	conda:
		"envs/sleuth.yaml"
	script:
		"scripts/sleuthWaldTest.R"

rule sleuth_heatmap:
	input:
		sResults = "sleuthResults/sleuth_results.tsv",
		sObject = "sleuthResults/sleuth_object"
	output:
		"plots/sample_heatmap.pdf"
	conda:
		"envs/heatmap.yaml"
	script:
		"scripts/heatmap.R"
		


rule volcano_plot:
	input:
		"sleuthResults/sleuth_wald_results.tsv"
	output:
		"plots/qvsbeta_values_volcanoPlot.pdf"
	conda:
		"envs/sleuth.yaml"
	script:
		"scripts/qvsbeta_values_volcanoPlot.py"

rule boxplot_counts:
	input: ""
		


rule pvalue_hist:
	input:
		"sleuthResults/sleuth_results.tsv"
	output:
		"plots/p-values_histogramm.pdf"
	conda:
		"envs/sleuth.yaml"
	script:
		"scripts/p-value_histogramm.R"

rule mean_variance:
	input:
		results= "sleuthResults/sleuth_results.tsv",
		lrt_obj= "sleuthResults/sleuth_object",
		wt_obj= "sleuthResults/sleuth_wald_object"
	output:
		"plots/mean_var_plot.pdf",
		"plots/ma_plot.pdf",
		"plots/vars_plot.pdf",
		"plots/group_density.pdf"
	conda:
		"envs/sleuth.yaml"
	script:
		"scripts/mean_var.R"
