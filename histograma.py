import numpy 
import rasterio
from rasterio.plot import show_hist
import matplotlib.pyplot as plt
from PIL import Image

#CAMBIO EN EL DATATYPE DEL TIF

def TiffToNumpyArrays(OpenedImage):
    imgArrayFloat32 = numpy.array(OpenedImage).astype(numpy.float32)
    imgArrayUINT8 = Image.fromarray(numpy.uint8(imgArrayFloat32*255))
    imgFloat32 = Image.fromarray(numpy.float32(imgArrayUINT8))
    # convert (para la media, minimo y máximo, trabaja de 0-1, que es en lo que está mi imagen .tif)
    imgArray_1 = numpy.array(imgArrayFloat32)
    #convert (para la lista de pixeles que me va a dar la moda, trabaja de 0-255 y luego ya lo devolvemos a 0-1)
    imgArray_255 = numpy.array(imgFloat32)
    #imgArrayUINT8.show()
    return imgArray_1, imgArray_255


def calculateHistogramAndParameters(imagePath):
    OpenedImage = Image.open(imagePath)
    RasterioOpenedImage = rasterio.open(imagePath)

    sep = int(input("Introduzca 0 si quiere separaciones fijas o marque 1 si quiere porcentuales para el histograma "))
    imgArray_1, imgArray_255 = TiffToNumpyArrays(OpenedImage)

    #para el histograma
    #bins son las separaciones
    #lw es el ancho de línea, stacked false es para que no se apilen unos encima de otro,Alpha y steptfilled
    # van vinculados, el segundo es para superponer histogramas por si hay mas de uno y el
    # alpha es el grado de transparencia

    #separaciones fijas
    if sep == 0:
        s = float(input("¿Cada cuanto quiere las separaciones? "))
        div = (numpy.nanmax(imgArray_1)-numpy.nanmin(imgArray_1))//s
        div2 = round(div, 2)
        div3 = int(div2)
        #Para guardar el histograma en png
        fig, axh = plt.subplots()
        show_hist(RasterioOpenedImage, bins=div3, lw=0.0, stacked=False, alpha=0.3,
                  histtype='stepfilled', title="Histogram", ax=axh)
        fig.savefig('Histograma.png')
        #separaciones porcentuales
    elif sep == 1:
        nm = int(input("¿Cúantas separaciones quiere en el histograma? "))
        #Para guardar el histograma en png
        fig, axh = plt.subplots()
        show_hist(RasterioOpenedImage, bins=nm, lw=0.0, stacked=False, alpha=0.3,
                  histtype='stepfilled', title="Histogram", ax=axh)
        fig.savefig('Histograma.png')
    
    #SACAR MODA
    listaPixeles = list()
    for row in imgArray_255:
        for cell in row:
            if cell > 0.0:
                listaPixeles.append(cell)

    #FILTRADO CON LA FÓRMULA --> MEDIA - 2*DESV.ESTANDAR
    minimo      = numpy.nanmin(imgArray_1)
    maximo      = numpy.nanmax(imgArray_1)
    media       = numpy.nanmean(imgArray_1)
    desviacion  = numpy.nanstd(imgArray_1)
    moda = max(set(listaPixeles), key=listaPixeles.count)/255
    Kcp = numpy.nanmean(imgArray_1)*1.25
    Kc = Kcp + 0.1

    return minimo, maximo, media, desviacion, moda, Kc, imgArray_1, imgArray_255


#############################################################
#Main code


minValue, maxValue, average, std, mod, kc, ImgArray_0_1, ImgArray_0_255 = calculateHistogramAndParameters(
    'NDVI_2019_1.tif')



#SACAR MINIMO, MAXIMO Y MEDIA (ignoramos los valores nan, si trabajasemos de 0-255 los nan se convierten en 0.0)
print("MINIMO", minValue)
print("MAXIMO", maxValue)
print("MEDIA", average)
print("DESVIACIÓN ESTANDAR", std)
print("TAM", ImgArray_0_1.shape)

#descarta = mod*0.8
descarta = average - 2*std
print("descarta",descarta)
#descarto los mayores 
listaPixeles=list()
for row in ImgArray_0_1:
    for cell in row:
        if cell > descarta:
            cell=0.0
            listaPixeles.append(cell) 
        else:
            listaPixeles.append(cell) 
        #print(cell, end=' ')

imagenVector=numpy.asarray(listaPixeles,dtype=numpy.float32) 
imagenVector2 = imagenVector.reshape(ImgArray_0_1.shape)
imfin = Image.fromarray(numpy.uint8(imagenVector2*255))
imfin2 = Image.fromarray(numpy.float32(imfin))
#los valores totalmente negros (0.0) son los que son correctos, hay que mejorar los otros
imfin2.show()

#EXPORTAR NUEVO TIFF
imagen_filtrada = Image.fromarray(numpy.float32(imfin))
imagen_filtrada.save("ENERO_FILTRADO.tiff")
