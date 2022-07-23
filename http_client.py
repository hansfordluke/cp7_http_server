import os
os.system("pip install requests")
os.system("pip install curses")

from email import header
import http.client
import sys
import requests

from pip import main

def url_transformation(char):
    

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

def run_client(URL):
    rqst = requests.get(URL)
    # connection = http.client.HTTPConnection("localhost:9999")
    # connection.request("GET", "/")
    # response = rqst.getresponse()
    # print("Status: {} and reason: {}".format(response.status, response.reason))
    print(rqst)
    # connection.close()
    return rqst

if __name__ == "__main__":
    msg_input()
    URL = "http://localhost:9999"
    run_client(URL)
