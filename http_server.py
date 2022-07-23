from heapq import _heapify_max
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
        res_parts = res_path.split('.')[0] #removing file enxtension
        hex_words = res_parts.split("/")[1:] #stripping empty first string
        hex_values = []
        for hex_string in hex_words:
            hex_byte_space = re.split("-|_|!|&|%", hex_string)[:2] #Splitting two hex values apart whitespace to give byte representation
            for single_byte in hex_byte_space:
                hex_values.append(len(single_byte)-1)
        byte_rcnstrctd = []
        
        hex_values = []
        for i in range(0,len(hex_values)-1,2):
            value_to_hex1 = hex(hex_values[i]).split("x")[1]
            value_to_hex2 = hex(hex_values[i+1]).split("x")[1]
            byte_rcnstrctd.append(str(value_to_hex1) + str(value_to_hex2))
        for byte in byte_rcnstrctd:
            hex_values.append("0x"+byte)
        print(hex_values)
        # print(hex_bytes)
        # split_res_path = re.split("/|.", res_path)
        #print(split_res_path)

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