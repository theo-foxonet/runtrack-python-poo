class point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    
    def afficherLesPoints(self):
        print("les coordonées de x et y sont ", self.x, self.y)
    
    def afficherX(self):
        print("X:", self.x)
    
    def afficherY(self):
        print("Y:", self.y)
    def changerX(self):
        x2=6
        y2=74
        self.x=x2
        self.y=y2
        print("les coordonées ont été changé:", self.y, self.x)

point1=point(65, 63)
point1.afficherLesPoints()
point1.afficherX()
point1.afficherY()
point1.changerX()
