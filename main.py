from alfa import Alfa
from registro import Registro

if __name__ == "__main__":
    print("Hola!")
    question = str(input ("¿Deseas iniciar sesión [A] o Registrarte [B]?"))

    if question == "A" or question == "a":
        log_alfa= Alfa(None, None, None, None)
        log_user = log_alfa.check_hash()
    elif question == "B" or question == "b":
        registrar_alumno = Registro()
        alumno_registrado = registrar_alumno.registrar_alumno() # lista que contiene los datos del alumno registrado
        print(alumno_registrado)
        usuario = alumno_registrado[0]
        carrera = alumno_registrado[1]
        asignatura = alumno_registrado[2]
        password = alumno_registrado[3]
        alfa = Alfa(usuario=usuario, carrera=carrera, asignatura=asignatura, password=password)
        alfa.cifrardatos()


