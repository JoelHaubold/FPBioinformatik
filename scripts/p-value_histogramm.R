path <- file.path(".", "sleuthResults/sleuth_results.tsv")
savepath <- file.path(".", "plots")
table <- read.table(path, header = TRUE, stringsAsFactors = FALSE)
print(table)

pdf("plots/p-values_histogramm.pdf")
#hist(table$pval)
hist(table$pval, 
     main="Histogram of p-values", 
     xlab="p-values",
     ylab="count",
     border="black", 
     col="black")
#dev.off()

print("p-value_Histogramm successfully created at .plots/p-values_histogramm.pdf")