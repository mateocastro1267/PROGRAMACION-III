def ordenar_de_mayor_a_menor(lista):
   
    return sorted(lista, reverse=True)

lista_numeros = [5, 2, 8, 1, 9]
print("Lista original:", lista_numeros)
print("Lista ordenada de mayor a menor:", ordenar_de_mayor_a_menor(lista_numeros))
