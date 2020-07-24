import numpy 
import rasterio
from rasterio.plot import show_hist
import matplotlib.pyplot as plt

#CAMBIO EN EL DATATYPE DEL TIF
from PIL import Image
im = Image.open('NDVI_2019_1.tif')
im1 = numpy.array(im).astype(numpy.float32)
im2 = Image.fromarray(numpy.uint8(im1*255))
im3 = Image.fromarray(numpy.float32(im2))
#convert (para la media, minimo y máximo, trabaja de 0-1, que es en lo que está mi imagen .tif)
imarray = numpy.array(im1)
#convert (para la lista de pixeles que me va a dar la moda, trabaja de 0-255 y luego ya lo devolvemos a 0-1)
imarray2 = numpy.array(im3)
im2.show()

#HISTOGRAMA

#bins son las separaciones
#lw es el ancho de línea, stacked false es para que no se apilen unos encima de otro,Alpha y steptfilled
# van vinculados, el segundo es para superponer histogramas por si hay mas de uno y el 
# alpha es el grado de transparencia
src=rasterio.open('NDVI_2019_1.tif')

sep= int(input("Introduzca 0 si quiere separaciones fijas o marque 1 si quiere porcentuales para el histograma "))

#separaciones fijas
if sep == 0:
    s= float(input("¿Cada cuanto quiere las separaciones? "))
    div=(numpy.nanmax(imarray)-numpy.nanmin(imarray))//s
    div2=round(div,2)
    div3=int(div2)
    #Para guardar el histograma en png
    fig, axh = plt.subplots()
    show_hist (src, bins=div3, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Histogram", ax=axh)
    fig.savefig('Histograma.png')

#separaciones porcentuales
if sep == 1:
    nm= int(input("¿Cúantas separaciones quiere en el histograma? "))
     #Para guardar el histograma en png
    fig, axh = plt.subplots()
    show_hist( src, bins=nm, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Histogram", ax=axh)
    fig.savefig('Histograma.png')
    


#SACAR MINIMO, MAXIMO Y MEDIA (ignoramos los valores nan, si trabajasemos de 0-255 los nan se convierten en 0.0)
print("MINIMO",numpy.nanmin(imarray)) 
print("MAXIMO", numpy.nanmax(imarray))
print("MEDIA", numpy.nanmean(imarray))
imarray.shape
print("TAM", imarray.shape)

#SACAR MODA
listaPixeles=list()
for row in imarray2:
    for cell in row:
        if cell > 0.0:
            listaPixeles.append(cell)        
print("La moda es:")
print(max(set(listaPixeles), key = listaPixeles.count)/255)

#CALCULO DE LA KC
Kcp = numpy.nanmean(imarray)*1.25
Kc = Kcp + 0.1
print("La Kc es de ", Kc)

#20% POR DEBAJO DE LA MODA 
descarta=(max(set(listaPixeles), key = listaPixeles.count)/255)*0.8
print("descarta",descarta)

#descarto los mayores 
listaPixeles2=list()
for row in imarray:
    for cell in row:
        if cell > descarta:
            cell=0.0
            listaPixeles2.append(cell) 
        else:
            listaPixeles2.append(cell) 
        #print(cell, end=' ')

imagenVector=numpy.asarray(listaPixeles2,dtype=numpy.float32) 
imagenVector2=imagenVector.reshape(imarray.shape)
imfin = Image.fromarray(numpy.uint8(imagenVector2*255))
imfin2 = Image.fromarray(numpy.float32(imfin))
#los valores totalmente negros (0.0) son los que son correctos, hay que mejorar los otros
imfin2.show()

#EXPORTAR NUEVO TIFF
imagen_filtrada = Image.fromarray(numpy.float32(imfin))
imagen_filtrada.save("ENERO_FILTRADO.tiff")
