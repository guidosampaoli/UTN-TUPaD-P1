from random import randint
import utils.functions as f
from utils.functions import actividad

"""
1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
"""
f.actividad(1)
for i in range(0, 101):
    print(i)


"""
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.
"""
f.actividad(2)
num = int(input("Ingrese un número entero: "))
contador = 0
while num > 0:
    num //= 10
    contador += 1
print(f"El número ingresado tiene {contador} dígitos.")


"""
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.
"""
f.actividad(3)
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
menor = min(num1, num2)
mayor = max(num1, num2)
suma = 0
for i in range(menor + 1, mayor):
    suma += i
print(f"La suma de los número entre {menor} y {mayor} es: {suma}")


"""
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
"""
f.actividad(4)
num = int(input("Ingrese un número entero para sumar | Ingrese 0 para terminar: "))
suma = 0
while num != 0:
    suma += num
    num = int(input("Ingrese un número entero para sumar | Ingrese 0 para terminar: "))
print(f"La suma de los número es: {suma}")


"""
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""
actividad(5)
secreto = randint(0, 9)
intento = int(input("Adiviná el número entre 0 y 9: "))
intentos = 1
while intento != secreto:
    intento = int(input("¡Incorrecto! Intentá de nuevo: "))
    intentos += 1
print(f"¡Correcto! Adivinaste el número secreto en {intentos} intentos")


"""
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.
"""
actividad(6)
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)


"""
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
"""
actividad(7)
num = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(0, num + 1):
    suma += i
print(f"La suma de todos los números comprendidos entre 0 y {num} es: {suma}")


"""
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""
actividad(8)
pares = 0
impares = 0
negativos = 0
positivos = 0
for i in range(1, 101):
    num = int(input(f"Ingrese el {i}º número entero: "))
    if num >= 0:
        positivos += 1
    else:
        negativos += 1
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Cantidad de números:"
      f"\nPares: {pares}"
      f"\nImpares: {impares}"
      f"\nNegativos: {negativos}"
      f"\nPositivos: {positivos}")


"""
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
"""
actividad(9)
inicio = 1
fin = 101
suma = 0
for i in range(inicio, fin):
    num = int(input(f"Ingrese el {i}º número entero: "))
    suma += num
print(f"La media de los valores ingresados es: {suma / (fin - 1)}")


"""
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""
actividad(10)
num = int(input("Ingrese un número entero: "))
invertido = 0
while num != 0:
    digito = num % 10
    invertido = invertido * 10 + digito
    num //= 10
print(f"El número invertido es: {invertido}")