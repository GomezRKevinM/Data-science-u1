from math import fsum

# Crea una lista de 5 calificaciones, calcula el promedio y muestra si el estudiante aprueba (≥3.0)
def calculateAverageAndShowApprovedStatus(notes: list[float|int] = [4.0, 3.5, 1.0,3.8, 2.6]):
    if not isinstance(notes, list): #  validando parametro
        raise TypeError("notes debe ser una lista")

    if not all(isinstance(note, (int, float)) for note in notes): # validando elementos dentro de la lista
        raise TypeError("Todos los elementos de la lista deben ser enteros o flotantes")

    avg = fsum(notes) / len(notes) # obteniendo promedio
    print(f"El estudiante aprueba con: {avg}" if avg >= 3.0 else f"El estudiante reprueba con: {avg}" ) # mostrando resultado

# Simula la lectura de datos desde una fuente (por ejemplo, una lista de nombres) e imprime cada uno en mayúsculas
def iterateAListAPrintElementsToUpperCase(listName: list[str] = ['Kevin', 'Gary', 'Bella', 'Alexis', 'Sergio', 'Nathan']):
    if not isinstance(listName, list): # validando parametro
        raise TypeError("lista debe ser una lista")
    if all(not isinstance(name, str) for name in listName): # validando elementos dentro de la lista
        raise TypeError("los elementos de la lista deben ser cadenas de texto")

    for name in listName: print(name.upper()) # recorrer e imprimir cada elementro de la lista en mayuscul

# Crea un pequeño programa que pida al usuario su edad y muestre un mensaje según su rango etario (niño, joven, adulto)
def askForYearOldAndShowEtarioRangeMessage():
    edad = 0
    while True: # bucle para repetir la pregunta hasta obtener una respuesta valida
        answer = input("Digita tu edad: ")  # obtener la edad por consola
        if answer.isnumeric():
            edad = int(answer) # asignacion de valor casteado a entero
            break # al ser un valor valido, cerramos el while
        else :
            print("Argumento invalido, intente otra vez") # imprimismo el mensaje de error y se repite el ciclo

    match edad: # creando campos de coincidencia
        case n if n >= 30: # cuando la edad es mayor o igual a 30
            print("Eres un adulto")
        case n if n >= 18: # cuando la edad es mayor o igual a 18
            print("Eres un joven")
        case _: # cualquier edad menor de 18
            print("Eres un niño")
