import random
from math import sqrt as raiz, pow as elevar
import operaciones as operators

lista=operators.cargar()
operators.imprimir_mayor(lista)
operators.imprimir_suma(lista)

""" dado1=random.randint(1,6)
dado2=random.randint(1,6)
print("Primer dado:",dado1)
print("Segundo dado:",dado2)
suma=dado1+dado2
if suma==7:
    print("Gano")
else:
    print("Perdio") """

""" from math import sqrt, pow

valor = int(input("Ingrese un valor entero:"))
r1 = raiz(valor)
r2 = elevar(valor, 3)
print("La raiz cuadrada es", r1)
print("El cubo es", r2) """
