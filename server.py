import requests
url = 'http://127.0.0.1:8000'
headers = {
    'Authorization': 'Token ccf4f3c28aa94a670e09c30059cae220de5bee58'
}
r = requests.get(url=url, headers=headers)
data = r.json()
print(data)
