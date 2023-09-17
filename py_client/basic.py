import requests

endpoint = "https://httpbin.org/"
endpoint = 'http://127.0.0.1:8004/api'

get_response = requests.post(endpoint,json={"query":"name"})
print(get_response.text)
print("status",get_response.status_code)