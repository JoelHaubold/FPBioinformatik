suppressMessages({
  library("sleuth")
})

path <- file.path(".", snakemake@input[[2]])
pathResults <- file.path(".", snakemake@input[[1]])
                         
so = sleuth_load(path)
table <- read.table(pathResults, header = TRUE, stringsAsFactors = FALSE)

pdf("plots/sample_heatmap.pdf")
plot_sample_heatmap(so)


tableShort = head(table, 50)
pdf("snakemake@output[[1]]")
plot_transcript_heatmap(so, tableShort$target_id, cluster_transcripts = TRUE) 
#, cluster_transcripts = TRUE

