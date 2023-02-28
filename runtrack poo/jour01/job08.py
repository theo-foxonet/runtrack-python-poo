class Cercle():
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, rayon):
        self.newrayon = rayon
        self.rayon = self.newrayon
        print("voici le nouveau rayon :", self.rayon)

    def afficherInfos(self):
        print(self.rayon)
        print(self.circonf)
        print(self.airevaleur)
        print(self.diam)
    
    def circonference(self):
        self.circonf = 2*3.14*(self.rayon)
        return("La circonférence du cercle est :",self.circonf)

    def aire(self):
        self.airevaleur = 3.14*(self.rayon*self.rayon) 
        return("L'aire du cercle est de :",self.airevaleur)

    def diametre(self):
        self.diam = 2*(self.rayon)
        return("Le diamètre du cercle est de :",self.diam)
Cercle1 = Cercle(4)
Cercle2 = Cercle1
Cercle1.circonference()
Cercle1.aire()
Cercle1.diametre()
Cercle1.afficherInfos()
Cercle2.changerRayon(7)
Cercle2.circonference()
Cercle2.aire()
Cercle2.diametre()
Cercle2.afficherInfos()