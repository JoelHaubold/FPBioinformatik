# library(gage)
# 
# filename=system.file("extdata/gse16873.demo", package = "gage")
# demo.data=readExpData(filename, row.names=1)
# #check the data
# head(demo.data)
# 
# str(demo.data)
# 
# #convert the data.frame into a matrix as to speed up the computing
# demo.data=as.matrix(demo.data)
# str(demo.data)

# #_lrt needs
# st <- sleuth_prep(table, extra_bootstrap_summary = TRUE, target_mapping = t2g, 
#                   aggregation_column = "ext_gene", gene_mode = TRUE)

library(gage)

data(gse16873)
hn=(1:3)*2-1
dcis=(1:3)*2

hn2= (1:3)
dcis2= (4:6)
#getGenesTsv
# <- read.table("D:\\Ole\\Dokumente\\R_Programme\\BioInf\\genes.tsv")

#rowname target_id as column
d <- table
names <- rownames(d)
rownames(d) <- NULL
data <- cbind(names,d)
colnames(data)[colnames(data)=="names"] <- "sym"


data(egSymb)

#merge at sym
newFrame <- merge(data, egSymb, by.x = "sym", by.y = "sym", all.x = TRUE)

noNaFrame <- newFrame[complete.cases(newFrame), ]

row.names(noNaFrame) <- noNaFrame$eg
noNaFrame[1] <- NULL

drops <- c("sym", "eg")
expTable = noNaFrame[ , !(names(noNaFrame) %in% drops)]

#head(gse16873)
#head(table)
head(expTable)
data(kegg.gs)

gageoutput <- gage(expTable, gsets = kegg.gs)
#gagetest <- gage(expTable, gsets = kegg.gs, ref = hn, samp = dcis)
#gagetest2 <- gage(expTable, gsets = kegg.gs, ref = hn2, samp = dcis2)

gageSig <- sigGeneSet(gageoutput, outname="shrug.kegg")
#gse16873.kegg.sig2<-sigGeneSet(gagetest2, outname="genes.kegg")
#gse16873.kegg.sig<-sigGeneSet(gagetest, outname="genes.kegg")

gs=unique(unlist(kegg.gs[rownames(gageoutput$greater)[1:3]]))
essData=essGene(gs, expTable)

 for (gs in rownames(gageoutput$greater)[1:3]) {
       outname = gsub(" |:|/", "_", substr(gs, 10, 100))
       geneData(genes = kegg.gs[[gs]], exprs = essData, ref = 1:3, samp = 4:6, outname = outname, txt = T, heatmap = TRUE,
                          Colv = F, Rowv = F, dendrogram = "none", limit = 3, scatterplot = TRUE)
   }

#geneDataStuff <- geneData(genes = gs, exprs = essData, outname = "geneData", heatmap = TRUE, scatterplot = TRUE)
