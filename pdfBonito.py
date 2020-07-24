import os

#Librerias reportlab a usar:
from reportlab.platypus import (BaseDocTemplate, Frame, Paragraph, 
                    NextPageTemplate, PageBreak, PageTemplate)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4


#NIVEL 1: CREAMOS LOS CANVAS
#===========================   
#Creamos los canvas para el pie de página y encabezado, que serán fijos
def encabezado(canvas,doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawImage("argon_candidato.jpg", 65, 750, 90, 70)
    canvas.restoreState()
    
def pie(canvas,doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "Page %d" % doc.page)
    canvas.restoreState()

#NIVEL 2: CREAMOS LOS FLOWABLES
#==============================
#Creamos la hoja de Estilo
estilo=getSampleStyleSheet()

#Iniciamos el platypus story
story=[]

#Añadimos al story los flowables. Hay que tener en cuenta que se inicia
#con el primer pageTemplate "UnaColumna"
story.append(Paragraph("Esto es una prueba en la primera pagina", estilo['BodyText']))
                        
#story.append(NextPageTemplate('DosColumnas'))  # Cambio de PageTemplate
story.append(PageBreak())  # Inicio en otra hoja
story.append(Paragraph("Esto es una prueba en la 2ºhoja", estilo['Normal']))
                
#story.append(NextPageTemplate('UnaColumna'))
#story.append(PageBreak())
#story.append(Paragraph("Regresamos al texto del Frame normal del" +\ " pagetemplate de dos columnas", estilo['Normal']))

#NIVEL 3: CREAMOS LOS FRAMES, para luego asignarlos a un pagetemplate.
#===========================
#Frame (x1, y1, ancho, alto, leftPadding=6, bottomPadding=6, rightPadding=6,
# topPadding=6, id=None, showBoundary=0)

#1. Frame que contendrá a toda el contenido de una hoja
frameN = Frame(inch, inch, 451, 697, id='normal')

#2. Frame de columnas
#frame1 = Frame(inch, inch, 220, 697, id='col1')
#rame2 = Frame(inch + 230, inch, 220, 697, id='col2')

#NIVEL 4: CREAMOS LOS PAGETEMPLATE, le asignamos los frames y los canvas
#=================================
#PageTemplate(id=None,frames=[],onPage=_doNothing,onPageEnd=_doNothing)
PTUnaColumna = PageTemplate(id='UnaColumna', frames=frameN, onPage=encabezado, onPageEnd=pie)
#PTDosColumnas =  PageTemplate(id='DosColumnas', frames=[frame1,frame2],
                       # onPage=encabezado, onPageEnd=pie)

#NIVEL 5: CREAMOS EL DOCTEMPLATE, a partir del BaseDocTemplate
#===============================
doc = BaseDocTemplate('test.pdf', pageTemplates=[PTUnaColumna], pagesize=A4)

#Construimos el PDF
doc.build(story)

os.system("test.pdf")
