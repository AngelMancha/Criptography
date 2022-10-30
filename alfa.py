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
    def __init__(self, nombre, usuario, carrera, asignatura, password):
        self.nombre=nombre
        self.usuario = usuario
        self.carrera = carrera
        self.asignatura = asignatura
        self.password = password

    def cifrardatos(self):
        """Función que te crea el usuario y guarda los datos personales CIFRADOS en un archivo JSON"""



        #Añadimos a la contraseña un salt aleatorio
        salt_function = self.calculate_salt(self.password)
        #Obtenemos la contraseña con el salt añadido
        salt_password = salt_function[1]
        #Y además guardamos el salt por separado en otra variabld
        salt = salt_function[0]
        #Hacemos un hash del salt+contraseña para guardarla en la base de datos
        hashed_password = self.hash_function(salt_password)



        #Derivamos una clave de la contraseña que introdujo el usuario utilizando el salt generado.
        #Esta clave es la clave que vamos a utilizar para el cirfrado y el descrifrado de datos
        salt_bytes=bytes(salt, encoding = 'utf-8')
        key = self.derivate_key(self.password, salt_bytes)
        # Usamos AES para beneficiarnos de su rapidez y su fuerza para cifrar
        # Ciframos los datos introducidos por el usuario con el cifrado simétrico AES, excepto la contaseña
        nombre_cif = self.encrypt(key, self.nombre, None)




        #Guardamos los datos cifrados y el hash de la contraseña junto con el salt en la base de datos (json)
        user_data = {"Usuario": str(self.usuario), "Nombre": str(nombre_cif[1]), "Password": str(hashed_password), "Salt":salt, "iv": str(nombre_cif[0]), "tag": str(nombre_cif[2])}
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

    def derivate_key(self, password, salt):
        byte_password=self.return_bytes(password)
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=390000)
        derivate_key=kdf.derive(byte_password)
        return derivate_key

    def calculate_salt(self, key):
        salt = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        salt_password = salt + key
        return salt, salt_password

    def read_json_file(self, json_file):
        with open(json_file, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def inicio_sesion(self):

        """dato_descifrado = self.decrypt(key, None, user_cif[0], user_cif[1], user_cif[2])
         print("ESTO TIENE QUE SER EL USUARIO", dato_descifrado)
         """
        #json_file = self.read_json_file("data.json")

        print( "\nINICIO DE SESIÓN\n" )



        result = False
        user_name = input(str("Introduce tu nombre de usuario: "))
        while not result:

            with open("data.json", "r", encoding="utf-8") as file:
                usuario = json.load(file)

                json_usuario = usuario["Usuario"]
                json_salt=usuario["Salt"]
                json_iv=usuario["iv"]
                json_tag=usuario["tag"]
                #obtenemos la clave de cifrado y descifrado del usuario acutal en el archivo json
                #json_key = self.derivate_key(user_password, json_salt)
                #result_user=self.decrypt(json_key, None, json_iv,json_user,json_tag)
            if json_usuario == user_name:
                result=True

            if result == False:
                print("EL nombre de usuario introducido no está registrado")
                user_name = input(str("Vuelve a introducir tu nombre de usuario: "))
            else:
                print("El suario exixte")


        result = False
        password_log_in = input("Introduce la contraseña de incio de sesión: ")
        while not result:

            with open('data.json', 'r') as fp:
                data = json.load(fp)
                salt_json = data["Salt"]
            salt_password_log_in = salt_json + password_log_in
            compare1 = self.hash_function(salt_password_log_in)
            with open('data.json', 'r') as fp:
                data = json.load(fp)
                compare2 = data["Password"]

            if str(compare1) == str(compare2):
                result = True

            if result == False:
                print("La contraseña es incorrecta")
                password_log_in = input("Vuelve a introducir la contraseña de inicio de sesión: ")
            else:
                print("¡Bienvenido a ALFA!")

