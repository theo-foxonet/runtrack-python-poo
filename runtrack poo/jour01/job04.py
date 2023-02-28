class Personne:
    def __init__(self, nom, prenom):
        self.nom=nom
        self.prenom=prenom
    def SePresenter(self):
        print(self.prenom, self.nom)

personne1= Personne("foxonet","billy")
personne1.SePresenter()