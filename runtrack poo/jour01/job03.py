class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1=nombre1
        self.nombre2=nombre2
    def addition(self):
        somme=self.nombre1+self.nombre2
        print(somme)
initialisation= Operation(5, 4)
initialisation.addition()