from cgitb import reset
import os
os.system("pip3 install requests")

from email import header
from urllib.parse import urlparse
import http.client
import sys
import requests

from pip import main

#url = "http://mylonelyacejourney.ace"
url = "http://localhost:9999/resource"

def url_splitter(url):
    slashparts = url.split('/')
    base_name = '/'.join(slashparts[:3]) + '/'
    dir_name = '/'.join(slashparts[:-1]) + '/'
    res_path = '/'.join(slashparts[3:]) + '/'
    print('slashparts = %s' % slashparts)
    print('basename = %s' % base_name)
    print('dirname = %s' % dir_name)
    print('res_path = %s' % res_path)

def url_transformation(char):
    if char.isnumeric():
        url = url.capitalise()
        print("int")
    elif char.isalpha():
        url_splitter(url)
        print("alpha")
    else:
        print("spec")

def msg_input():
    msg = input("Enter Message: ")
    binaryStr = ' '.join(format(ord(item), 'b') for item in msg)
    for char in msg:
        if char.isnumeric():
            print("int")
        elif char.isalpha():
            print("alpha")
        else:
            print("spec")
    
    print(msg)
    print(binaryStr)

def run_client(url):
    rqst = requests.get(url)
    # connection = http.client.HTTPConnection("localhost:9999")
    # connection.request("GET", "/")
    # response = rqst.getresponse()
    # print("Status: {} and reason: {}".format(response.status, response.reason))
    print(rqst)
    # connection.close()
    return rqst

if __name__ == "__main__":
    msg_input()
    url = "http://locaLhost:9999/ops/resource.html"
    url_splitter(url)
    run_client(url)