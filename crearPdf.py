from reportlab.pdfgen import canvas
c=canvas.Canvas("hola mundo.pdf")

# Dibujamos una imagen (IMAGEN, X,Y, WIDTH, HEIGH)
c.drawImage("argon_candidato.jpg", 30, 750, 90, 70)
#c.showPage()

c.drawString(100,730, "HOLA MUNDO")

c.setLineWidth(.3)
c.setFont('Helvetica', 12)
 
c.drawString(450,785,"AGRON & NOMO")

  
c.line(30,765,550,765)

c.save()