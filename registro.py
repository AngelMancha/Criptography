class Registro:
    """Esta clase solo se va a encargar de validar los datos de inicio de sesión o registro"""
    def __init__(self):
        self.campos_registro = campos_registro = ["usuario: ", "carrera", "asignaturas: ", "contraseña: "]
        self.datos_alumno = []

    def registrar_alumno(self):
        """ En esta función se pide los datos al usuario para registrarlo en la aplicación"""
        print("Bienvenido a Alfa!")
        self.validate_usuario()
        self.validate_carrera()
        self.validate_asignatura()
        self.validate_password()
        return self.registrar_alumno()


    def validate_usuario(self)-> str:
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
        carrera = input("Introduce su carrera. Elige entre estas opciones:\n"
                        "A) Ingeniería Informática \n"
                        "B) Ingeniería de Telecomunicaciones \n")
        posibles_opciones = ["A", "B", "a", "b"]
        while carrera not in posibles_opciones:
            carrera = input("Introduce su carrera. Elige entre estas opciones:\n"
                            "A) Ingeniería Informática \n"
                            "B) Ingeniería de Telecomunicaciones \n")
            print("Elija entre A, B o C")
            if carrera in posibles_opciones:
                break
        if carrera == "a" or carrera == "A":
            self.datos_alumno.append("Ingeniería Informática")
        if carrera == "b" or carrera == "B":
            self.datos_alumno.append("Ingeniería de Telecomunicaciones")

    def validate_asignatura(self):
        if self.datos_alumno[1] == "Ingeniería Informática":
            self.carrera_inf()
        if self.datos_alumno[1] == "Ingeniería de Telecomunicaciones":
            self.carrera_tel()

    def validate_password(self):
        password1 = input("Por favor, ingrese su contraseña\n"
                         "Recuerde que una contraseña segura debe tener mínimo 8 caracteres. "
                         "Debe incluir números.\n")

        password_segura = self.password_segura(password1)
        while not password_segura:
            print("¡Contraseña poco segura! Por favor, siga las indicaciones dadas para tener una contraseña segura.")
            password1 = input("Por favor, ingrese su contraseña\n"
                             "Recuerde que una contraseña segura debe tener mínimo 8 caracteres. "
                             "Debe incluir números.\n")
            password_segura = self.password_segura(password1)
        password2 = input("Por favor, repita la contraseña\n")
        aux = False
        if password2 != password1:
            aux = False
        while not aux:
            password2 = input("Las contraseñas deben coincidir. \nPor favor, repita la contraseña")
            if password2 == password1:
                aux = True
        self.datos_alumno.append(password2)

    def password_segura(self, password):
        size_pasword = len(password)
        if size_pasword < 8:
            return False
        aux = False
        for letter in password:
            if letter.isdigit() == True:
                aux = True
        return aux

    def carrera_inf(self):
        posibles_opciones = ["A", "B", "a", "b"]
        asignatura = input("Introduce su asignatura. Elige entre estas opciones:\n"
                           "A) Criptografía y seguridad informática \n"
                           "B) Heurística y Optimización \n")
        while asignatura not in posibles_opciones:
            asignatura = input("Introduce su asignatura. Elige entre estas opciones:\n"
                               "A) Criptografía y seguridad informática \n"
                               "B) Heurística y Optimización \n")
            print("Elija entre A, B o C")
            if asignatura in posibles_opciones:
                break
        if asignatura == "a" or asignatura == "A":
            self.datos_alumno.append("Criptografía y seguridad informática")
        if asignatura == "b" or asignatura == "B":
            self.datos_alumno.append("Heurística y Optimización")

    def carrera_tel(self):
        posibles_opciones = ["A", "B", "a", "b"]
        asignatura = input("Introduce su asignatura. Elige entre estas opciones:\n"
                           "A) Sistemas Electrónicos \n"
                           "B) Teoría moderna de la detección y estimación \n")
        while asignatura not in posibles_opciones:
            asignatura = input("Introduce su asignatura. Elige entre estas opciones:\n"
                               "A) Sistemas Electrónicos \n"
                               "B) Teoría moderna de la detección y estimación \n")
            print("Elija entre A, B o C")
            if asignatura in posibles_opciones:
                break
        if asignatura == "a" or asignatura == "A":
            self.datos_alumno.append("Sistemas Electrónicos")
        if asignatura == "b" or asignatura == "B":
            self.datos_alumno.append("Teoría moderna de la detección y estimación")
