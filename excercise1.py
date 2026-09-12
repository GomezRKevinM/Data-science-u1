# 1. Crea una lista que represente datos estructurados (por ejemplo: edades de estudiantes) y muestra su tipo de dato
estudiantes_edades = [12, 15, 16, 9, 12, 13]
print(f"Edades de etudiantes: {estudiantes_edades} -> data type= {type(estudiantes_edades).__name__}")

# 2. Crea una variable tipo texto que represente un comentario libre de un usuario y cuenta cuantas palabras tiene
comentario = "Estaba registrando mi información en el formulario de crear estudiante y el campo de edad tiene un error, si el valor no tiene 2 digitos no deja enviar los datos"
words_in_comentario = len(comentario.split(" ")) # separando palabras y contando las
print(f"la variable comentario tiene un total de {words_in_comentario} palabras") # imprimiendo el total de palabras


# 3. Crea un diccionario con información estructurada de un estudiante (nombre, edad, carrera) e imprime cada valor por separado.
