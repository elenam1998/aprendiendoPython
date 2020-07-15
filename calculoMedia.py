import numpy 
import rasterio
from rasterio.rio.insp import stats

#CAMBIO EN EL DATATYPE DEL TIF
from PIL import Image
im = Image.open('NDVI_2019_1.tif')
im1 = numpy.array(im).astype(numpy.float32)
im2 = Image.fromarray(numpy.uint8(im1*255))
im2.show()

#ARRAY DE DATOS 
im3 = Image.fromarray(numpy.float32(im2))
#convert
imarray = numpy.array(im3)



###OPCION 1 PARA LA MEDIA CON NUMPY
print("STATS",numpy.min(imarray), numpy.max(imarray), numpy.mean(imarray))
###OPCION 2 PARA LA MEDIA CON RASTERIO
a=rasterio.rio.insp.stats(imarray)
print("estadisticas",a)


#shape, size
#imarray.shape
#im.size


#show
#print ("array", imarray)
#print ("forma array", imarray.shape)
#print ("tamano imagen", im.size)

