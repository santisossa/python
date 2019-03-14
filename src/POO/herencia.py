class Persona:

    def __init__(self):
        self.nombre=input("Ingrese el nombre:")
        self.edad=int(input("Ingrese la edad:"))

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)


class Empleado(Persona):

    def __init__(self):
        super().__init__()
        self.sueldo=float(input("Ingrese el sueldo:"))

    def imprimir(self):
        super().imprimir()
        print("Sueldo:",self.sueldo)

    def paga_impuestos(self):
        if self.sueldo>3000:
            print("El empleado debe pagar impuestos")
        else:
            print("No paga impuestos")


# bloque principal

persona1=Persona()
persona1.imprimir()
print("____________________________")
empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()
#------------------------------------------------------------------------------------------------------------------------------

class Operacion:

    def __init__(self):
        self.valor1=0
        self.valor2=0
        self.resultado=0

    def cargar1(self):
        self.valor1=int(input("Ingrese primer valor:"))

    def cargar2(self):
        self.valor2=int(input("Ingrese segundo valor:"))

    def mostrar_resultado(self):
        print(self.resultado)

    def operar(self):
        pass


class Suma(Operacion):

    def operar(self):
        self.resultado=self.valor1+self.valor2


class Resta(Operacion):

    def operar(self):
        self.resultado=self.valor1-self.valor2


# bloque princpipal

suma1=Suma()
suma1.cargar1()
suma1.cargar2()
suma1.operar()
print("La suma de los dos valores es")
suma1.mostrar_resultado()

resta1=Resta()
resta1.cargar1()
resta1.cargar2()
resta1.operar()
print("La resta de los valores es:")
resta1.mostrar_resultado()