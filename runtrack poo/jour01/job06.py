class animal:
    def __init__(self, age, prenom):
        age2=input("veuillez rentrer un age")
        age==0
        self.age=age2
        self.prenom=prenom
        print(self.age)
    def vieillir(self):
        self.age=int(self.age)+1
        print(self.age)
Animal1 = animal(6, "bamby")
Animal1.vieillir()
