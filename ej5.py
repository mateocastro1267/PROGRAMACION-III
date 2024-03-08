def es_palindromo(palabra):
    """
    Función para verificar si una palabra es un palíndromo.
    """
    return palabra == palabra[::-1]

print(es_palindromo("neuquen"))  
print(es_palindromo("jovenes"))  
