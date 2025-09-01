class Persona:
    def __init__(self, nombre, apellido1, apellido2):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido1} {self.apellido2}"

personas = [
    Persona("Emily", "sandoval", "Ramírez"),
    Persona("Carlos", "Ramírez", "Torres")
]

for persona in personas:
    print(persona.nombre_completo())
