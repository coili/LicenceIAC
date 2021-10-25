import math

"""
Classe Point
@author Colin Senot
"""
class Point:

    """
    Constructeur de la classe
    @param x : coordonnée X du point (par défaut, 0)
    @param y : coordonnée Y du point (par défaut, 0)
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    """
    Getter de l'attribut x
    @return x : coordonnée X du point
    """
    def getX(self):
        return self.x

    """
    Getter de l'attribut y
    @return y : coordonnée Y du point
    """
    def getY(self):
        return self.y

    """
    Méthode permettant de calculer la distance, entre deux points
    @param Point : deuxième point
    @return distance : distance entre deux points (instance et paramètre)
    """
    def distance(self, Point):
        point_x = Point.getX()
        point_y = Point.getY()

        distance = math.sqrt(pow((point_x - self.x), 2) + pow((point_y - self.y), 2))

        return round(distance, 3)
        


"""
=================
Mise en situation
=================
"""

A = Point(2, 3)
B = Point(4, 1)

print("Distance entre le point A et le point B : ", A.distance(B))