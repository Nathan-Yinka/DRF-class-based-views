import requests
# import base64

# username = 'nathan-yinka'
# password = '1234'

# credentials = f"{username}:{password}"
# credentials_base64 = base64.b64encode(credentials.encode()).decode()
# print(credentials_base64)

# headers = {
#     'Authorization': f'Basic {credentials_base64}',
#     'Content-Type': 'application/json',  # Adjust the content type as needed
# }

from getpass import getpass

auth_endpoint = "http://127.0.0.1:8004/api/auth/"
endpoint = 'http://127.0.0.1:8004/api/product'

username = input("Enter your username ")
password = getpass("enter password ")

auth_response = requests.post(auth_endpoint,json={"username":username,"password":password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()["token"]
    headers = {
        "Authorization":"Bearer "+str(token),
    }
    endpoint = 'http://127.0.0.1:8004/api/product'
    get_response = requests.get(endpoint,headers=headers)
    print(get_response.text)
    print("status",get_response.status_code)