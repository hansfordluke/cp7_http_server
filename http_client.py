import os
os.system("pip3 install requests")

from email import header
from urllib.parse import urlparse
import http.client
import sys
import requests

from pip import main

#url = "http://mylonelyacejourney.ace"
url = "http://localhost:9999"

def url_splitter(url):
    # Create a list of each bit between slashes
    slashparts = url.split('/')
    # Now join back the first three sections 'http:', '' and 'example.com'
    basename = '/'.join(slashparts[:3]) + '/'
    # All except the last one
    dirname = '/'.join(slashparts[:-1]) + '/'
    print('slashparts = %s' % slashparts)
    print('basename = %s' % basename)
    print('dirname = %s' % dirname)

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
    url = "http://localhost:9999"
    url_splitter(url)
    run_client(url)