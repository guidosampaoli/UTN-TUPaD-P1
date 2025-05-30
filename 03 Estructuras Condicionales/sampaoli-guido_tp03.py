import utils.functions as f
from statistics import mode, median, mean
import random

"""
1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
"""
f.actividad(1)
user_age = int(input("Ingrese su edad: "))
if user_age > 18:
    print("Es mayor de edad")


"""
2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”.
"""
f.actividad(2)
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


"""
3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar.
"""
f.actividad(3)
num = int(input("Ingrese un número par: "))
if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


"""
4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
    ● Niño/a: menor de 12 años.
    ● Adolescente: mayor o igual que 12 años y menor que 18 años.
    ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
    ● Adulto/a: mayor o igual que 30 años.
"""
f.actividad(4)
edad = int(input("Ingrese su edad: "))
if edad >= 0 and edad < 12:
    print("Usted pertenece a la categoría de Niño/a.")
elif edad >= 12 and edad < 18:
    print("Usted pertenece a la categoría de Adolescente.")
elif edad >= 18 and edad < 30:
    print("Usted pertenece a la categoría de Adulto/a joven.")
elif edad >= 30:
    print("Usted pertenece a la categoría de Adulto/a.")
else:
    print("Ingrese una edad válida.")


"""
5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string.
"""
f.actividad(5)
password = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
longitud = len(password)
if longitud >= 8 and longitud <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")


"""
6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
y calcular la moda, la mediana y la media de dichos números.
Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
"""
f.actividad(6)
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if media > mediana > moda:
    print(f"El sesgo de la lista es POSITIVO:"
          f"\nMedia: {media} > Mediana: {mediana} > Moda: {moda}")
elif media < mediana < moda:
    print(f"El sesgo de la lista es NEGATIVO:"
          f"\nMedia: {media} < Mediana: {mediana} < Moda: {moda}")
elif media == mediana == moda:
    print(f"La lista no tiene sesgo:"
          f"\nMedia: {media} = Mediana: {mediana} = Moda: {moda}")
else:
    print("No se cumple ninguna condición de sesgo definida.")


"""
7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla.
"""
f.actividad(7)
palabra = input("Ingrese una palabra: ")
if palabra.endswith(("a", "e", "i", "o", "u")):
    palabra += "!"
print(palabra)


"""
8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas.
"""
f.actividad(8)
nombre = input("Ingrese su nombre completo: ")
opcion = int(input("1) Mayúsculas"
                   "\n2) Minúsculas"
                   "\n3) Primera letra mayúscula"
                   "\nIngrese el número de la opción deseada para transformar su nombre: "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Por favor ingrese una opción válida.")


"""
9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
"""
f.actividad(9)
magnitud = float(input("Ingrese la magnitud del terremoto para saber a qué categoría pertenece: "))
if magnitud < 3:
    categoria = '"Muy leve" (imperceptible).'
elif 3 <= magnitud < 4:
    categoria = '"Leve" (ligeramente perceptible).'
elif 4 <= magnitud < 5:
    categoria = '"Moderado" (sentido por personas, pero generalmente no causa daños).'
elif 5 <= magnitud < 6:
    categoria = '"Fuerte" (puede causar daños en estructuras débiles).'
elif 6 <= magnitud < 7:
    categoria = '"Muy fuerte" (puede causar daños significativos).'
elif magnitud >= 7:
    categoria = '"Extremo" (puede causar graves daños a gran escala).'
print (f"El terremoto de magnitud {magnitud} en la escala de richter es de categoría {categoria}")


"""
10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano.
"""
f.actividad(10)
hemisferio = input("Indique en cuál hemisferio se encuentra (N/S): ").upper()
mes = int(input("Indique el mes en formato numérico: "))
dia = int(input("Indique el día: "))
fecha = (mes, dia)
if fecha >= (12, 21) or fecha <= (3,20):
    if hemisferio == "N":
        estacion = "Invierno"
    elif hemisferio == "S":
        estacion = "Verano"
elif (3, 21) <= fecha <= (6, 20):
    if hemisferio == "N":
        estacion = "Primavera"
    elif hemisferio == "S":
        estacion = "Otoño"
elif (6, 21) <= fecha <= (9, 20):
    if hemisferio == "N":
        estacion = "Verano"
    elif hemisferio == "S":
        estacion = "Invierno"
elif (9, 21) <= fecha <= (12, 20):
    if hemisferio == "N":
        estacion = "Otoño"
    elif hemisferio == "S":
        estacion = "Primavera"
print(f"La estación según el hemisferio y fecha es: {estacion}")
