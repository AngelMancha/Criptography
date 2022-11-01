class Registro:
    """Esta clase solo se va a encargar de validar los datos de inicio de sesión o registro"""
    def __init__(self):
        self.datos_alumno = []

    def registrar_alumno(self):
        """ En esta función se pide los datos al usuario para registrarlo en la aplicación"""
        print("Bienvenido a Alfa!")
        print("\nREGISTRO\n")
        self.validate_nombre()
        self.validate_usuario()
        self.validate_carrera()
        self.validate_asignatura()
        self.validate_password()
        return self.datos_alumno


    def validate_nombre(self):
        """ Función que sirve para validar el nombre real del usuario"""
        nombre = input(str("Por favor, introduce tu nombre: "))
        self.datos_alumno.append(nombre)


    def validate_usuario(self):
        """ Función que sirve para introducir el usuario"""
        usuario = str(input("Introduce su nombre de usuario: "))
        size_str = len(usuario)
        while usuario.isdigit() or size_str == 0:
            if usuario.isdigit() == True:
                print("El nombre de usuario no debe tener solo valores numéricos")
                usuario = str(input("Introduce su nombre de usuario: "))
            if size_str == 0:
                print("Por favor, rellene este campo")
                usuario = str(input("Introduce su nombre de usuario: "))
                size_str = len(usuario)
        self.datos_alumno.append(usuario)


    def validate_carrera(self):
        """ Función para escoger una opción de carrera. """
        carrera = input("Introduce su carrera. Elige entre estas opciones:\n"
                        "A) Ingenieria Informatica \n"
                        "B) Ingenieria de Telecomunicaciones \n")
        posibles_opciones = ["A", "B", "a", "b"]
        while carrera not in posibles_opciones:
            carrera = input("Introduce su carrera. Elige entre estas opciones:\n"
                            "A) Ingenieria Informatica \n"
                            "B) Ingenieria de Telecomunicaciones \n")
            print("Elija entre A, B o C")
            if carrera in posibles_opciones:
                break
        if carrera == "a" or carrera == "A":
            self.datos_alumno.append("Ingenieria Informatica")
        if carrera == "b" or carrera == "B":
            self.datos_alumno.append("Ingenieria de Telecomunicaciones")

    def validate_asignatura(self):
        if self.datos_alumno[2] == "Ingenieria Informatica":
            self.carrera_inf()
        if self.datos_alumno[2] == "Ingenieria de Telecomunicaciones":
            self.carrera_tel()

    def validate_password(self):
        """ Función que valida una contraseña """
        password1 = input("Por favor, ingrese su contraseña\n"
                         "Recuerde que una contraseña segura debe tener mínimo 8 caracteres. "
                         "Debe incluir números.\n"
                          "Debe incluir mayúsculas y minúsculas\n")

        password_segura = self.password_segura(password1)
        while not password_segura:
            print("¡Contraseña poco segura! Por favor, siga las indicaciones dadas para tener una contraseña segura.")
            password1 = input("Por favor, vuelva a ingresar su contraseña\n"
                             "Recuerde que una contraseña segura debe tener mínimo 8 caracteres. "
                             "Debe incluir números.\n"
                              "Debe incluir mayúsculas y minúsculas\n")
            password_segura = self.password_segura(password1)

        password2 = input("La contraseña es válida, vuelva a confirmarla\n")
        aux = False
        if password2 == password1:
            aux = True
        while not aux:
            password2 = input("Las contraseñas deben coincidir. \nPor favor, repita la contraseña")
            if password2 == password1:
                aux = True
        self.datos_alumno.append(password2)

    def password_segura(self, password):
        """Función que comprueba la seguridad de una contraseña. La función devuelve True en caso de que la contraseña
         sea válida y False en caso contrario."""
        size_pasword = len(password)
        user_name = self.datos_alumno[1]
        digit = False
        minus = False
        mayuscula = False
        if size_pasword >= 8:
            for letter in password:
                if letter.isdigit() == True:
                    digit = True
                if letter.islower() == True:
                    minus = True
                if letter.isupper() == True:
                    mayuscula = True
        # en el caso extremo en el que el usuario ponga la misma contraseña que el nombre de usuario se despliega un
        # mensaje de error
        if password == user_name:
            print("¡¡¡ La contraseña NO debe ser igual al nombre de usuario !!!\n")
            return False
        # En caso de que no haya dígitos, minúsculas o mayúsculas la función devuelve False
        if (digit == False or minus == False or mayuscula == False):
            return False
        return True

    def carrera_inf(self):
        """ Función que sirve para imprimir las posibles asignaturas de ingeniería informática """
        posibles_opciones = ["A", "B", "a", "b"]
        asignatura = input("Introduce su asignatura. Elige entre estas opciones:\n"
                           "A) Criptografia y seguridad informatica \n"
                           "B) Heurística y Optimización \n")
        while asignatura not in posibles_opciones:
            asignatura = input("Introduce su asignatura. Elige entre estas opciones:\n"
                               "A) Criptografia y seguridad informatica \n"
                               "B) Heuristica y Optimizacion \n")
            print("Elija entre A, B o C")
            if asignatura in posibles_opciones:
                break
        if asignatura == "a" or asignatura == "A":
            self.datos_alumno.append("Criptografia y seguridad informatica")
        if asignatura == "b" or asignatura == "B":
            self.datos_alumno.append("Heuristica y Optimizacion")

    def carrera_tel(self):
        """ Función que sirve para imprimir las posibles asignaturas de ingeniería de telecomunicaciones """
        posibles_opciones = ["A", "B", "a", "b"]
        asignatura = input("Introduce su asignatura. Elige entre estas opciones:\n"
                           "A) Sistemas Electronicos \n"
                           "B) Teoria moderna de la deteccion y estimacion \n")
        while asignatura not in posibles_opciones:
            asignatura = input("Introduce su asignatura. Elige entre estas opciones:\n"
                               "A) Sistemas Electronicos \n"
                               "B) Teoria moderna de la deteccion y estimacion \n")
            print("Elija entre A, B o C")
            if asignatura in posibles_opciones:
                break
        if asignatura == "a" or asignatura == "A":
            self.datos_alumno.append("Sistemas Electrónicos")
        if asignatura == "b" or asignatura == "B":
            self.datos_alumno.append("Teoria moderna de la deteccion y estimacion")
