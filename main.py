from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import json

import os
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)

# Tenemos que empezar con un solo usuario para guardar todos sus datos, hacer todas las operaciones
# y luego avanzar para hacerlo multiusuario

# Importante: No tiene que haber contraseñas escritas en ningún lado (en memoria sí)
# Investigar SALT y Derivación de claves

# El HASH nos sirve como autenticación y para el resumen de toda la información

# PARA EL VIERNES ---> Funciones de cifrado/descifrado (simétrico)
class Alfa():
    def __init__(self):
        pass
    def crearFormulario(self):
        """Función que te crea el usuario y guarda los datos personales CIFRADOS en un archivo JSON"""
        # Usamos AES para beneficiarnos de su rapidez y su fuerza para cirfrar

        #Le pedimos los datos al usuario
        print("Introduce tu nombre de usuario: ")
        user_name = input()

        """
        print("Introduce tu edad: ")
        user_name = input()

        print("Introduce tu fecha de nacimiento: ")
        user_name = input()

        print("Introduce tu email: ")
        user_name = input()
        """
        print("Introduce la contraseña: ")
        password = input()
        key = os.urandom(16) # Le damos al usuario una clave privada para cifrar sus datos personales
        #Ciframos y guardamos los datos en json
        user_cif = self.encrypt(key, user_name, None)
        print(user_cif)
        #user_cif = self.encrypt(edad, password, None)
        #user_cif = self.encrypt(fecha de nacimeinto, password, None)
        #user_cif = self.encrypt(email, None)

        user_data = {"Usuario": str(user_cif), "Contraseña": password}


        with open('data.json', 'w') as fp:
            json.dump(user_data, fp)

        with open('data.json', 'r') as fp:
            data = json.load(fp)



    def encrypt(self, key, plaintext, associated_data: None):
        # Generamos un IV de 96 bits
        iv = os.urandom(12)

       # Construimos un cifrado basado en AES para cifrar con la clave key y la iv calculada anteriormente

        encryptor = Cipher( algorithms.AES(key), modes.GCM(iv),).encryptor()

        #asociamos datos al texto que queremos cifrar para autenticarlo
        #encryptor.authenticate_additional_data(associated_data)

        # Ciframos el texto deseado y lo obtenemos
        b = plaintext.encode('utf-8')
        ciphertext = encryptor.update(b) + encryptor.finalize()
        return ciphertext


    def decrypt(self, key, associated_data, iv, ciphertext, tag):
        """Esta función descrifra """
        # Usamos AES-GCM para poder proporcionar al usuario tanto la confidencialidad de sus datos como su integridad
        # Es por ello que usamos el modo GCM (Galois/Counter Mode)
        decryptor = Cipher(algorithms.AES(key),modes.GCM(iv, tag)).decryptor()

        # We put associated_data back in or the tag will fail to verify
        # when we finalize the decryptor.
        decryptor.authenticate_additional_data(associated_data)

        # Decryption gets us the authenticated plaintext.
        # If the tag does not match an InvalidTag exception will be raised.
        return decryptor.update(ciphertext) + decryptor.finalize()

######################################

hola = Alfa()
Alfa.crearFormulario(hola)