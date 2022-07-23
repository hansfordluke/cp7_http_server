import os
os.system("pip install requests")
os.system("pip install requests_toolbelt")

from http import server
from http.server import HTTPServer, BaseHTTPRequestHandler
from re import L
import http.server
from requests_toolbelt.utils import dump
import requests

HOST = "localhost"
PORT = 9999

class TestHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(404)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body><h1>HELLO WORLD!</h1></body></html>", "utf-8"))

    
server = HTTPServer((HOST, PORT), TestHTTP)
# response = requests.Request('POST', "http://localhost:9999")

resp = requests.get('http://localhost:9999')
data = dump.dump_all(resp)
print(data.decode('utf-8'))

print("Server running...")
# print(response.url)
server.serve_forever()
server.server_close()