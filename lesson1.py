import requests
from requests.auth import HTTPBasicAuth

response = requests.get(
    url="https://petstore.swagger.io/v2/pet/findByStatus",
    # auth=HTTPBasicAuth("username", "password")
    headers={
        "api_key": "special-key"
    },
    params={
        "status":"sold"
    },
    # verify=False
)
response = response.json()
print(response)
