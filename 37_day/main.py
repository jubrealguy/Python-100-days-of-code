import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'
USERNAME = "jubrealguy"
TOKEN = "iamadeveloper"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

cycling_graph = f"{graph_endpoint}/graph1"

today = datetime.now()
date = today.strftime("%Y%m%d")
print(date)
cycling_config = {
    "date": date,
    "quantity": "25.6"
}

response = requests.post(url=cycling_graph, json=cycling_config, headers=headers)

# #  Deleting an entry / pixel
# cycling_graph = f"{graph_endpoint}/graph1/20250721"
# response = requests.post(url=cycling_graph, headers=headers)
