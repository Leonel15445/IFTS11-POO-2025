from perro import Perro
from usuario import UsuarioAdoptante

class SistemaAdopcion:
    def __init__(self):
        self.perros = []
        self.usuarios = []

    def cargar_perro(self, perro):
        self.perros.append(perro)

    def eliminar_perro(self, id_perro):
        self.perros = [p for p in self.perros if p.id != id_perro]

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def postular_perro(self, dni_usuario, id_perro):
        usuario = self._buscar_usuario(dni_usuario)
        perro = self._buscar_perro(id_perro)
        if usuario and perro and perro.estado == 'disponible':
            perro.cambiar_estado('reservado')

    def confirmar_adopcion(self, dni_usuario, id_perro):
        usuario = self._buscar_usuario(dni_usuario)
        perro = self._buscar_perro(id_perro)
        if usuario and perro and perro.estado == 'reservado':
            perro.cambiar_estado('adoptado')
            usuario.historial_adopciones.append(perro)

    def sugerir_perros(self, preferencias):
        sugerencias = []
        for perro in self.perros:
            if perro.estado == 'disponible':
                coincide = True
                for clave, valor in preferencias.items():
                    if getattr(perro, clave, None) != valor:
                        coincide = False
                        break
                if coincide:
                    sugerencias.append(perro)
        return sugerencias

    def mostrar_perros_disponibles(self):
        for perro in self.perros:
            if perro.estado == 'disponible':
                perro.mostrar_info()

    def mostrar_perros_por_estado(self, estado):
        for perro in self.perros:
            if perro.estado == estado:
                perro.mostrar_info()

    def mostrar_perros_por_usuario(self, dni_usuario):
        usuario = self._buscar_usuario(dni_usuario)
        if usuario:
            usuario.ver_historial()

    def _buscar_perro(self, id):
        for perro in self.perros:
            if perro.id == id:
                return perro
        return None

    def _buscar_usuario(self, dni):
        for usuario in self.usuarios:
            if usuario.dni == dni:
                return usuario
        return None