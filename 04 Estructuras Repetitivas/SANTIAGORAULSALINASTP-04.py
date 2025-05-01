# Alumno: Santiago Raul Salinas TP 4 
# Ejercicio 1

for numero in range(101):
    print(numero)

#Ejercicio 2

try:
    numero_str = input("Ingrese un número entero: ")
    numero_int = int(numero_str)
    cantidad_digitos = len(numero_str)
    print(f"El número ingresado tiene {cantidad_digitos} dígitos.")
except ValueError:
    print("Error: La entrada no es un número entero válido.")

# Ejercicio 3

def sumar_numeros_entre(inicio, fin):
    suma = 0
    if inicio >= fin - 1:
        return 0
    for numero in range(inicio + 1, fin):  
        suma += numero
    return suma 
try:
    valor1_str = input("Ingrese el primer valor entero: ")
    valor1 = int(valor1_str)
    valor2_str = input("Ingrese el segundo valor entero: ")
    valor2 = int(valor2_str)
    resultado_suma = sumar_numeros_entre(valor1, valor2)
    print(f"La suma de los números enteros entre {valor1} y {valor2} (excluyendo estos) es: {resultado_suma}")
except ValueError:
    print("Error: Por favor, ingrese números enteros válidos.")

#Ejercicio 4

suma_total = 0

print("Ingrese números enteros para sumar (ingrese 0 para detener): ")

while True:
    try:
        entrada_str = input("Ingrese un número: ")
        numero = int(entrada_str)
        if numero == 0:
            break  
        else:
            suma_total += numero
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")

print(f"\nEl total de los números ingresados es: {suma_total}")

#Ejercicio 5

import random
numero_secreto = random.randint(0, 9)
intentos = 0
adivinado = False
print("¡Bienvenido al juego de adivinar el número!")
print("Intenta adivinar el número secreto entre 0 y 9.")

while not adivinado:
    try:
        intento_str = input("Ingresa tu intento: ")
        intento = int(intento_str)
        intentos += 1
        if intento < numero_secreto:
            print("¡Demasiado bajo! Intenta de nuevo.")
        elif intento > numero_secreto:
            print("¡Demasiado alto! Intenta de nuevo.")
        elif intento == numero_secreto:
            adivinado = True
            print(f"¡Felicidades! ¡Adivinaste el número secreto ({numero_secreto}) en {intentos} intentos!")
    except ValueError:
        print("Error: Por favor, ingresa un número entero válido entre 0 y 9.")
    except KeyboardInterrupt:
        print("\n¡Juego interrumpido!")
        break
if not adivinado and intentos > 0:
    print(f"El número secreto era {numero_secreto}.")

#Ejercicio 6
for numero in range(100, -1, -2):
    print(numero)

#Ejercicio 7

while True:
    try:
        limite_str = input("Ingrese un número entero positivo: ")
        limite = int(limite_str)
        if limite > 0:
            break
        else:
            print("Por favor, ingrese un número entero positivo.")
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")
suma = 0
for numero in range(limite + 1):
    suma += numero

print(f"La suma de los números enteros desde 0 hasta {limite} es: {suma}")

#Ejercicio 8

cantidad_numeros = 100
pares = 0
impares = 0
positivos = 0
negativos = 0
print(f"Ingrese {cantidad_numeros} números enteros:")
for i in range(cantidad_numeros):
    while True:
        try:
            entrada_str = input(f"Ingrese el número {i + 1}: ")
            numero = int(entrada_str)

            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1
            if numero > 0:
                positivos += 1
            elif numero < 0:
                negativos += 1

            break  
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")

print("\nResultados:")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")

#Ejercicio 9

cantidad_numeros = 100
numeros = []
print(f"Ingrese {cantidad_numeros} números enteros:")
for i in range(cantidad_numeros):
    while True:
        try:
            entrada_str = input(f"Ingrese el número {i + 1}: ")
            numero = int(entrada_str)
            numeros.append(numero)
            break  
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")
if numeros: 
    media = sum(numeros) / len(numeros)
    print(f"\nLa media de los {len(numeros)} números ingresados es: {media}")
else:
    print("\nNo se ingresaron números para calcular la media.")

#Ejercicio 10

def invertir_numero(numero):
    numero_str = str(abs(numero)) 
    numero_invertido_str = numero_str[::-1] 

    if numero < 0:
        return -int(numero_invertido_str)  
    else:
        return int(numero_invertido_str)
while True:
    try:
        entrada_str = input("Ingrese un número entero: ")
        numero_usuario = int(entrada_str)
        break
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")
numero_invertido = invertir_numero(numero_usuario)
print(f"El número ingresado fue: {numero_usuario}")
print(f"El número con los dígitos invertidos es: {numero_invertido}")