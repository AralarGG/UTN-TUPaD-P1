#TRABAJO PRACTICO: FUNCIONES

#EJERCICIO 1
#1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")
    
    
imprimir_hola_mundo()


#EJERCICIO 2
#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

nombre = input("Ingrese nombre: ")
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")
    
saludar_usuario(nombre)

#EJERCICIO 3
#3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.


nombre = input("Ingrese nombre: ")
apellido =input("Ingrese apellido: ")
edad =input("Ingrese edad: ")
residencia =input("Ingrese residencia: ")
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}!")
informacion_personal(nombre, apellido, edad, residencia)

#EJERCICIO 4
#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área 
# del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro 
# del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

import math
radio = float(input("Ingrese radio: "))
pi = math.pi
def calcular_area_circulo(radio):
    return pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * pi * radio

print(calcular_area_circulo(radio))
print(calcular_perimetro_circulo(radio))



#EJERCICIO 5
#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

segundos = int(input("Ingrese segundos: "))
def segundos_a_horas(segundos):
    return segundos / 3600

print(f"Serían: {segundos_a_horas(segundos)}")

#EJERCIOCIO 6
#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

numero = int(input("Ingrese numero del 1 al 10: "))

def tabla_multiplicar(numero):
    for c in range(1, 11):
        print(f"{c} x {numero} = {c * numero}")

tabla_multiplicar(numero)

#EJERCICIO 7
# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.


numero_1 = int(input("Ingrese numero 1: "))
numero_2 = int(input("Ingrese numero 2: "))
def operaciones_basicas(a,b):
    suma = a + b
    print(f"La suma es: {suma}")
    resta = a - b
    print(f"La resta es: {resta}")
    multiplicacion = a * b
    print(f"La multiplicacion es: {multiplicacion}")
    if b != 0:
        division = a / b
        print(f"La division es: {division}")
    else:
        print("No se puede dividir por 0")
operaciones_basicas(numero_1, numero_2)

#EJERCICIO 8
# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.


peso = float(input("Ingrese peso: "))
altura = float(input("Ingrese altura en metro: "))

def calcular_imc(x, y):
    imc = (peso) / (altura ** 2)
    print(f"El IMC es: {imc}")
    
calcular_imc(peso, altura)


#EJERCICIO 9
# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.
 

celsius = float(input("Ingrese grados Celsius: "))
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * (9/5)) + 32
    print(f"En fahrenheit sería: {fahrenheit}")
    
celsius_a_fahrenheit(celsius)

#EJERCICIO 10
#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.

x1 = float(input("Ingrese numero 1: "))
x2 = float(input("Ingrese numero 2: "))
x3 = float(input("Ingrese numero 3: "))

def calcular_promedio(a,b,c):
    return (a + b + c) / 3

print(f"El promedio es {calcular_promedio(x1,x2,x3)}")