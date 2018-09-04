import requests

response=requests.get('http://api.forismatic.com/api/1.0/')
print(response)
print(response.status_code)
print(response.content)
