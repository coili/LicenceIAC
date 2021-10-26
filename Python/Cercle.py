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
    @param centre : centre du cercle, de type Point
    @param r : rayon du cercle
    """
    def __init__(self, nom, centre, r):
        assert isinstance(nom, str), "Le nom doit etre une chaine de caracteres."
        assert isinstance(centre, Point), "Le centre doit etre un point."
        assert isinstance(r, (int, float)), "Le rayon doit etre un nombre."

        self.__nom = nom
        self.__centre = centre
        self.__rayon = r
 

    """
    Getter de l'attribut nom
    @return nom : nom
    """
    def getNom(self):
        return self.__nom
    
    """
    Getter de l'attribut centre
    @return centre : centre du cercle
    """
    def getCentre(self):
        return self.__centre
    
    """
    Getter de l'attribut rayon
    @return rayon : rayon du cercle
    """
    def getRayon(self):
        return self.__rayon

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


    # Définitions des propriétés
    nom = property(getNom)
    centre = property(getCentre)
    rayon = property(getRayon)

