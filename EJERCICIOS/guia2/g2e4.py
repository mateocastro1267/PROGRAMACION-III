class Operaciones:
    def __init__(self):
        self.num1 = int(input("Ingrese el primer número entero: "))
        self.num2 = int(input("Ingrese el segundo número entero: "))
        self.realizar_operaciones()

    def realizar_operaciones(self):
        self.suma()
        self.resta()
        self.multiplicacion()
        self.division()

    def suma(self):
        resultado = self.num1 + self.num2
        print(f"La suma de {self.num1} y {self.num2} es: {resultado}")

    def resta(self):
        resultado = self.num1 - self.num2
        print(f"La resta de {self.num1} y {self.num2} es: {resultado}")

    def multiplicacion(self):
        resultado = self.num1 * self.num2
        print(f"El producto de {self.num1} y {self.num2} es: {resultado}")

    def division(self):
        if self.num2 != 0:
            resultado = self.num1 / self.num2
            print(f"La división de {self.num1} entre {self.num2} es: {resultado}")
        else:
            print("No se puede dividir entre cero.")


operaciones = Operaciones()
