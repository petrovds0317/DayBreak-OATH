import requests

url = "http://127.0.0.1:5002/auth"
d = {}

response = requests.get(url, json=d)
print(response.text)