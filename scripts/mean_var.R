

suppressMessages({
  library("sleuth")
})

#path <- file.path(".", "sleuthResults/sleuth_object")
#path2 <- file.path(".", "sleuthResults/sleuth_wald_object")
#pathResults <- file.path(".", "sleuthResults/sleuth_results.tsv")

so = sleuth_load(snakemake@input[[2]])
wt = sleuth_load(snakemake@input[[3]])
table <- read.table(pathResults, header = TRUE, stringsAsFactors = FALSE)

pdf(snakemake@output[[1]])
plot_mean_var(so)
print("mean variance plot done")

tests(wt)
pdf(snakemake@output[[2]])
plot_ma(wt, test = "conditionscramble", test_type = "wt")

pdf(snakemake@output[[3]])
plot_vars(wt)

pdf(snakemake@output[[4]])
plot_group_density(so)