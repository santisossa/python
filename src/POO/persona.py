class Persona:

    def inicializar(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido = apellido
        self.edad = edad

    def imprimir(self):
        print("Nombre:",self.nombre,"Apellido:",self.apellido,"Edad:",self.edad)


# bloque principal

persona1=Persona()
persona1.inicializar("Santiago","Sossa",21)
persona1.imprimir()

persona2=Persona()
persona2.inicializar("Carla","morrison",30)
persona2.imprimir()