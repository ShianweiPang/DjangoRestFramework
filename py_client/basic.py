import requests

# endpoint ="https://httpbin.org/status/200/"
endpoint ="http://localhost:8000/api/"

# HTTP Request get back HTML
# REST API HTTP Request get back JSON
# JSON similar to Python Dictionary

# GET REQUEST
# get_response = requests.get(endpoint, params={'abc':123}, json={'message':"Hii is hunter!"})  # HTTP Request
# print(get_response.json())

# POST REQUEST
get_response = requests.post(endpoint, json={'brand':123})
print(get_response.json())