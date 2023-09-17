import requests

data ={
    "title": 'Product1'
}
get_response = requests.post(endpoint,json=data)
print(get_response.text)
print("status",get_response.status_code)