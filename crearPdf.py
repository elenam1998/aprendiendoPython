from reportlab.pdfgen import canvas
from reportlab.platypus import (BaseDocTemplate, Frame, Paragraph, 
                    NextPageTemplate, PageBreak, PageTemplate)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
c=canvas.Canvas("hola mundo.pdf")
def encabezado(canvas,doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawImage("nomoLogo.png", 410, 750, 150, 70)
    canvas.restoreState()
# Dibujamos una imagen (IMAGEN, X,Y, WIDTH, HEIGH)
c.drawImage("nomoLogo.png", 30, 450, 150, 70)
frameN = Frame(inch, inch, 451, 697, id='normal')
PTUnaColumna = PageTemplate(id='UnaColumna', frames=frameN, onPage=encabezado)

c.save()