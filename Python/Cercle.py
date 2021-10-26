# coding: utf-8

import math
from Point import Point

"""
Classe Cercle
@author Colin Senot
"""
class Cercle:

    """
    Constructeur de la classe
    @param nom : nom du cercle
    @param Point : centre du cercle
    @param r : rayon du cercle
    """
    def __init__(self, nom, Point, r):
        self.__nom = nom
        self.__centre = Point
        self.__rayon = r

    """
    Méthode permettant d'obtenir le périmètre du cercle
    @return result : périmètre du cercle
    """
    def perimetre(self):
        result = 2 * math.pi * self.__rayon
        return round(result, 2)

    """
    Méthode permettant d'obtenir la surface du cercle
    @return result : surface du cercle
    """
    def surface(self):
        result = math.pi * pow(self.__rayon, 2)
        return round(result, 2) 

    """
    Méthode permettant de savoir si un point appartient au cercle
    @param Point : point à tester
    @return result : True si le point appartient au cercle
    """
    def testAppartenance(self, Point):
        result = False
        distance = round(self.__centre.distance(Point), 1)

        if distance == self.__rayon:
            result = True
        
        return result
        
    """
    Méthode permettant l'affichage des informations du cercle
    @return affichage : affiche les informations du cercle
    """
    def __repr__(self):
        affichage = "Informations concernant le cercle " + self.__nom + "\n"
        affichage += "- Centre : \n" + str(self.__centre) + "\n"
        affichage += "- Rayon : " + str(self.__rayon) + "\n"
        return affichage


"""
=================
Mise en situation
=================
"""

E = Point("E", -2, 1)
F = Point("F", 3, 1)
O = Point("O", 0, 0)

cercle = Cercle("C", E, 5)

print(cercle)

perimetre = "Perimetre du cercle : " + str(cercle.perimetre())
surface = "Surface du cercle : " + str(cercle.surface())

print(perimetre)
print(surface)

if cercle.testAppartenance(F):
    print("Le point F appartient au cercle.")
else:
    print("Le point F n'appartient pas au cercle.")

if cercle.testAppartenance(O):
    print("Le point O appartient au cercle.")
else:
    print("Le point O n'appartient pas au cercle.")