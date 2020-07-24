import numpy 
import rasterio
from rasterio.rio.insp import stats

#open
from PIL import Image
im = Image.open('NDVI_2019_1.tif')
im1 = numpy.array(im).astype(numpy.float32)
im2 = Image.fromarray(numpy.uint8(im1*255))
im2.show()

#array de datos
im3 = Image.fromarray(numpy.float32(im2))
#convert
imarray = numpy.array(im3)

###OPCION 1 CON NUMPY
print("STATS",numpy.min(imarray), numpy.max(imarray), numpy.mean(imarray))
###OPCION 2 CON RASTERIO
a=rasterio.rio.insp.stats(imarray)
print("estadisticas",a)
#shape, size
imarray.shape
im.size


#show
print ("array", imarray)
print ("forma array", imarray.shape)
print ("tamano imagen", im.size)

#Dejar de ser array para volver a ser imagen TIFF
#Image.fromarray(imarray)