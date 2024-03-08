def es_numero_step(numero):
    
    numero_str = str(numero)
    for i in range(len(numero_str)-1):
        if abs(int(numero_str[i]) - int(numero_str[i+1])) != 1:
            return False
    return True

print(es_numero_step(123234))  
print(es_numero_step(9876787654))  
