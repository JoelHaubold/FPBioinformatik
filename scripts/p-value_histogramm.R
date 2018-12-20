path <- file.path(".", "sleuth_results.tsv")
savepath <- file.path(".", "plots")
table <- read.table(path, header = TRUE, stringsAsFactors = FALSE)

pdf("plots/p-values_histogramm.pdf")
#hist(table$pval)
hist(table$pval, 
     main="Histogram of p-values", 
     xlab="p-values",
     ylab="count",
     border="blue", 
     col="black")
dev.off()