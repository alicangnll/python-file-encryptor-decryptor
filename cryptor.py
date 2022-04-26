#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python File Cryptor/Decryptor
# Picture : https://prnt.sc/Z8JETv4nQEey

import pyAesCrypt, os, string, random, tkinter

bufferSize = 64 * 1024
rnd = random.choices(string.ascii_lowercase)

print("1)Kriptola\n2)Kriptoyu aç")
tip = input()
print("Lütfen dosya/klasor yolunu girin: ")
data = input()
print("Lütfen dosya/klasor şifresini girin: ")
password = input()

# encrypt
def kriptola_dosya(filename):
    pyAesCrypt.encryptFile(filename, "" + str(rnd) + ".crypt", password)
# decrypt
def dekriptola_dosya(filename):
    pyAesCrypt.decryptFile(str(filename), "" + str(filename) + ".out", password)

if(str(tip) == "1"):
    kriptola_dosya(data)
elif(str(tip) == "2"):
    dekriptola_dosya(data)
else:
    print("Yanlış seçim yaptınız!")