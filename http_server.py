import os
os.system("pip install requests")

from http import server
from http.server import HTTPServer, BaseHTTPRequestHandler
from re import L
import re

HOST = "localhost"
PORT = 9999

class TestHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        res_path = str(self.path)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body><h1>HELLO WORLD!</h1></body></html>", "utf-8"))
        res_parts = res_path.split('.')[0]
        #print(res_parts)
        byte_parts = [part.split("/") for part in res_parts]
        print(byte_parts)
        # split_res_path = re.split("/|.", res_path)
        #print(split_res_path)
        return res_path

def urn_path_parser(urn_path):
    split_path = urn_path.split("/")
    split_path = [path.strip() for path in split_path]
    print(split_path)

def url_splitter(url):
    slashparts = url.split('/')
    base_name = '/'.join(slashparts[:3]) + '/'
    dir_name = '/'.join(slashparts[:-1]) + '/'
    res_path = '/'.join(slashparts[3:]) + '/'
    return base_name, dir_name, res_path
    # print('slashparts = %s' % slashparts)
    # print('basename = %s' % base_name)
    # print('dirname = %s' % dir_name)
    # print('res_path = %s' % res_path)


server = HTTPServer((HOST, PORT), TestHTTP)
print("Server running...")
#urn_path_parser(TestHTTP.urn_path)
server.serve_forever()
server.server_close()