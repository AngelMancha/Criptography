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
        carrera_cif = self.encrypt(key, self.carrera, None)
        asignatura_cif = self.encrypt(key, self.asignatura, None)

        #Rellenamos el archivo json con los datos de los alumnos que se van a registrar
        user_data = {"Usuario": str(self.usuario), "Nombre": str(nombre_cif[1]), "Carrera": str(carrera_cif[1]), 
                     "Asignatura": (asignatura_cif[1]).decode('latin-1'), "Password": str(hashed_password), "Salt": salt,
                     "iv": (asignatura_cif[0]).decode('latin-1'), "tag": (asignatura_cif[2]).decode('latin-1')}

        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            data.append(user_data)
        with open("data.json", "w", encoding="utf-8", newline="") as file:
            json.dump(data, file, indent=2)





    def encrypt(self, key, plaintext, associated_data: None):
        """Función que implementa AES y cifra los datos con la clave "Key" """
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
        """Función que descifra los datos utilizando la clave "key" """
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
        """Función que calcula un hash de la contraseña"""
        hashed_key = hashes.Hash(hashes.SHA256())
        byte_hash_key = self.return_bytes(key)
        hashed_key.update(byte_hash_key)
        hashed_key.copy()
        return hashed_key.finalize()

    def return_bytes(self, key):
        """Función para transformar a bytes una cadena de string"""
        return bytes(key, encoding = 'utf-8')

    def derivate_key(self, password, salt):
        """Función para obtener una clave derivada a partir de la contraseña"""
        byte_password=self.return_bytes(password)
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=390000)
        derivate_key=kdf.derive(byte_password)
        return derivate_key

    def calculate_salt(self, key):
        """Función para calcular un salt aleatorio"""
        salt = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        salt_password = salt + key
        return salt, salt_password

    def read_json_file(self, json_file):
        "Función para abrir el archivo json donde están los alumnos resgistrados"
        with open(json_file, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def inicio_sesion(self):
        """Función para la implementación del inicio de sesión. Comprueba que el usuario esté registrado
        y en caso de que lo esté le pide la contraseña al usuario. Si es correcta le da la bienvenida a la aplicacion"""


        print( "\nINICIO DE SESIÓN\n" )

        json_file = self.read_json_file("data.json")

        user_exists = False
        user_name = input(str("Introduce tu nombre de usuario: "))
        #Este bucle se ejectua hasta que se encuentre en la base de datos el nombre de usuario
        #que ha introducido el alumno
        while not user_exists:
            #Para ello buscamos entre todos los alumnos registrados en la base de datos (json)
            for usuario in json_file:

                if usuario["Usuario"] == user_name:
                     user_exists=True

            #Si una vez iterada toda la base de datos no hay ningún nombre de usuario que
            #coincida, se le pregunta al usuario si quiere volver a introducir otro nombre de
            #usuario o terminar con la operación
            if user_exists == False:
                print("EL nombre de usuario introducido no está registrado")
                continue_var=input("¿Quieres volver a intentarlo? [y/n]")
                if continue_var == "n":
                    break
                user_name = input(str("Vuelve a introducir tu nombre de usuario: "))
            #Si se ha encontrado el usuario en la base de datos:
            else:
                print("El suario exixte")


        #Solo si el usuario existe, el usuario le pedirá que introduzca la contraseña
        #asociada a ese usuario
        if user_exists:
            correct_password=False
            password_log_in = input("Introduce la contraseña de incio de sesión: ")
            while not correct_password:

                for usuario in json_file:

                    if  usuario["Usuario"] == user_name:
                        #1: obtiene el salt asociado a el usuario
                        salt_json = usuario["Salt"]
                        #2: se lo añade a la contraseña que ha introducido el usuario ahora
                        salt_password_log_in = salt_json + password_log_in
                        #3: le calcula el hash a la contraseña que ha introducido el usuario más el salt
                        compare1 = self.hash_function(salt_password_log_in)
                        #4: comparamos el hash calculado ahora con el guardado para ese usuario en la base de datos:
                        compare2 = usuario["Password"]


                if str(compare1) == str(compare2):
                    correct_password = True
                #si no coinciden el sistema le vuelve a pedir la contraseña
                if correct_password == False:
                    print("La contraseña es incorrecta")
                    password_log_in = input("Vuelve a introducir la contraseña de inicio de sesión: ")
                # si coinciden hambos hashes
                else:
                    print("¡Bienvenido a ALFA!")


                    question = input("¿Deseas  obtener la asignatura en la que estás matriculado?")
                    if question == "y" or question == "Y":
                        for usuario in json_file:

                            if usuario["Usuario"] == user_name:
                                salt_json = usuario["Salt"]
                                salt_json_bytes = self.return_bytes(salt_json)

                                iv_json = usuario["iv"]
                                iv_json_bytes = iv_json.encode('latin-1')

                                tag_json = usuario["tag"]
                                tag_json_bytes = tag_json.encode('latin-1')

                                key_descif=self.derivate_key(password_log_in, salt_json_bytes)

                                asignatura_cif=usuario["Asignatura"]
                                asignatura_cif_bytes=asignatura_cif.encode('latin-1')


                                asignatura_descif=self.decrypt(key_descif, None, iv_json_bytes ,asignatura_cif_bytes , tag_json_bytes)

                        print("El usuario ",user_name, "está matriculado en la asignatura " , asignatura_descif.decode())








