import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()  # Throw error when the response code is not OK

data = response.json()

latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

issPosition = (latitude,longitude)

print(f"The ISS is currently in {issPosition}")