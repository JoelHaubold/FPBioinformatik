suppressMessages({
  library("sleuth")
})

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
sleuth_save(so, file = snakemake@output[[2]])


# plot_bootstrap(so, "ENST00000291572", units = "est_counts", color_by = "condition")
# plot_bootstrap(so, "ENST00000474114", units = "est_counts", color_by = "condition")
# plot_bootstrap(so, "ENST00000491703", units = "est_counts", color_by = "condition")
# plot_bootstrap(so, "ENST00000397857", units = "est_counts", color_by = "condition")
# print("Bootstrap plots done")
