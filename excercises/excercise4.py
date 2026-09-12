# Crea una lista con 5 frutas e imprime la tercera
fruit_list = ['Banana', 'Manzana', 'Kiwi', 'Sandia', 'Naranja']
print(f"fruta #3 {fruit_list[-3]}") # podemos uasr 2 o -3 para representar el 3er elemento en esta ocación

# Añade un elemento a la lista anterior
fruit_list.append("Fresa")
print(fruit_list) #imprimimos para mostrar la fruta agregada

# Crea una tupla con 3 ciudades y recórrela con un ciclo
ciudades = "Cartagena", "Medellin", "Pereira" # tupla con empaquetado implicito - usar () para empaquetado explicito
for city in ciudades: # ciclo para recorrer la tupla
    print(city) # imprimir el item presente en la iteracion del ciclo

# Crea un diccionario con productos y precios y muestra solo las claves
productos = {
    "Teclado" :  180000,
    "Honor 400 smart": 1300000,
    "Manzana": 2500
}
print(f"keys of productos: {productos.keys()}")