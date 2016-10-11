# cluster analysis
d <- as.dist(read.csv("/Users/Weijian/Desktop/dstrdist/sin_weighted.csv"))
hc = hclust(d, method = 'ward.D')

# plot dendrogram
plot(hc, cex = 0.4)

# optimal number of clusters using CH index
library(fpc)
krange <- c(2:506)
l_ch <- vector('list',length(krange))
l_asw <- vector('list',length(krange))
for (i in 1:length(krange)){
	ch_k <- cluster.stats(d,cutree(hc,k=krange[i]))$ch
	l_ch[i] <- ch_k
	asw_k <- cluster.stats(d,cutree(hc,k=krange[i]))$avg.silwidth
	l_asw[i] <- asw_k
}
plot(krange,l_ch)
plot(krange,l_asw)