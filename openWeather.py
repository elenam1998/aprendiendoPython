#pip install requests
#pip install pprint
#pip install pyown

import requests
from pprint import pprint

city = input('Enter your city : ')

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=b1d4dd23c70a2c7a252d39d4f6fcd29c&units=metric'.format(city)
res = requests.get(url)
data = res.json()

temp=data['main']['temp']
wind_speed=data['wind']['speed']
latitude=data['coord']['lat']
longitude=data['coord']['lon']
description=data['weather'][0]['description']

print('TEMPERATURA : {} grados celsius'.format(temp))
print('VELOCIDAD VIENTO : {} m/s'.format(wind_speed))
print('LATITUD : {}'.format(latitude))
print('LONGITUD : {}'.format(longitude))
print('DESCRIPCION : {}'.format(description))

#TODOS LOS DATOS
#pprint(data)