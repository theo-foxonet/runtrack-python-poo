class produit():
    def __init__(self, nom,prixHT,TVA):
        self.nom = nom
        self.prixHT= prixHT
        self.TVA = TVA


    def CalculerprixTTC(self):
        self.prixTTC = self.prixHT * self.TVA /100 + self.prixHT
        print("Le prix TTC est de :",self.prixTTC)

    def afficher(self):
        return self.nom, \
            self.prixHT, \
            self.prixTTC, \
            self.TVA
    
    def modifier(self, newnom, newprix):
        self.nom = newnom
        self.prixHT = newprix
        produit.CalculerprixTTC(self)
        print(produit.afficher(self))
produit1= produit("fanta",4,6)
produit1.CalculerprixTTC()
produit1.afficher()
produit1.modifier("coca", 5)
