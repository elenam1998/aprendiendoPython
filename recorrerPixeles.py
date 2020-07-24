import numpy 
import rasterio
from rasterio.rio.insp import stats
import matplotlib
#CAMBIO EN EL DATATYPE DEL TIF
from PIL import Image
im = Image.open('NDVI_2019_1.tif')
im1 = numpy.array(im).astype(numpy.float32)
im2 = Image.fromarray(numpy.uint8(im1*255))
im2.show()

#ARRAY DE DATOS 
im3 = Image.fromarray(numpy.float32(im2))
#convert
imarray = numpy.array(im1)


for row in imarray:
    for cell in row:
        print(cell, end=' ')
