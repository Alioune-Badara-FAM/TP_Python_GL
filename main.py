from math import *
class Point(object):
    x : float
    y : float
    def __init__(self, abscisse, ordonee):
        self.x = abscisse
        self.y = ordonee
    def afficher(self):
        print("point(x = " + str(self.x) + ', y = ' + str(self.y) + ')')

class Cercle:
    centre : Point
    rayon : float
    def __init__(self,centre,rayon):
        self.centre = centre
        self.rayon = rayon
    def perimetre(self):
        return 2*pi*self.rayon
    def surface(self):
        return pi*pow(self.rayon,2)
    def appartenance(self, p:Point):
        if(sqrt(pow(self.centre.x - p.x, 2) + pow(self.centre.y - p.y, 2)) == self.rayon):
            return True
        else:
            return False
    def afficher(self):
        print("Le centre du cercle a pour abcisse x = " + str(self.centre.x) + ', ordonnee y = ' + str(self.centre.y) + ' et le rayon du cercle est de r = ' +  str(self.rayon) + ')')
class Cylindre(Cercle):
    hauteur : float
    def __init__(self, centre, rayon,  hauteur):
        Cercle.__init__(self, centre, rayon)
        self.hauteur = hauteur
    def volume(self):
        return pi * pow(self.rayon,2) * self.hauteur
if __name__ == '__main__':
    A = Point(6.3, 3.5)
    B = Point(4.8, 2.4)
    A.afficher()
    myCercle = Cercle(A,6)
    print("Le perimetre du cercle est de : ", myCercle.perimetre())
    print("La surface du cercle est de : ", myCercle.surface())
    print("Le point de cordonnee " , B.afficher() , " apparteint-il au cercle !? : " + str(myCercle.appartenance(B)))
    myCercle.afficher()
    cylindre = Cylindre(A,7.1,6.4)
    print("Le volume du cylindre est : ", cylindre.volume())
    
    
        
    



    


