# cluster analysis
d <- as.dist(read.csv("/DIRECTORY/sin_weighted.csv"))
hc = hclust(d, method = 'ward.D')

# plot dendrogram
plot(hc, cex = 0.4)