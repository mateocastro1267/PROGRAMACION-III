def buscar_en_lista(lista, elemento):

    try:
        indice = lista.index(elemento)
        return indice
    except ValueError:
        return -1

lista = [8, 12, 9, 45]

elemento_buscado = int(input("Ingrese el elemento que desea buscar: "))

indice = buscar_en_lista(lista, elemento_buscado)

if indice != -1:
    print("El elemento", elemento_buscado, "se encuentra en el índice", indice)
else:
    print("El elemento", elemento_buscado, "no se encuentra en la lista.")
