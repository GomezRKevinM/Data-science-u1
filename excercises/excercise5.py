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

# Crea una estructura condicional que clasifique una nota (A, B, C o D)
def classifyNote(note: float | int = 5.0):
    if not isinstance(note,float | int):
        raise TypeError("El argumento espera un numero")

    if note < 0 or note > 5:
        raise ValueError("El argumento espera un numero entre 0 y 5")
    match note:
        case n if 4.0 <= n <= 5:
            vowel = "A"
        case n if 3.0 <= n < 4:
            vowel = "B"
        case n if 2.0 <= n < 3:
            vowel = "C"
        case _:
            vowel = "D"

    print(f"su nota se clafica en {vowel}")
