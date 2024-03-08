def dibujar_rectangulo(ancho, alto, caracter):

    for i in range(alto):
        print(caracter * ancho)

def main():
    
    ancho = int(input("Ancho: "))
    alto = int(input("Alto: "))
    caracter = input("Caracter: ")

    dibujar_rectangulo(ancho, alto, caracter)

if __name__ == "__main__":
    main()
