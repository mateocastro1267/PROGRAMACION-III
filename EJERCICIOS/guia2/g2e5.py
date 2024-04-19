class Persona:
    def __init__(self):
        self.nombre = input("Ingrese el nombre de la persona: ")
        self.edad = int(input("Ingrese la edad de la persona: "))

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)


class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = float(input("Ingrese el sueldo del empleado: "))

    def imprimir(self):
        super().imprimir()
        print("Sueldo:", self.sueldo)

    def pagar_impuestos(self):
        if self.sueldo > 3000:
            print("El empleado debe pagar impuestos.")
        else:
            print("El empleado no debe pagar impuestos.")



if __name__ == "__main__":
   
    persona = Persona()
    print("\nDatos de la persona:")
    persona.imprimir()

    
    empleado = Empleado()
    print("\nDatos del empleado:")
    empleado.imprimir()
    empleado.pagar_impuestos()
