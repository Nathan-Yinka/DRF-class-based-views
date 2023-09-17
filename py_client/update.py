import requests

endpoint = "https://httpbin.org/"
endpoint = 'http://127.0.0.1:8004/api/product/3'
data ={
    "title": 'Product1 the updated value'
}
get_response = requests.put(endpoint,json=data)
print(get_response.text)
print("status",get_response.status_code)