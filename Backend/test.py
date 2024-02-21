import requests

url = 'http://localhost:8000/charges_api'

data = {
    'age': 19,
    'bmi': 27.9,
    'children': 0
}

response = requests.post(url, json=data)
# response = requests.get('http://localhost:8000/')

print(response.json()['prediction'])