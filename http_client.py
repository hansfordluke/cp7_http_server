import os
os.system("pip3 install requests")

import random
import requests
import string

def msg_input():
    msg = input("Enter Message: ")
    msg_to_hex = [hex(ord(char)) for char in msg] 
    print(f"{msg} in hex bytes:", msg_to_hex)
    return msg_to_hex

def randomised_word(msg_to_hex): #The function responsible for generating the word
    """Function splits the 2 character hex value for each byte and creates a word of length len(hex_char[i]) dynamically"""
    hex_wordlist = []
    for value in msg_to_hex:
        hex_values = value.split("x")[1]
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
    input = msg_input()
    hex_word, hex_wordlist = randomised_word(input) # words used to represent hex value length from 1-16
    payload = ''    
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

    base_name = "http://locaLhost:9999/"
    url = base_name + payload 
    requests.get(url)
    print(requests.get(url))
    print(url)