# cluster analysis
d <- read.csv("DIRECTORY/sin_weighted.csv")
dM <- as.dist(d)
hc = hclust(dM, method = 'ward.D')

# plot dendrogram
plot(hc, cex = 0.4)

# plot dendrogram with color bar underneath corresponding to external classification
library(WGCNA)
classlabels <- unlist(read.csv("DIRECTORY/worddictentries.csv", colClasses=c('NULL','NULL','NULL','NULL',NA,'NULL')))
plotDendroAndColors(hc, labels2colors(classlabels), cex.dendroLabels=.4)