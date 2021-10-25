import math
from Exo3 import Point

"""
Classe Cercle
@author Colin Senot
"""
class Cercle:

    """
    Constructeur de la classe
    @param Point : centre du cercle
    @param r : rayon du cercle
    """
    def __init__(self, Point, r):
        self.centre = Point
        self.rayon = r

    """
    Méthode permettant d'obtenir le périmètre du cercle
    @return result : périmètre du cercle
    """
    def perimetre(self):
        result = 2 * math.pi * self.rayon
        return round(result, 2)

    """
    Méthode permettant d'obtenir la surface du cercle
    @return result : surface du cercle
    """
    def surface(self):
        result = math.pi * pow(self.rayon, 2)
        return round(result, 2) 

    """
    Méthode permettant de savoir si un point appartient au cercle
    @param Point : point à tester
    @return result : True si le point appartient au cercle
    """
    def testAppartenance(self, Point):
        result = False
        distance = round(self.centre.distance(Point), 1)

        if distance == self.rayon:
            result = True
        
        return result
        


"""
=================
Mise en situation
=================
"""
A = Point(4, -2)
cercle_1 = Cercle(A, 2)

print("Périmètre du cercle : ", cercle_1.perimetre())
print("Surface du cercle : ", cercle_1.surface())

B = Point(2, -2)

if cercle_1.testAppartenance(B):
    print("Le point B appartient au cercle.")
else:
    print("Le point B n'appartient pas au cercle.")

C = Point(4, 4)

if cercle_1.testAppartenance(C):
    print("Le point C appartient au cercle.")
else:
    print("Le point C n'appartient pas au cercle.")