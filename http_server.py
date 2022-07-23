from http import server
from http.server import HTTPServer, BaseHTTPRequestHandler
from re import L

HOST = "localhost"
PORT = 9999

class TestHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>HELLO WORLD!</h1></body></html>", "utf-8"))



server = HTTPServer((HOST, PORT), TestHTTP)
print("Server running...")
server.serve_forever()
server.server_close()