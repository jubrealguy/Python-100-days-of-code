
# ******************** Getting the location of the international space station ******************

# import requests

# response = requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()
# long = data["iss_position"]["longitude"]
# lat = data["iss_position"]["latitude"]

# iss_position = (long, lat)
# print(iss_position)

import requests
from datetime import datetime

MY_LAT = 6.524379
MY_LONG = 3.379206

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

# website to check longitude and longitude of locations - https://www.latlong.net/

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split('T')[1].split(':')[0]
sunset = data["results"]["sunset"].split('T')[1].split(':')[0]

print(sunrise, sunset)

time_now = datetime.now()
print(time_now.hour)