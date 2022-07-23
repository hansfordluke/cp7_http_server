import http.client

connection = http.client.HTTPConnection("localhost:9999")
connection.request("GET", "/")
response = connection.getresponse()
print("Status: {} and reason: {}".format(response.status, response.reason))

connection.close()