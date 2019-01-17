suppressMessages({
  library("sleuth")
})

path <- file.path(".", "sleuthResults/sleuth_object")
so = sleuth_load(path)

pdf("plots/sample_heatmap.pdf")
plot_sample_heatmap(so)

