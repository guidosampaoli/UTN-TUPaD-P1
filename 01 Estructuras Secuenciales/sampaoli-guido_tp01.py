import math
import utils.functions as f

"""
1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
"""
f.actividad(1)
print("Hola Mundo!")


"""
2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla.
"""
f.actividad(2)
name = input("Ingresá tu nombre: ")

print(f"Hola {name}!")


"""
3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla.
"""
f.actividad(3)
name = input("Ingresá tu nombre: ")
lastname = input("Ingresá tu apellido: ")
age = input("Ingresá tu edad: ")
residence = input("Ingresá tu lugar de residencia: ")

print(f"Soy {name} {lastname}, tengo {age} años y vivo en {residence}")


"""
4) Crear un programa que pida al usuario el radio de un círculo e imprima
por pantalla su área y su perímetro.
"""
f.actividad(4)
radio = int(input("Ingresá el radio de un círculo: "))
area = math.pi * (radio**2)
perimetro = 2 * math.pi * radio
print(f"El área del círculo de radio {radio} es: {area} \n"
      f"El perímetro del círculo de radio {radio} es: {perimetro}")


"""
5) Crear un programa que pida al usuario una cantidad de segundos
e imprima por pantalla a cuántas horas equivale.
"""
f.actividad(5)
segundos = int(input("Ingresá una cantidad de segundos: "))
horas = segundos / 3600
print("El equivalente en horas es: ", horas)


"""
6) Crear un programa que pida al usuario un número e imprima
por pantalla la tabla de multiplicar de dicho número.
"""
f.actividad(6)
num = int(input("Ingrese un número para crear su tabla de multiplicar: "))
for n in range(1, 11):
    result = num * n
    print(f"{num} x {n} = {result}")


"""
7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre
por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
"""
f.actividad(7)
num1 = int(input("Ingrese un número entero distinto de 0: "))
num2 = int(input("Ingrese otro número entero distinto de 0: "))
suma = num1 + num2
division = num1 / num2
multiplicacion = num1 * num2
resta = num1 - num2
print(f"Suma: {suma}"
      f"\nDivisión: {division}"
      f"\nMultiplicación: {multiplicacion}"
      f"\nResta: {resta}")


"""
8) Crear un programa que pida al usuario su altura y su peso e imprima
por pantalla su índice de masa corporal.
Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2
"""
f.actividad(8)
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura**2)
print(f"Su índice de masa corporal (IMC) es: {imc}")


"""
9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
"""
f.actividad(9)
celsius = int(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celsius * (9/5)) + 32
print(f"La temperatura expresada en grados Fahrenheit es: {fahrenheit}")


"""
10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números.
"""
f.actividad(10)
num1 = int(input("Ingrese el primer número entero mayor a cero: "))
num2 = int(input("Ingrese el segundo número entero mayor a cero: "))
num3 = int(input("Ingrese el tercer número entero mayor a cero: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los número ingresados es: {promedio}")