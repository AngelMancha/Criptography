import json

import os
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

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

        personal_data = ["usuario: ", "edad: ", "fecha nacimiento: ", "email: ", "contraseña: "]
        #Le pedimos los datos al usuario

        """
        for i in range(0, len(personal_data)-1):
            print("Introduce tu ", personal_data[i])
            input_text = input()
        """


        print("Introduce el usuario: ")
        user_name = input()

        print("Introduce la contraseña: ")
        password = input()

        # Derivamos una clave de la contraseña que introdujo el usuario
        key = self.derivate_key(password)
        # Usamos AES para beneficiarnos de su rapidez y su fuerza para cirfrar
        # Encriptamos los datos introducidos por el usuario, excepto la contaseña
        user_cif = self.encrypt(key, user_name, None)

        dato_descifrado = self.decrypt(key, None, user_cif[0], user_cif[1], user_cif[2])
        print("ESTO TIENE QUE SER EL USUARIO", dato_descifrado)

        #Hacemos un hash de la contraseña para guardarla en la base de datos
        hashed_password = self.hash_function(password)
        user_data = {"Usuario": str(user_cif), "Contraseña": str(hashed_password)}


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




hola = Alfa()
Alfa.crearFormulario(hola)