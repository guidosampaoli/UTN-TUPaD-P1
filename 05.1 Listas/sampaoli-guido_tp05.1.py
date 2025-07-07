import utils.functions as f

"""
1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4.
Utilizar la función range.
"""
f.actividad(1)
multiplos_4 = []
for i in range(1, 101):
    if i % 4 == 0:
        multiplos_4.append(i)
    else:
        pass
print(multiplos_4)


"""
2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
indexing con números negativos!
"""
f.actividad(2)
mi_lista = [8, 9.3, "texto", ["lista", "anidada"], "quinto elemento"]
print(mi_lista[-2])


"""
3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
ejemplo:
lista_vacia = []
"""
f.actividad(3)
mi_lista = []
mi_lista.append(7)
mi_lista.append(8)
mi_lista.append(9)
print(mi_lista)


"""
4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
en los videos o bien investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]
"""
f.actividad(4)
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)


"""
5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
"""
f.actividad(5)
numeros = [8, 15, 3, 22, 7]
print(f"Dada la lista original: {numeros}")
numeros.remove(max(numeros))
print(f"Se identifica el número más grande de la lista con la función 'max()'"
      f"\ny con el método 'remove()' se elimina dicho elemento de la lista."
      f"\nEso es lo que sucede en la línea de código: 'numeros.remove(max(numeros))'"
      f"\nQuedando así la lista modificada: {numeros}")


"""
6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
pantalla los dos primeros.
"""
f.actividad(6)
lista = []
for i in range(10, 31, 5):
    lista.append(i)
print(lista[0:2])


"""
7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
"""
f.actividad(7)
autos = ["sedan", "polo", "suran", "gol"]
print(autos)
autos[1] = autos[1][::-1]
autos[2] = autos [2][::-1]
print(autos)


"""
8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
directamente. Imprimir la lista resultante por pantalla.
"""
f.actividad(8)
simples = [5, 10, 15]
dobles = []
for i in simples:
    dobles.append(i * 2)
print(dobles)

"""
9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
a) Agregar "jugo" a la lista del tercer cliente usando append.
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
c) Eliminar "pan" de la lista del primer cliente.
d) Imprimir la lista resultante por pantalla
"""
f.actividad(9)
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)


"""
10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
● Posición lista_anidada[0]: 15
● Posición lista_anidada[1]: True
● Posición lista_anidada[2][0]: 25.5
● Posición lista_anidada[2][1]: 57.9
● Posición lista_anidada[2][2]: 30.6
● Posición lista_anidada[3]: False
Imprimir la lista resultante por pantalla.
"""
f.actividad(10)
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)