from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import json


# Tenemos que empezar con un solo usuario para guardar todos sus datos, hacer todas las operaciones
# y luego avanzar para hacerlo multiusuario

# Importante: No tiene que haber contraseñas escritas en ningún lado (en memoria sí)
# Investigar SALT y Derivación de claves

# El HASH nos sirve como autenticación y para el resumen de toda la información

# PARA EL VIERNES ---> Funciones de cifrado/descifrado (simétrico)
class Alfa():
    def __init__(self):
        user = "María"
    def crearFormulario(self):
        """Función que te crea el usuario y guarda los datos personales CIFRADOS en un archivo JSON"""
        # Usamos AES para beneficiarnos de su rapidez y su fuerza para cirfrar
        print("Introduce tu nombre de usuario: ")
        user_name = input()

        print("Introduce la contraseña: ")
        password = input()

        user_data = {"Usuario": user_name, "Contraseña": password}
        with open('data.json', 'w') as fp:
            json.dump(user_data, fp)

        with open('data.json', 'r') as fp:
            data = json.load(fp)

hola = Alfa()
Alfa.crearFormulario(hola)