import os
os.system("pip3 install requests")

from email import header
from urllib.parse import urlparse
from pip import main
import http.client
import random
import requests
import string

#url = "http://mylonelyacejourney.ace"
# url = "http://localhost:9999/resource"

def url_splitter(url):
    slashparts = url.split('/')
    base_name = '/'.join(slashparts[:3]) + '/'
    dir_name = '/'.join(slashparts[:-1]) + '/'
    res_path = '/'.join(slashparts[3:]) + '/'
    # print('slashparts = %s' % slashparts)
    # print('basename = %s' % base_name)
    # print('dirname = %s' % dir_name)
    # print('res_path = %s' % res_path)

def msg_input():
    msg = input("Enter Message: ")
    msg_to_hex = [hex(ord(char)) for char in msg] 
    print(msg_to_hex)
    binaryStr = ' '.join(format(ord(item), 'b') for item in msg)
    # for char in msg:
        # if char.isnumeric():
        #     print("int")
        # elif char.isalpha():
        #     # print("alpha")
        # else:
        #     print("spec")
    
    # print(msg)
    # print(binaryStr)
    return msg_to_hex

def randomised_word(msg_to_hex): #The function responsible for generating the word
    """Function splits the 2 character hex value for each byte and creates a word of length len(hex_char[i]) dynamically"""
    random_wordlist = []
    for value in msg_to_hex:
        for char in value.split("x")[1]: #Split the string away from the 0x hex indicator
            print(char)
            lowercase_letters = string.ascii_lowercase
            lowercase_word = '' #The variable which will hold the random word
            random_word_length = int(char, 16) #The random length of the word
            word = ''
            while len(word) != random_word_length: #While loop
                word += random.choice(lowercase_letters) #Selects a random character on each iteration
            random_wordlist.append(word)
    return word, random_wordlist #Returns the word

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
    input = msg_input()
    url = "http://locaLhost:9999/ops/Resource.html"
    url_splitter(url)
    run_client(url)
    random_word, random_wordlist = randomised_word(input)
    print(random_word)
    print(random_wordlist)