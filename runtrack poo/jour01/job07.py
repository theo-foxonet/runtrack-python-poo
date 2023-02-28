class Personnage:
    def __init__(self, x, y):
        self.matrice = [[1,2,3],[4,5,6],[7,8,9]]
        self.x = x
        self.y = y
        self.matrice1=self.matrice[self.x][self.y]

    def gauche(self):
        self.x = self.x -1
    def droite(self):
        self.x = self.x+1
    def bas(self):
        self.y = self.y +1
    def haut(self):
        self.y = self.y-1
    def position(self):
        valeurs=(self.x, self.y)
        print(valeurs)

perso1=Personnage(2,1)
perso1.gauche()
perso1.position()
perso1.haut()
perso1.position()
