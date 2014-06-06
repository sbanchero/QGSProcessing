##[INTA]=group
##Input_raster=raster
##Band=number 1
##No_Data=number 0
##Output_Raster_Name=string

import os
from osgeo import gdal, ogr, osr
from processing.core.TableWriter import TableWriter
from processing.core.GeoAlgorithmExecutionException import \
        GeoAlgorithmExecutionException
from processing.tools.raster import *



def array2raster(newRasterfn,geoTransform,rasterCRS,pixelWidth,pixelHeight, array):
    cols = array.shape[1]
    rows = array.shape[0]
    driver = gdal.GetDriverByName('GTiff')
    outRaster = driver.Create(newRasterfn, cols, rows, 1, gdal.GDT_Byte)
    outRaster.SetGeoTransform(geoTransform)
    outband = outRaster.GetRasterBand(1)
    outband.WriteArray(array)
    outRaster.SetProjection(rasterCRS.ExportToWkt())
    outband.FlushCache()
    




raster = gdal.Open(Input_raster)

pixelWidth = raster.RasterXSize
pixelHeight = raster.RasterYSize
geoTransform = raster.GetGeoTransform()
rasterCRS = osr.SpatialReference()
rasterCRS.ImportFromWkt(raster.GetProjectionRef())


band = raster.GetRasterBand(Band)
data = band.ReadAsArray() 

# Here calc the index or stats
result = (data - data.min()) / (data.min() + data.max())

# Here make the new raster
array2raster(Output_Raster_Name,
geoTransform,
rasterCRS,
pixelWidth,
pixelHeight,data)
    
