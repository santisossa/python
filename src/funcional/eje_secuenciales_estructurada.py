# SECUENCIALES

num1 = int(input("ingrese primer valor:"))
num2 = int(input("ingrese segundo valor:"))
suma = num1+num2
producto = num1*num2
print("La suma de los dos valores es")
print(suma)
print("El producto de los dos valores es")
print(producto)

# CONDICIONALES

nota1 = int(input("Ingrese primer nota:"))
nota2 = int(input("Ingrese segunda nota:"))
nota3 = int(input("Ingrese tercer nota:"))
prom = (nota1+nota2+nota3)/3
if prom >= 7:
    print("Promocionado")
else:
    if prom >= 4:
        print("Regular")
    else:
        print("Reprobado")


# CICLOS

n = int(input("Ingrese el valor final:"))
x = 1
while x <= n:
    print(x)
    x = x+1

 # FOR-------------------------------------
suma = 0
for f in range(5):
    valor = int(input("Ingrese valor:"))
    suma = suma+valor
print("La suma es")
print(suma)
promedio = suma/10
print("El promedio es:")
print(promedio)
# FOREACH------------------------------
lista = [2, 3, 50, 7, 9]

for elemento in lista:
    print(elemento)

# LISTAS

lista = []
for x in range(5):
    valor = int(input("Ingrese valor:"))
    lista.append(valor)

menor = lista[0]
posicion = 0
for x in range(1, 5):
    if lista[x] < menor:
        menor = lista[x]
        posicion = x

print("Lista completa")
print(lista)
print("Menor de la lista")
print(menor)
print("Posicion del menor en la lista")
print(posicion)

# --------------------------------------

nombres = []
edades = []
for x in range(5):
    nom = input("Ingrese el nombre de la persona:")
    nombres.append(nom)
    ed = int(input("Ingrese la edad de dicha persona:"))
    edades.append(ed)

print("Nombre de las personas mayores de edad:")
for x in range(5):
    if edades[x] >= 18:
        print(nombres[x])

 # --------------------------------------

sueldos = []
for x in range(5):
    valor = int(input("Ingrese sueldo:"))
    sueldos.append(valor)

print("Lista sin ordenar")
print(sueldos)

for x in range(4):
    if sueldos[x] > sueldos[x+1]:
        aux = sueldos[x]
        sueldos[x] = sueldos[x+1]
        sueldos[x+1] = aux

print("Lista con el último elemento ordenado")
print(sueldos)

# --------------------------------------
sueldos = []
for x in range(5):
    valor = int(input("Ingrese sueldo:"))
    sueldos.append(valor)

print("Lista sin ordenar")
print(sueldos)

for k in range(4):
    for x in range(4):
        if sueldos[x] > sueldos[x+1]:
            aux = sueldos[x]
            sueldos[x] = sueldos[x+1]
            sueldos[x+1] = aux

print("Lista ordenada")
print(sueldos)

# --------------------------------------
alumnos = []
notas = []
for x in range(5):
    nom = input("Ingrese el nombre del alumno:")
    alumnos.append(nom)
    no = int(input("Ingrese la nota de dicho alumno:"))
    notas.append(no)

for k in range(4):
    for x in range(4-k):
        if notas[x] < notas[x+1]:
            aux1 = notas[x]
            notas[x] = notas[x+1]
            notas[x+1] = aux1
            aux2 = alumnos[x]
            alumnos[x] = alumnos[x+1]
            alumnos[x+1] = aux2

print("Lista de alumnos y sus notas ordenadas de mayor a menor")
for x in range(5):
    print(alumnos[x], notas[x])

# --------------------------------------
lista = [10, 20, 30, 40, 50]

print(lista)

print(lista.pop(0))
print(lista.pop(1))
print(lista.pop(2))

print(lista)


# CONVERTIR LISTAS A TUPLAS Y VICEVERSA

list(#parametro de tipo tupla)
tuple(#parametro de tipo lista)

# --------------------------------------
lista1 = [0, 1, 2, 3, 4, 5, 6]
lista2 = lista1[2:5]
print(lista2)  # 2,3,4
lista3 = lista1[1:3]
print(lista3)  # 1,2
lista4 = lista1[:3]
print(lista4)  # 0,1,2
lista5 = lista1[2:]
print(lista5)  # 2,3,4,5,6

# --------------------------------------

lista1 = [0, 1, 2, 3, 4, 5, 6]
print(lista1[-1])  # 6
print(lista1[-2])  # 5


# FUNCIONES

def presentacion():
    print("Programa que permite cargar dos valores por teclado.")
    print("Efectua la suma de los valores")
    print("Muestra el resultado de la suma")
    print("*******************************")


def carga_suma():
    valor1 = int(input("Ingrese el primer valor:"))
    valor2 = int(input("Ingrese el segundo valor:"))
    suma = valor1+valor2
    print("La suma de los dos valores es:", suma)


def finalizacion():
    print("*******************************")
    print("Gracias por utilizar este programa")


# programa principal

presentacion()
carga_suma()
finalizacion()

# --------------------------------------


def carga_suma():
    valor1 = int(input("Ingrese el primer valor:"))
    valor2 = int(input("Ingrese el segundo valor:"))
    suma = valor1+valor2
    print("La suma de los dos valores es:", suma)


def separacion():
    print("*******************************")


# programa principal

for x in range(5):
    carga_suma()
    separacion()

# --------------------------------------


def sumar(v1, v2, *lista):
    suma = v1+v2
    for x in range(len(lista)):
        suma = suma+lista[x]
    return suma


# bloque principal

print("La suma de 1+2")
print(sumar(1, 2))
print("La suma de 1+2+3+4")
print(sumar(1, 2, 3, 4))
print("La suma de 1+2+3+4+5+6+7+8+9+10")
print(sumar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# --------------------------------------


def sumar(v1, v2, v3):
    return v1 + v2 + v3


li = [2, 4, 5]
su = sumar(*li)
print(su)


# OBJETOS(Diccionarios)

def imprimir(paises):
    for clave in paises:
        print(clave, paises[clave])


# bloque principal

paises = {"argentina": 40000000, "españa": 46000000,
          "brasil": 190000000, "uruguay": 3400000}
imprimir(paises)


# Para consultar si una clave se encuentra en el diccionario podemos utilizar el operador in:
if clave in diccionario:
    print(diccionario[clave])
# Esto muy conveniente hacerlo ya que si no existe la clave produce un error al tratar de accederlo:
print(diccionario[clave])
