# 1. Crea una lista que represente datos estructurados (por ejemplo: edades de estudiantes) y muestra su tipo de dato
def createAListWichRepresentStructureData(edades: list[int]= None):
    if edades is None:
        edades = [12, 15, 16, 9, 12, 13]
    elif not isinstance(edades, list):
        raise TypeError("El parámetro 'edades' debe ser una lista")
    print(f"Edades de estudiantes: {edades} -> data type = {type(edades).__name__}")

# 2. Crea una variable tipo texto que represente un comentario libre de un usuario y cuenta cuantas palabras tiene
def createAVariableTypeText(comment: str= None):
    if comment is None:
        comment = "Estaba registrando mi información en el formulario de crear estudiante y el campo de edad tiene un error, si el valor no tiene 2 digitos no deja enviar los datos"
    elif not isinstance(comment, str):
        raise TypeError("El parámetro 'comment' debe ser una cadena de texto")
    words_in_comentario = len(comment.split(" ")) # separando palabras y contando las
    print(f"comentario: {comment}")
    print(f"la variable comentario tiene un total de {words_in_comentario} palabras") # imprimiendo el total de palabras


# 3. Crea un diccionario con información estructurada de un estudiante (nombre, edad, carrera) e imprime cada valor por separado.
def createADictionaryWithStudentStructuredInformation(nombre: str = None, edad: int = None, carrera: str = None):
    if nombre is None:
        nombre = "Kevin Manuel Gomez Rojas"
    elif not isinstance(nombre, str):
        raise TypeError("El parámetro 'nombre' debe ser una cadena de texto")

    if edad is None:
        edad = 24
    elif not isinstance(edad, int):
        raise TypeError("El parámetro 'edad' debe ser un numero entero")

    if carrera is None:
        carrera = "Ing de Software"
    elif not isinstance(carrera, str):
        raise TypeError("El parámetro 'carrera' debe ser una cadena de texto")

    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera
    }
    print(f"Nombre del estudiante: {estudiante['nombre']}")
    print(f"Edad del estudiante: {estudiante['edad']}")
    print(f"Carrera del estudiante: {estudiante['carrera']}")
