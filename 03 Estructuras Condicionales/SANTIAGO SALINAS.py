# 1) Escribir un programa que solicite la edad del usuario. 
# Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int(input("Introduce tu edad: "))

if edad > 18:
    print("Es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario.
# Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
nota = int(input("Introduce tu nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares.
# Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".
# Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
numero = int(input("Introduce un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#  ● Niño/a: menor de 12 años. 
#  ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#  ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#  ● Adulto/a: mayor o igual que 30 años.
edad = int(input("Introduce tu edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14).
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.
contraseña = input("Introduce una contraseña: ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma: 
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria.
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if media > mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("Sesgo no definido")

# 7) Escribir un programa que solicite una frase o palabra al usuario.
# Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
frase = input("Introduce una frase o palabra: ")

if frase[-1] in "aeiouAEIOU": 
    frase_modificada = frase + "!"
    print(frase_modificada)
else:
    print(frase)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.
# Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.
nombre = input("Introduce tu nombre: ")
opcion = input("Elige una opción:\n1. Mayúsculas\n2. Minúsculas\n3. Primera letra mayúscula\nOpción: ")

if opcion == "1":
    nombre_modificado = nombre.upper()
elif opcion == "2":
    nombre_modificado = nombre.lower()
elif opcion == "3":
    nombre_modificado = nombre.title()
else:
    nombre_modificado = "Opción inválida"

print(nombre_modificado)

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
magnitud = float(input("Introduce la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es.
#  El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
# NOTA: sacar información de la tabla del PDF
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()
mes = input("¿Qué mes del año es? ").lower()
dia = int(input("¿Qué día es? "))

if hemisferio == "N":
    if mes == "diciembre" and dia >= 21 or mes == "enero" or mes == "febrero" or mes == "marzo" and dia <= 20:
        estacion = "Invierno"
    elif mes == "marzo" and dia >= 21 or mes == "abril" or mes == "mayo" or mes == "junio" and dia <= 20:
        estacion = "Primavera"
    elif mes == "junio" and dia >= 21 or mes == "julio" or mes == "agosto" or mes == "septiembre" and dia <= 20:
        estacion = "Verano"
    else:
        estacion = "Otoño"
elif hemisferio == "S":
    if mes == "diciembre" and dia >= 21 or mes == "enero" or mes == "febrero" or mes == "marzo" and dia <= 20:
        estacion = "Verano"
    elif mes == "marzo" and dia >= 21 or mes == "abril" or mes == "mayo" or mes == "junio" and dia <= 20:
        estacion = "Otoño"
    elif mes == "junio" and dia >= 21 or mes == "julio" or mes == "agosto" or mes == "septiembre" and dia <= 20:
        estacion = "Invierno"
    else:
        estacion = "Primavera"
else:
    estacion = "Hemisferio inválido"

print(f"Estás en {estacion}")