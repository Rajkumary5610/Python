# Cipher Text programme in python



import random           #importing Modele
import string            #importing Modele

char = " " + string.punctuation + string.digits + string.ascii_letters

char = list(char)
key = char.copy()
random.shuffle(key)
print(f"chars: {char}")
print(f"key:   {key}")

#Encrypt

plain_text = input("Enter the text to be Encrypted: ")
cipher_text = ""

for letter in plain_text:
    index = char.index(letter)
    cipher_text += key[index]

print(f"plain text: {plain_text}")
print(f"Encrypted text: {cipher_text}")

#Decrypt

cipher_text = input("Enter the  text to be Decrypted: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += char[index]

print(f"Encrypted text: {cipher_text}")
print(f"plain text: {plain_text}")





















