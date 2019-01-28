suppressMessages({
  library("sleuth")
})

path <- file.path(".", "sleuthResults/sleuth_object")
pathResults <- file.path(".", "sleuthResults/sleuth_results.tsv")
                         
so = sleuth_load(path)
table <- read.table(pathResults, header = TRUE, stringsAsFactors = FALSE)

pdf("plots/sample_heatmap.pdf")
plot_sample_heatmap(so)


tableShort = head(table, 50)
pdf("plots/transcript_heatmap.pdf")
plot_transcript_heatmap(so, tableShort$target_id, cluster_transcripts = TRUE) 
#, cluster_transcripts = TRUE

