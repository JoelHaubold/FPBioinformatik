suppressMessages({
  library("sleuth")
})
sample_id = dir(file.path(".", "quantOutput"))
sample_id
sample_sheet = read.table("samplesheet.tsv", header = TRUE, stringsAsFactors = FALSE)
print(sample_sheet)
kal_dirs <- file.path(".", "quantOutput", sample_id)
kal_dirs

table <- dplyr :: select(sample_sheet, sample = sample, condition = condition)
table <- dplyr :: mutate(table, path = kal_dirs)
print(table)


so <- sleuth_prep(table, extra_bootstrap_summary = TRUE)
print("prep done")

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
head(sleuth_significant, 20)

plot_bootstrap(so, "ENST00000291572", units = "est_counts", color_by = "condition")
plot_bootstrap(so, "ENST00000474114", units = "est_counts", color_by = "condition")
plot_bootstrap(so, "ENST00000491703", units = "est_counts", color_by = "condition")
plot_bootstrap(so, "ENST00000397857", units = "est_counts", color_by = "condition")
print("Bootstrap plots done")
