from sistema import SistemaAdopcion
from perro import Perro
from usuario import UsuarioAdoptante

sistema = SistemaAdopcion()

perro1 = Perro(1, "Luna", "Labrador", 3, "mediano", 18, "buena", True, "disponible", "amigable")
sistema.cargar_perro(perro1)

perro2 = Perro(2, "rocky", "beagle", 2, "pequeño", 10, "excelente", True, "disponible", "jugueton")
sistema.cargar_perro(perro2)

preferencias = {"raza": "Labrador", "edad": 3}
usuario1 = UsuarioAdoptante("Leo", "12345678", "leo@mail.com", preferencias)
sistema.registrar_usuario(usuario1)

sistema.postular_perro("12345678", 1)

sistema.confirmar_adopcion("12345678", 1)

sistema.mostrar_perros_por_usuario("12345678")
print("\nPerros disponibles:")
sistema.mostrar_perros_por_estado("disponible")