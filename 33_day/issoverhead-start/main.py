import requests
from datetime import datetime
import smtplib
import time

my_email = "oladimeji12344321@gmail.com"
password = "zpmhmouwarbqbhom"

MY_LAT = 6.524379
MY_LONG = 3.379206

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # print(iss_latitude, iss_longitude)
    # print(abs(iss_longitude - MY_LONG))
    # print(abs(iss_latitude - MY_LAT))
    if abs(iss_longitude - MY_LONG) < 5 and abs(iss_latitude - MY_LAT) < 5:
        return True

is_iss_overhead()

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split('T')[1].split(':')[0])
    sunset = int(data["results"]["sunset"].split('T')[1].split(':')[0])


    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60) 
    if is_iss_overhead() and is_night():
        print('go outside')
        try:
            # Use SMTP_SSL for port 465
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email, 
                    to_addrs="oladimeji12344321@yahoo.com", 
                    msg="Subject:Look up\n\nThe iss is above you in the sky")
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")
    else:
        print('stay inside')


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



