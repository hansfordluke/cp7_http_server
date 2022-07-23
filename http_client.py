import os
os.system("pip3 install requests")

from email import header
from urllib.parse import urlparse
from pip import main
import http.client
import random
import requests
import string

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

def msg_input():
    msg = input("Enter Message: ")
    msg_to_hex = [hex(ord(char)) for char in msg] 
    print(msg_to_hex)
    binaryStr = ' '.join(format(ord(item), 'b') for item in msg)
    return msg_to_hex

def randomised_word(msg_to_hex): #The function responsible for generating the word
    """Function splits the 2 character hex value for each byte and creates a word of length len(hex_char[i]) dynamically"""
    hex_wordlist = []
    for value in msg_to_hex:
        for char in value.split("x")[1]: #Split the string away from the 0x hex indicator
            print(char)
            lowercase_letters = string.ascii_lowercase
            hex_word_length = int(char, 16) #The random length of the word
            hex_word = ''
            while len(hex_word) != hex_word_length: #While loop
                hex_word += random.choice(lowercase_letters) #Selects a random character on each iteration
            hex_wordlist.append(hex_word)
    return hex_word, hex_wordlist #Returns the word

if __name__ == "__main__":
    input = msg_input()
    url = "http://locaLhost:9999/ops/Resource.html"
    base_name, dir_name, res_path = url_splitter(url)
    hex_word, hex_wordlist = randomised_word(input) # words used to represent hex value length from 1-16

    payload = ''    
    for position, hex_word in enumerate(hex_wordlist):
        special_char = ["-", "_", "&", "%", "@", "#", "$", "!"]
        file_type = [".jpg", ".zip", ".txt", ".pdf", ".html"]

        print(position, hex_word)

        if position % 2 == 0:
            payload += hex_word + f"{random.choice(special_char)}"
        else:
            if hex_word == hex_wordlist[-1]:
                payload += hex_word + f"{random.choice(file_type)}"
            else:
                payload += hex_word + "/" 
    
    url = base_name + payload
    
    requests.get(url)
    print(requests.get(url))
    print(url)