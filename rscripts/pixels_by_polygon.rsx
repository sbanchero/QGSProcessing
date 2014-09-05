##layer_raster=raster
##layer_vector=vector
##out=string
##INTA=group

#Librerias R que son requeridas
library("raster")

overR <- extract(layer_raster,layer_vector, df=TRUE)
res.agg <- aggregate(overR, by=list(overR[[names(overR)[1]]], overR[[names(overR)[2]]]), FUN=length)
names(res.agg)<-c('ID','PIXEL','CANT','VALRAS')
write.csv(res.agg[c(1,2,3)], file=out )

