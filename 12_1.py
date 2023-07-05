import requests
from datetime import datetime  # библиотека для http запросов

town = input('введите город: ')

key = '06d3cdd940dbee91c85e8dedf7a91f78'
url = 'https://api.openweathermap.org/data/2.5/weather'
params = {'APPID': key, 'q': 'Moscow', 'units': 'metric'}

request = requests.get(url, params=params)

result = request.json()
code = result['cod']

if code != 401:
    if code !=404:

# print(result)

#{'coord': {'lon': 37.6156, 'lat': 55.7522},
# 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}],
# 'base': 'stations', 'main': {'temp': 25.73, 'feels_like': 25.19, 'temp_min': 25.24,
# 'temp_max': 26.29, 'pressure': 1015, 'humidity': 32, 'sea_level': 1015, 'grnd_level': 998},
# 'visibility': 10000, 'wind': {'speed': 4.96, 'deg': 209, 'gust': 6}, '
# clouds': {'all': 20}, 'dt': 1688474614,
# 'sys': {'type': 2, 'id': 47754, 'country': 'RU', 'sunrise': 1688431913, 'sunset': 1688494529},
# 'timezone': 10800, 'id': 524901, 'name': 'Moscow', 'cod': 200}

# 'cod': 200 - все выдано в полном объеме
# 'cod': 404 -страницы не существует - его нужно вносить в try
# 'cod': 301 - страницы не определена (перенесена)
# 'cod': 200 - вы не авторизованы (ключ неверный)

        print(result['main'])
        # {'temp': 25.73, 'feels_like': 25.19, 'temp_min': 25.24, 'temp_max': 26.29, 'pressure': 1015, 'humidity': 32, 'sea_level': 1015, 'grnd_level': 998}
        data = result['main']
        print(f'Температура: {data["temp"]:.1f}\xB0C')
        # Температура: 25.8°C
        print(f'Влажность:', data['humidity'],'%')
        # Влажность: 32 %
        raw_time_sunset = result['sys']['sunset']
        print(datetime.utcfromtimestamp(raw_time_sunset).strftime("%H:%M"))
        # 18:15
        print(f'Координаты: {result["coord"]["lon"]}, {result["coord"]["lat"]}')
      #  if result['weather'] ==

        # Координаты: 37.6156, 55.7522
        print(result ['weather'][0]['main'])
        # Clouds
else:
    print('Информации нет')

