import requests

payload = {"URL_addition": "Ouch"}
r = requests.get("http://httpbin.org/get", params = payload)
print(r.url)