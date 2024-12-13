import requests


resp = requests.get('http://192.168.85.91:8000/api/election/get_election/?id=1')

print(resp.json())