# Escribe un programa que determine si un número es par o impar
def isOddOrEver(number: int = 5):
    if not isinstance(number,int):
        raise TypeError("El argumento espera un numero entero")
    par = "es par" if number % 2 == 0 else "no es par"
    print(f"numero {number} {par}")

# Usa un ciclo for para imprimir números del 1 al 10
def printsNumberUpTo10():
    for number in range(1,11): # recoremos del 1 al 11, solo imprime hasta el 10, cuando llega el 11 cierra el bucle
        print(number)

# Usa un ciclo while para contar regresivamente desde 5 hasta 1
def printsRegresive():
    contador = 5 # establecemos el inicio del contador
    while contador > 0: # establecemos la condicion de ejecución
        print(contador) # imprimimos el contador
        contador -= 1 # le restamos 1 a contador y se repite el ciclo hasta que contador sea = 0
