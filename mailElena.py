import smtplib

from_addr = 'elenamontesano17@gmail.com'
to = 'elenamontesanomartin@gmail.com'
message = 'This is a test Email from python'

# Reemplaza estos valores con tus credenciales de Google Mail
username = 'elenamontesano17@gmail.com'
password = '*********'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to, message)

server.quit()