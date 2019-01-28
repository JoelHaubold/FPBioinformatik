suppressMessages({
  library("sleuth")
})
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

path <- file.path(".", snakemake@input[[2]])
pathResults <- file.path(".", snakemake@input[[1]])

so = sleuth_load(path)

print("models")
models(so)
so <- sleuth_wt(so, 'conditionscramble')
print("wt done")

print("tests")
tests(so)

sleuth_table <- sleuth_results(so, 'conditionscramble', 'wt', show_all = FALSE)
sleuth_significant <- dplyr::filter(sleuth_table, qval <= 0.05)
print(head(sleuth_significant, 20))

write.table(sleuth_table, file=snakemake@output[[1]], quote=FALSE, sep='\t', col.names = NA)


# plot_bootstrap(so, "ENST00000291572", units = "est_counts", color_by = "condition")
# plot_bootstrap(so, "ENST00000474114", units = "est_counts", color_by = "condition")
# plot_bootstrap(so, "ENST00000491703", units = "est_counts", color_by = "condition")
# plot_bootstrap(so, "ENST00000397857", units = "est_counts", color_by = "condition")
# print("Bootstrap plots done")
