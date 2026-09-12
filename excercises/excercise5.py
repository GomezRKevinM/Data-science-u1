# Escribe un programa que determine si un número es par o impar
def isOddOrEver(number: int = 5):
    if not isinstance(number,int):
        raise TypeError("El argumento espera un numero entero")
    par = "es par" if number % 2 == 0 else "no es par"
    print(f"numero {number} {par}")

