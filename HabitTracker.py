from urllib import response
from datetime import datetime
import requests

pixela_endpoint = "https://pixe.la/v1/users"
# token -> User can generate their own token (between 8 to 128 characters in length)
TOKEN = "ENTER_RANDOM_CHARACTERS"
# username -> Unique username
USERNAME = "USERNAME"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Create user
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_header = {
    "X-USER-TOKEN": TOKEN
}
GRAPH_ID = "graph1"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}

# Create Graph
response = requests.post(url=graph_endpoint,headers=graph_header,json=graph_config)
print(response.text)

today = datetime.now().strftime("%Y%m%d")
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": today,
    "quantity": input("How many kilometers did you cycle today?")
}

# Add new pixel data
response = requests.post(url=pixel_creation_endpoint,headers=graph_header,json=pixel_data)
print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
pixel_update_data = {
    "quantity": input(f"How many kilometers did you cycle on {today}?")
}

# Update existing data
response = requests.put(url=pixel_update_endpoint,headers=graph_header,json=pixel_update_data)
print(response.text)

# Delete pixel data
response = requests.delete(url=pixel_update_endpoint,headers=graph_header)
print(response.text)

user_endpoint = f"{pixela_endpoint}/{USERNAME}"
# Delete user
response = requests.delete(url=user_endpoint,headers=graph_header)
print(response.text)