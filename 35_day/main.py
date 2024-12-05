# Weather API  ---   9111648e8bbe0ba6f3e54eff0330f3db

import requests


OWM = 'https://api.openweathermap.org/data/2.5/weather'
# API_KEY = '9111648e8bbe0ba6f3e54eff0330f3db'

weather_params = {
    'lat': 6.5244,
    'lon': 3.3792,
    'appid': API_KEY
}

response = requests.get(OWM, params=weather_params)
print(response.status_code)
print(response.json())