class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)

    def esta_regular(self, nota_minima=6):
        if self.nota >= nota_minima:
            print(self.nombre, "está regular.")
        else:
            print(self.nombre, "no está regular.")


alumno1 = Alumno("Juan", 8)
alumno2 = Alumno("María", 5)

alumno1.imprimir()
alumno2.imprimir()


alumno1.esta_regular()
alumno2.esta_regular()
