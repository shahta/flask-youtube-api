import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + 'video/10', {'name': 'Hi', 'likes': 4000, 'views': 1000})
print(response.json())

input()

response = requests.get(BASE + 'video/8')
print(response.json())

