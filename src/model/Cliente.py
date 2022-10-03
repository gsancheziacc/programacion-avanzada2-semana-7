
class Cliente:
    def __init__(self, id, nombre, apellido, rut, direccion):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.direccion = direccion

    def __str__(self):
        return "rut: " + self.rut + " Nombre: " + self.nombre + " Apellido: " + self.apellido
