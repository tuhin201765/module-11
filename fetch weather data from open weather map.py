from requests import get
from pprint import pprint


api_key = 'e95a66dde32f24ded84f58cf264cfa59'
city = 'Dhaka'
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"

res = get(api)
data = res.json()
country = data.get('name')
sys = data.get('sys').get('country')
temp = data.get('main').get('temp')
pressure = data.get('main').get('pressure')
weather = data.get('weather')[0].get('description')
haze = data.get('weather')[0].get('icon')
#
print(sys, weather, haze, temp, pressure)
# pprint(weather)
# pprint(haze)
# pprint(temp)
# pprint(pressure)