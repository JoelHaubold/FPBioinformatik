rule kallisto_index:
	input:
		"Tests/ref/genome.chr21.fa"
	output:
		"genome.idx"
	conda:
		"envs/kallisto.yaml"
	shell:
		"kallisto index -i {output} {input}"

rule kallisto_quant:
	input:
		inp="genome.idx", 
		fq1 = "Tests/reads/a.chr21.1.fq", 
		fq2 = "Tests/reads/a.chr21.2.fq" 
	output:
		"quantOutput"
	shell:
		"kallisto quant -i {input.inp} -o {output} {input.fq1} {input.fq2}" 
