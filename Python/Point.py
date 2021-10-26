# coding: utf-8

import math

"""
Classe Point
@author Colin Senot
"""
class Point:

    """
    Constructeur de la classe
    @param nom : nom du point
    @param x : coordonnée X du point (par défaut, 0)
    @param y : coordonnée Y du point (par défaut, 0)
    """
    def __init__(self, nom, x=0, y=0):
        self.__nom = nom
        self.__x = x
        self.__y = y
    
    """
    Getter de l'attribut x
    @return x : coordonnée X du point
    """
    def getX(self):
        return self.__x

    """
    Getter de l'attribut y
    @return y : coordonnée Y du point
    """
    def getY(self):
        return self.__y

    """
    Méthode permettant de calculer la distance, entre deux points
    @param Point : deuxième point
    @return distance : distance entre deux points (instance et paramètre)
    """
    def distance(self, Point):
        point_x = Point.getX()
        point_y = Point.getY()

        distance = math.sqrt(pow((point_x - self.__x), 2) + pow((point_y - self.__y), 2))

        return round(distance, 3)

    """
    Méthode permettant l'affichage des informations d'un point
    @return affichage : affiche les informations du point
    """
    def __repr__(self):
        affichage = "Informations concernant le point " + self.__nom + "\n"
        affichage += "- Abscisse : " + str(self.__x) + "\n"
        affichage += "- Ordonnée : " + str(self.__y) + "\n"
        return affichage
        


"""
=================
Mise en situation
=================
"""

A = Point("A", 2, 3)
B = Point("B", 4, 1)

print("Distance entre le point A et le point B : ", A.distance(B))