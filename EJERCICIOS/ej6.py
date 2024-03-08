def contar_vocales(frase):
   
    vocales = "aeiouAEIOU"
    contador = 0
    for caracter in frase:
        if caracter in vocales:
            contador += 1
    return contador

frase = "Esta es una frase de ejemplo"
print("Cantidad de vocales:", contar_vocales(frase))
