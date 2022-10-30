from alfa import Alfa
from registro import Registro

if __name__ == "__main__":
    print("Hola!")

    end = False
    while not end:
        question = input("¿Deseas iniciar sesión [A] o Registrarte [B] o salir [x]?")
        if question == "A" or question == "a":
            log_alfa= Alfa(None, None, None, None, None)
            log_user = log_alfa.inicio_sesion()
        elif question == "B" or question == "b":
            registrar_alumno = Registro()
            alumno_registrado = registrar_alumno.registrar_alumno() # lista que contiene los datos del alumno registrado
            print(alumno_registrado)
            nombre = alumno_registrado [0]
            usuario = alumno_registrado[1]
            carrera = alumno_registrado[2]
            asignatura = alumno_registrado[3]
            password = alumno_registrado[4]
            alfa = Alfa(nombre=nombre, usuario=usuario, carrera=carrera, asignatura=asignatura, password=password)
            alfa.cifrardatos()
        elif question == "X" or question == "x":
            end = True
