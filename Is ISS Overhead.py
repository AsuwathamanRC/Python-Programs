import smtplib
import time
import requests
from datetime import datetime

MY_EMAIL = "YOUR_EMAIL"
MY_PASSWORD = "YOUR_EMAIL_PASSWORD"
MY_LAT = 11.016844
MY_LNG = 76.955833

def is_ISS_OverHead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()  # Throw error when the response code is not OK
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5<=iss_latitude<=MY_LAT+5 and MY_LNG-5<=iss_longitude<=MY_LNG+5:
        return True


def isNight():
    parameters = {
        "lat" : MY_LAT,
        "lng" : MY_LNG,
        "formatted" : 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    hour = datetime.now().hour

    if hour>=sunset and hour<=sunrise:
        return True


while True:
    time.sleep(60)
    if is_ISS_OverHead() and isNight():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )
        print("Success")
