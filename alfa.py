import json
import random
import os
import string
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Alfa():
    def __init__(self, usuario, carrera, asignatura, password):
        self.usuario = usuario
        self.carrera = carrera
        self.asignatura = asignatura
        self.password = password

    def cifrardatos(self):
        """Función que te crea el usuario y guarda los datos personales CIFRADOS en un archivo JSON"""
        # Derivamos una clave de la contraseña que introdujo el usuario
        key = self.derivate_key(self.password)
        # Usamos AES para beneficiarnos de su rapidez y su fuerza para cifrar
        # Ciframos los datos introducidos por el usuario con el cifrado simétrico AES, excepto la contaseña
        user_cif = self.encrypt(key, self.usuario, None)

        #Añadimos a la contraseña un salt aleatorio
        salt_function = self.calculate_salt(self.password)
        salt_password = salt_function[1]
        salt = salt_function[0]
        #Hacemos un hash del salt+contraseña para guardarla en la base de datos
        hashed_password = self.hash_function(salt_password)


        #Guardamos los datos cifrados y el hash de la contraseña junto con el salt en la base de datos (json)
        user_data = {"Usuario": str(user_cif), "Password": str(hashed_password), "Salt":salt}
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
        return iv, ciphertext, encryptor.tag


    def decrypt(self, key, associated_data, iv, ciphertext, tag):
        """Esta función descrifra """
        # Usamos AES-GCM para poder proporcionar al usuario tanto la confidencialidad de sus datos como su integridad
        # Es por ello que usamos el modo GCM (Galois/Counter Mode)
        decryptor = Cipher(algorithms.AES(key),modes.GCM(iv, tag)).decryptor()

        # We put associated_data back in or the tag will fail to verify
        # when we finalize the decryptor.
        #decryptor.authenticate_additional_data(associated_data)

        # Decryption gets us the authenticated plaintext.
        # If the tag does not match an InvalidTag exception will be raised.
        return decryptor.update(ciphertext) + decryptor.finalize()


    def hash_function(self, key):
        hashed_key = hashes.Hash(hashes.SHA256())
        byte_hash_key = self.return_bytes(key)
        hashed_key.update(byte_hash_key)
        hashed_key.copy()
        return hashed_key.finalize()

    def return_bytes(self, key):
        return bytes(key, encoding = 'utf-8')

    def derivate_key(self, password):
        byte_password=self.return_bytes(password)
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=390000)
        derivate_key=kdf.derive(byte_password)
        return derivate_key

    def calculate_salt(self, key):
        salt = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        salt_password = salt + key
        return salt, salt_password
