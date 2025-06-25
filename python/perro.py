class Perro:
    def __init__(self, id, nombre, raza, edad, tamaño, peso, estado_salud, vacunado, estado, temperamento):
        self.id = id
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.tamaño = tamaño
        self.peso = peso
        self.estado_salud = estado_salud
        self.vacunado = vacunado
        self.estado = estado
        self.temperamento = temperamento

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def mostrar_info(self):
        print(f"[{self.id}] {self.nombre} - {self.raza} ({self.edad} años)")
        print(f"  Tamaño: {self.tamaño} | Peso: {self.peso}kg")
        print(f"  Salud: {self.estado_salud} | Vacunado: {'Sí' if self.vacunado else 'No'}")
        print(f"  Estado: {self.estado} | Temperamento: {self.temperamento}")