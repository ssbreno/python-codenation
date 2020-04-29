import requests
import sys
import hashlib
import json
import os
from flask import Flask, request, render_template

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ROT = 9

def cipher(message, dir):
    m = ''
    for c in message:
        if c in ALPHABET:
            c_index = ALPHABET.index(c)
            m += ALPHABET[(c_index + (dir * ROT)) % len(ALPHABET)]
        else:
            m += c
    return m

def encrypt(message):
    return cipher(message, 1)

def decrypt(message):
    return cipher(message, -1)

def resumo_sha1(message):
    with open(message, 'r') as arq:
        data = json.load(arq)
        encoding = arq.encoding
    resumo = hashlib.sha1(data['decifrado'].encode(encoding)).hexdigest()
    data['resumo_criptografico'] = resumo
    print(resumo)

    with open(message, 'w') as arq:
        json.dump(data, arq)


def send_formdata(message):
    API_URL = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=1a03d7e86615a1fc7d41d263bcd919e0c47ce1aa"
    filepath = "D:\\Repositorios\\request_codenation\\answer.json"
    try:
        files = { 'answer' : open(filepath, "rb") }
        req = requests.post(API_URL, files=files)
        print(req.status_code)
        print(req.text)
    except Exception as e:
            print ("Exception:", e)



def main():
    command = sys.argv[1].lower()
    message = sys.argv[2].lower()

    if command == 'encrypt':
       print(encrypt(message))
    elif command == 'decrypt':
       print(decrypt(message))
    elif command == 'resumosha1':
       resumo_sha1(message)
    elif command == 'send_formdata':
       send_formdata(message)
    else:
        print(command + (' -> command not found'))

if __name__ == '__main__':
    main()