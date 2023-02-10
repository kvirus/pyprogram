from PIL import Image
import requests
from io import BytesIO
import json

params = {
  'access_key': '5ab3b5fec6098aa60ad49f260e46316a',
  'query': 'Rostov'
}

api_result = requests.get('http://api.weatherstack.com/current', params)

x=api_result.json()
y=x['current']['weather_icons']
z=str(y)
z1=z[2:]
print(z1)

print('Город',x['location']['name'])
print('Время',x['location']['localtime'])
print('Температура',x['current']['temperature'])
print('Облачность',x['current']['weather_descriptions'])
print('Скорость ветра',x['current']['wind_speed'])
print('Влажность',x['current']['humidity'])
print('Ощущяется как',x['current']['feelslike'])


