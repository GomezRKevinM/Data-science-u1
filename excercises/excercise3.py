# Calcula el promedio de tres números usando operadores aritméticos
from math import isnan


def calculaPromedioDe3Numeros(num1 = 5, num2 = 4, num3 =2):
    if not isinstance(num1, int) or not isinstance(num2, int) or not isinstance(num3, int): # validamos tipo
        raise TypeError("Parámetro invalido para numero")

    promedio = (num1+num2+num3)/3 # sumamos el total y dividimos por 3 para sacar el promedio
    print(f"promedio de [{num1},{num2},{num3}] = {promedio}") #imprimimos

# Usa operadores de comparación para verificar si un número es mayor que 50
def useComparerOperatorsForCheckIfANumberIsGreaterThan50(numero=51):
    if not isinstance(numero, int): # validamos tipo
        raise TypeError("el parametro ingresado no es un número")
    print(f"{numero} es mayor que 50" if numero > 50 else f"{numero} es menor que 50") # usamos operador ternario para comparar e imprimir

# Usa operadores lógicos para verificar si una persona es mayor de edad (≥18) y tiene licencia
def useLogicsOperatorsForCheckIfAPersonIsGreater(edad=24, licencia = False):
    if not isinstance(edad, int): # validamos tipo
        raise TypeError("La edad debe ser un numero entero")

    es_mayor = "si" if edad >= 18 else "No" # operador ternario para comparar y asignar Si o No
    tiene_licencia = "si" if licencia else "No" # operador ternario para comparar y asignar Si o No
    print(f"la persona es mayor de edad: {es_mayor}")
    print(f"la persona tiene Licencia: {tiene_licencia}")
