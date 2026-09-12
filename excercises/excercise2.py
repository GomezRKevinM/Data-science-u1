# Declara variables de tipo entero, flotante, cadena y booleano. Imprime el tipo de cada una.
from typing import cast

edad = 24 #int
peso = 62.5 #double
nombre = "Kevin" #str
mayor_edad = True #boolean

# imprimiendo tipos

print(f" edad --> {type(edad).__name__}")
print(f" peso --> {type(peso).__name__}")
print(f" nombre --> {type(nombre).__name__}")
print(f" mayor_edad --> {type(mayor_edad).__name__}")

# Escribe un programa que concatene nombre y apellido almacenados en variables
apellido = "Gomez Rojas"
nombre = "Kevin Manuel"
if nombre[-1] != " ": # verificando si el nombre termina con espacio
    full_name = nombre + " " + apellido
else: # concatenar sin espacio porque el nombre ya lo trae
    full_name = nombre + apellido

# Convierte una variable tipo string con valor numérico a entero y súmale 10.
value_str = "10"
cast_value = int(value_str) # convertimos la string a entero
result = cast_value + 10 # Sumamos el valor convertido + 10
print(f" resultado {cast_value} + 10 = {result}")