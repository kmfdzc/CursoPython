#Created by: Karina Fernandez
#Created on: September 3rd, 2021
#Last modification: September 9th, 2021

#-------VARIABLES--------

#Ejercicio 1: Imprimir la suma de a y b
a = 5
b = 8
print (a + b)

#Ejercicio 2: Imprimir a^b
A = 2
B = 0
print(A**B)

#Ejercicio 3: Imprimir los años que le faltan al usuario para llegar a 100
edad = input()
print(100-edad)

#Ejercicio 4: Determinar si la persona es mayor de edad
edadusuario = input()
if edadusuario >= 18:
   esMayorEdad = True
   print("Es mayor de edad")
else:
    print("Es menor de edad")

#Ejercicio 5: Pasar de grados Farenheit a centigrados
print("Ingresa los grados Farenheit")
farenheit = input()
centigrados = (farenheit - 32) * 5 / 9
print("Los centigrados son: ", centigrados)

#-------CONDICIONALES--------

#Ejercicio 1: Determinar si el superhéroe es Batman
heroe = input()
heroe_lowcaps = heroe.lower()
batman = "batman"
if heroe_lowcaps == batman:
    print("Tu héroe es Batman")
else:
    print("Tu héroe no es Batman")

#Ejercicio 2: Explicar a que se refiere cada opción
print("Selecciona una opción:\n 1. Imprimir reporte\n 2. Consultar reportes\n 3. Salir")
seleccion = input()
if seleccion == 1:
    print("Has seleccionado '1. Imprimir reporte'")
elif seleccion == 2:
    print("Has seleccionado '2. Consultar reportes'")
elif seleccion == 3:
    print("Has seleccionado '3. Salir'")

#Ejercicio 3: Imprimir el número mayor
numero1 = input()
numero2 = input()
if numero1 < numero2:
    print(numero2, " es el número mayor")
elif numero2 < numero1:
    print(numero1, " es el número mayor")

#Ejercicio 4: Imprimir el punto más cercano al origen 
print("Ingresa X1")
X1 = input()
print("Ingresa Y1")
Y1 = input()
print("Ingresa X2")
X2 = input()
print("Ingresa Y2")
Y2 = input()
distancia1 = ((X1 ^ 2) + (Y1 ^ 2)) ** 0.5
distancia2 = ((X2 ^ 2) + (Y2 ^ 2)) ** 0.5
if distancia1 < distancia2:
    print("El punto ", X1, ",", Y1, " es el más cercano al origen")
elif distancia2 < distancia1:
    print("El punto ", X2, ",", Y2, " es el más cercano al origen")

#Ejercicio 5: Determinar si el número es multiplo de 3 o 5
print("Ingresa un número del 1 al 10")
number = input()
if (number % 3 == 0):
    print("El número es múltiplo de 3")
elif (number % 5 == 0):
    print("El número es múltiplo de 5")
else:
    print("El número no es múltiplo de 3 o 5")

#Ejercicio 6: Juego piedra papel o tijera
print("Jugador 1:")
txt1 =input()
jugador1 = txt1.lower()
print("Jugador 2:")
txt2 =input()
jugador2 = txt2.lower()

if jugador1 == "piedra":
    if jugador2 == "piedra":
        print("Es un empate")
    elif jugador2 == "papel":
        print("Gana el jugador 2 porque papel gana a piedra")
    elif jugador2 == "tijera":
        print("Gana el jugador 1 porque piedra gana a tijera")

elif jugador1 == "papel":
    if jugador2 == "piedra":
        print("Gana el jugador 1 porque papel gana a piedra")
    elif jugador2 == "papel":
        print("Es un empate")
    elif jugador2 == "tijera":
        print("Gana el jugador 2 porque tijera gana a papel")

elif jugador1 == "tijera":
    if jugador2 == "piedra":
        print("Gana el jugador 2 porque piedra gana a tijera")
    elif jugador2 == "papel":
        print("Gana el jugador 1 porque tijera gana a papel")
    elif jugador2 == "tijera":
        print("Es un empate")

else:
    print("Los datos capturados no son válidos")

#-------ITERADORES--------

#Ejercicio 1: Imprimir números del 215 al 234
for n in range(215, 235):
    print(n)

#Ejercicio 2: Imprimir del 1 al 101 de 5 en 5
for m in range(1, 102, 5):
    print(m)

#Ejercicio 3: Sumar del 1 al 101 de 5 en 5
lista = []
for i in range(1, 102, 5):
    lista.append(i)
print( sum(lista) )

#Ejercicio 4: Sumar del 440 al 570 si es múltiplo de 3 o de 5
array = []
for idx in range(440, 571):
    if ( ( idx % 3 == 0) or ( idx % 5 == 0 ) ):
        array.append(idx)
print( sum(array) )

#Ejercicio 5: Sumar del 440 al 570 si es múltiplo de 3 y 5
arreglo = []
for idy in range(440, 571):
    if ( ( idy % 3 == 0) and ( idy % 5 == 0 ) ):
        arreglo.append(idy)
print( sum(arreglo) )

#-------CICLOS CONDICIONALES--------

#Ejercicio 1: Hacer un while, si número < 0 romper el ciclo
while True:
    print("Ingresa un número")
    num = input()
    if num < 0:
        break

#Ejercicio 2: Variable n = 100 y repite mientras n > 0. En el ciclo haz n = n / 1.5 e imprime el valor de n
c = 100
while c > 0:
    c = n/1.5
    print(c)

#Ejercicio 3: Capturar un punto y romper el ciclo si la distancia al origen es mayor a 10
while True:
   print("Ingresa X")
   puntoX = input()
   print("Ingresa Y")
   puntoY = input()
   distancia = ((puntoX ^ 2) + (puntoY ^ 2)) ** 0.5
   if distancia > 10:
       break

#Ejercicio 4: Romper un ciclo infinito si el texto es mayor a 6 dígitos
while True:
    print("Introduce un texto")
    texto = input()
    if len(texto) > 6:
        break

#Ejercicio 5: Si en el ejercicio 2, selecciona salir, salir del ciclo
while True:
    print("Selecciona una opción:\n 1. Imprimir reporte\n 2. Consultar reportes\n 3. Salir")
    seleccion = input()
    if seleccion == 1:
        print("Has seleccionado '1. Imprimir reporte'")
    elif seleccion == 2:
        print("Has seleccionado '2. Consultar reportes'")
    elif seleccion == 3:
        print("Has seleccionado '3. Salir'")
        break
