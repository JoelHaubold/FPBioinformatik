suppressMessages({
  library("sleuth")
})
#TODO In conda rule machen 
source("http://bioconductor.org/biocLite.R")
biocLite("biomaRt")

sample_id = dir(file.path(".", "quantOutput"))
sample_id
sample_sheet = read.table("samplesheet.tsv", header = TRUE, stringsAsFactors = FALSE)
#allign sample_sheet sample order with file explorer order
sample_sheet = sample_sheet[order(sample_sheet$sample),]
print(sample_sheet)
kal_dirs <- file.path(".", "quantOutput", sample_id)
kal_dirs

table <- dplyr :: select(sample_sheet, sample = sample, condition = condition)
table <- dplyr :: mutate(table, path = kal_dirs)
print(table)

mart <- biomaRt::useMart(biomart = "ENSEMBL_MART_ENSEMBL",
                         dataset = "hsapiens_gene_ensembl",
                         host = 'ensembl.org')
t2g <- biomaRt::getBM(attributes = c("ensembl_transcript_id", "ensembl_gene_id",
                                     "external_gene_name"), mart = mart)
t2g <- dplyr::rename(t2g, target_id = ensembl_transcript_id,
                     ens_gene = ensembl_gene_id, ext_gene = external_gene_name)
print("t2g:")
print(head(t2g))

print("pre sleuth stuff")
st <- sleuth_prep(table, extra_bootstrap_summary = TRUE, target_mapping = t2g, aggregation_column = "ext_gene", gene_mode = TRUE)

so <- sleuth_prep(table, extra_bootstrap_summary = TRUE, target_mapping = t2g)
print("prep done")
print("----------------------------------------------------------------------")
matrixGene <- sleuth_to_matrix(st, "obs_norm","tpm")

matrix <- sleuth_to_matrix(so, "obs_norm", "tpm")
print(head(matrix, 20))
print("----------------------------------------------------------------------")
#so <- sleuth_fit(so, ~ condition)
so <- sleuth_fit(so, ~condition, 'full')
print("full done")
so <- sleuth_fit(so, ~1, 'reduced')
print("reduced done")
so <- sleuth_lrt(so, 'reduced', 'full')
print("lrt done")
models(so)


sleuth_table <- sleuth_results(so, 'reduced:full', 'lrt', show_all = FALSE)
sleuth_significant <- dplyr::filter(sleuth_table, qval <= 0.05)
print(head(sleuth_significant, 20))


write.table(matrixGene, file= snakemake@output[[4]], quote=FALSE, sep='\t', col.names = NA)
write.table(sleuth_table, file=snakemake@output[[1]], quote=FALSE, sep='\t', col.names = NA)
write.table(matrix, file= snakemake@output[[2]], quote=FALSE, sep='\t', col.names = NA)
sleuth_save(so, file = snakemake@output[[3]])

