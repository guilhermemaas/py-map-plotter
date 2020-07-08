import requests

url = "https://us1.locationiq.com/v1/search.php"

data = {
    'key': 'c5523cabac6788',
    'q': 'Rua Pomerode, 295, Timbó Brasil',
    'format': 'json'
}

response = requests.get(url, params=data)

print(response.text)