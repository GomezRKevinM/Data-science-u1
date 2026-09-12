# Declara variables de tipo entero, flotante, cadena y booleano. Imprime el tipo de cada una.
def showTypes(edad = None, peso = None, nombre = None):
    if edad is None:
        edad = 24
    elif not isinstance(edad, int):
        raise TypeError("edad debe ser un entero")

    if peso is None:
        peso = 67.8
    elif not isinstance(peso, float):
        raise TypeError("peso debe ser un decimal")

    if nombre is None:
        nombre = "Kevin"
    elif not isinstance(nombre, str):
        raise TypeError("nombre debe ser una cadena de texto")

    mayor = edad >= 18 # comparamos la mayoria de edad

    # imprimiendo tipos
    print(" Variable     Tipo")
    print(f" edad ------> {type(edad).__name__}")
    print(f" peso ------> {type(peso).__name__}")
    print(f" nombre ----> {type(nombre).__name__}")
    print(f" mayor -----> {type(mayor).__name__}")

# Escribe un programa que concatene nombre y apellido almacenados en variables
def concatFullName(nombre= "Kevin Manuel", apellido = "Gomez Rojas"):
    if not isinstance(nombre, str):
        raise TypeError("nombre debe ser una cadena de texto")
    if not isinstance(apellido, str):
        raise TypeError("apellido debe ser una cadena de texto")

    if nombre[-1] != " ": # verificando si el nombre termina con espacio
        full_name = nombre + " " + apellido
    else: # concatenar sin espacio porque el nombre ya lo trae
        full_name = nombre + apellido
    print(full_name)

# Convierte una variable tipo string con valor numérico a entero y súmale 10.
def convertStrToInt(value = "10"):
    if not isinstance(value, str): # validacion de tipo
        raise TypeError("El valor debe ser una cadena de texto")
    if not value.isnumeric(): # validacion de contenido
        raise TypeError("El valor dentro de las cadenas de texto debe ser numerico")

    cast_value = int(value) # convertimos la string a entero
    result = cast_value + 10 # Sumamos el valor convertido + 10
    print(f" resultado {cast_value} + 10 = {result}")
