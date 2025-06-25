
class UsuarioAdoptante:
    def __init__(self, nombre, dni, email, preferencias):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.preferencias = preferencias
        self.historial_adopciones = []

    def modificar_datos(self, nombre=None, email=None):
        if nombre:
            self.nombre = nombre
        if email:
            self.email = email

    def ver_historial(self):
        if not self.historial_adopciones:
            print("No hay adopciones registradas.")
        else:
            print("Historial de adopciones:")
            for perro in self.historial_adopciones:
                print(f"- {perro.nombre} ({perro.raza})")