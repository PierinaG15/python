class Alumno:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
    #metodo mayor o menor de edad true or falsr
    def esMayorEdad(self):
       return self.edad >= 18
    