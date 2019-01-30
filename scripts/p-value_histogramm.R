path <- file.path(".", snakemake@input[[1]])
savepath <- file.path(".", "plots")
table <- read.table(path, header = TRUE, stringsAsFactors = FALSE)


pdf(snakemake@output[[1]])
#hist(table$pval)
hist(table$pval, 
     main="Histogram of p-values", 
     xlab="p-values",
     ylab="count",
     border="black", 
     col="black")
#dev.off()

print("p-value_Histogramm successfully created at .plots/p-values_histogramm.pdf")
