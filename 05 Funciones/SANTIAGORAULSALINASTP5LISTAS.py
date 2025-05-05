#Trabajo practico LISTAS
#Alumno: Santiago Raul Salinas
#Ejercicio 1
multiplos_de_cuatro = list(range(4, 101, 4))
print(multiplos_de_cuatro)
#Ejercicio 2
mi_lista_favorita = ["pizza", "música", "viajar", "programar", "dormir"]
penultimo_elemento = mi_lista_favorita[-2]
print(penultimo_elemento)
#Ejercicio 3
lista_vacia = []
lista_vacia.append("Aire")
lista_vacia.append("Tierra")
lista_vacia.append("Fuego")
print(lista_vacia)
#Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[len(animales) - 1] = "oso"
print(animales)
#Ejercicio 5
#Explicacion:
#En la primera linea Se crea la lista numeros con 5 elementos numericos dentro
#En la segunda linea la funcion max(numeros) devuelve el mayor de los elementos de la lista numeros (en este caso 22),
#una vez obtenido ese resultado se pasa  como argumento al metodo remove y este elimina dicho numero de la lista numeros.
#En la tercera linea se imprime la lista numeros, que ahora tiene 4 elementos, ya que se elimino el mayor.
#Ejercicio 6
lista_saltos = list(range(10, 31, 5))
print(lista_saltos)
print(lista_saltos[0])
print(lista_saltos[1])
#Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "fiesta"
autos[2] = "cruze"
print(autos)
#Ejercicio 8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)
#Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)
#Ejercicio 10
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]

print(lista_anidada)