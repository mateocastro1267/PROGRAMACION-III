try:
    with open('ej1G3.txt', 'w') as archivo:
        archivo.write(123)
except ValueError:
    print("No se puede escribir en el archivo")