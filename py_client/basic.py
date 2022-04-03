import requests

# endpoint ="https://httpbin.org/status/200/"
endpoint ="http://localhost:8000/api/"

# HTTP Request get back HTML
# REST API HTTP Request get back JSON
# JSON similar to Python Dictionary

get_response = requests.get(endpoint)  # HTTP Request
print(get_response.json()['message'])