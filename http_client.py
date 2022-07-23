import os
os.system("pip install requests")

from email import header
import http.client
import sys
import requests

from pip import main

def msg_input():
    msg = input("Enter Message: ")
    print(msg)

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
