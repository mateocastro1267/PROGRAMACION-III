def es_bisiesto(anio):

    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

def main():
  
    anio = int(input("Ingrese un año: "))

    if es_bisiesto(anio):
        print(anio, "es bisiesto.")
    else:
        print(anio, "no es bisiesto.")

if __name__ == "__main__":
    main()
