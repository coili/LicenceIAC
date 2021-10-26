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
    @param abscisse : coordonnée X du point (par défaut, 0)
    @param ordonnee : coordonnée Y du point (par défaut, 0)
    """
    def __init__(self, nom, abscisse=0, ordonnee=0):
        assert isinstance(nom, str), "Le nom doit etre une chaine de caracteres."
        assert isinstance(abscisse, int), "L'abscisse doit etre un entier."
        assert isinstance(ordonnee, int), "L'ordonnee doit etre un entier."

        self.__nom = nom
        self.__abscisse = abscisse
        self.__ordonnee = ordonnee


    """
    Setter de l'attribut nom
    @param nom : nouveau nom
    """
    def setNom(self, nom):
        assert isinstance(nom, str), "Le nom doit etre une chaine de caracteres."
        self.__nom = nom    

    """
    Getter de l'attribut nom
    @return nom : nom
    """
    def getNom(self):
        return self.__nom

    """
    Setter de l'attribut abscisse
    @param abscisse : nouvelle abscisse
    """
    def setAbscisse(self, abscisse):
        assert isinstance(abscisse, int), "L'abscisse doit etre un entier."
        self.__abscisse = abscisse
    
    """
    Getter de l'attribut abscisse
    @return abscisse : coordonnée X du point
    """
    def getAbscisse(self):
        return self.__abscisse

    """
    Setter de l'attribut ordonnee
    @param ordonnee : nouvelle ordonnee
    """
    def setOrdonnee(self, ordonnee):
        assert isinstance(ordonnee, int), "L'ordonnee doit etre un entier."
        self.__ordonnee = ordonnee

    """
    Getter de l'attribut ordonnee
    @return ordonnee : coordonnée Y du point
    """
    def getOrdonnee(self):
        return self.__ordonnee


    """
    Méthode permettant de calculer la distance, entre deux points
    @param Point : deuxième point
    @return distance : distance entre deux points (instance et paramètre)
    """
    def distance(self, Point):
        point_x = Point.getX()
        point_y = Point.getY()

        distance = math.sqrt(pow((point_x - self.__abscisse), 2) + pow((point_y - self.__ordonnee), 2))

        return round(distance, 3)

    """
    Méthode permettant l'affichage des informations d'un point
    @return affichage : affiche les informations du point
    """
    def __repr__(self):
        affichage = "Informations concernant le point " + self.__nom + "\n"
        affichage += "- Abscisse : " + str(self.__abscisse) + "\n"
        affichage += "- Ordonnée : " + str(self.__ordonnee) + "\n"
        return affichage
        
    
    nom = property(setNom, getNom)
    abscisse = property(setAbscisse, getAbscisse)
    ordonnee = property(setOrdonnee, getOrdonnee)
    

"""
=================
Mise en situation
=================
"""

A = Point("A", 2, 3)
B = Point("B", 4, 1)

print("Distance entre le point A et le point B : ", A.distance(B))