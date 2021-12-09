# coding: utf-8

from math import pi
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
    def GetNom(self):
        return self.__nom
    
    """
    Getter de l'attribut centre
    @return centre : centre du cercle
    """
    def GetCentre(self):
        return self.__centre
    
    """
    Getter de l'attribut rayon
    @return rayon : rayon du cercle
    """
    def GetRayon(self):
        return self.__rayon

    """
    Méthode permettant d'obtenir le périmètre du cercle
    @return result : périmètre du cercle
    """
    def Perimetre(self):
        result = 2 * pi * self.__rayon
        return round(result, 2)

    """
    Méthode permettant d'obtenir la surface du cercle
    @return result : surface du cercle
    """
    def Surface(self):
        result = pi * pow(self.__rayon, 2)
        return round(result, 2) 

    """
    Méthode permettant de savoir si un point appartient au cercle
    @param Point : point à tester
    @return result : True si le point appartient au cercle
    """
    def TestAppartenance(self, Point):
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
        affichage = "a faire" 
        return affichage


    # Définitions des propriétés
    nom = property(GetNom)
    centre = property(GetCentre)
    rayon = property(GetRayon)

