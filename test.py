import requests
import jsonpointer
BASE = "http://127.0.0.1:5000/"

data = {"likes": 10, "name": "Tim", "views": 22}

response = requests.put(BASE + "video/1", jaon)

print(response.json())