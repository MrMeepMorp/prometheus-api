import requests

url = "https://prometheus-api-mchv.onrender.com/generate-cnc"
payload = {"prompt": "a beautiful captive prince, trembling in chains"}
res = requests.post(url, json=payload)
print(res.json())
