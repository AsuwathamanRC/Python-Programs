import requests
import smtplib
from twilio.rest import Client

API_KEY = "OPEN_WEATHER_MAP_API"
LATITUDE = "11.108524"
LONGITUDE = "77.341064" #Tiruppur

account_sid = 'TWILIO_ACCOUNT_SID'
auth_token = 'TWILIO_AUTH_TOKEN'
from_number = 'TWILIO_TRIAL_NUMBER'
to_number = 'TWILIO_VERIFIED_MOBILE_NUMBER'

my_email = "YOUR_EMAIL"
password = "YOUR_EMAIL_PASSWORD"
receiver_mail = "RECEIVER_EMAIL"

parameters = {
    "lat" : LATITUDE,
    "lon" : LONGITUDE,
    "exclude" : "current,minutely,daily",
    "appid" : API_KEY
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall",params=parameters)
response.raise_for_status()  # Throw error when the response code is not OK

data = response.json()

umbrellaRequired = False

for i in range(0,12):
    weatherCode = data["hourly"][i]["weather"][0]["id"]
    if weatherCode<700:
        umbrellaRequired = True

if umbrellaRequired:

    body = "It's going to rain today🌦️. Remember to bring an Umbrella☔"

    # Send SMS
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body=body,
                        from_=from_number,
                        to=to_number
                    )
    
    # Send Mail
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email,password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=receiver_mail,
                msg=f"Subject:Today's Weather Report!\n\n{body}"
            )