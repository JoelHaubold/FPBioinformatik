suppressMessages({
  library("sleuth")
})
sample_id = dir(file.path(".", "quantOutput"))
print(sample_id)

sample_sheet = read.table("samplesheet.tsv", header = TRUE, stringsAsFactors = FALSE)
print(sample_sheet)
kal_dirs <- file.path(".", "quantOutput", sample_id)
kal_dirs

table <- dplyr :: select(sample_sheet, sample = sample, condition = condition)
table <- dplyr :: mutate(table, path = kal_dirs)
table

so <- sleuth_prep(table, extra_bootstrap_summary = TRUE)