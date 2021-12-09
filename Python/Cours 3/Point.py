# coding: utf-8

from math import sqrt

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
        assert len(nom) == 1, "Le nom doit etre une lettre."
        
        assert isinstance(abscisse, (int, float)), "L'abscisse doit etre un entier ou un float."
        assert isinstance(ordonnee, (int, float)), "L'ordonnee doit etre un entier ou un float."

        self.__nom = nom.upper()
        self.__abscisse = abscisse
        self.__ordonnee = ordonnee


    """
    Setter de l'attribut nom
    @param nom : nouveau nom
    """
    def SetNom(self, nom):
        assert isinstance(nom, str), "Le nom doit etre une chaine de caracteres."
        assert len(nom) == 1, "Le nom doit etre une lettre."
        
        self.__nom = nom.upper()  

    """
    Getter de l'attribut nom
    @return nom : nom
    """
    def GetNom(self):
        return self.__nom

    """
    Setter de l'attribut abscisse
    @param abscisse : nouvelle abscisse
    """
    def SetAbscisse(self, abscisse):
        assert isinstance(abscisse, (int, float)), "L'abscisse doit etre un entier ou un float."
        self.__abscisse = abscisse
    
    """
    Getter de l'attribut abscisse
    @return abscisse : coordonnée X du point
    """
    def GetAbscisse(self):
        return self.__abscisse

    """
    Setter de l'attribut ordonnee
    @param ordonnee : nouvelle ordonnee
    """
    def SetOrdonnee(self, ordonnee):
        assert isinstance(ordonnee, (int, float)), "L'ordonnee doit etre un entier ou un float."
        self.__ordonnee = ordonnee

    """
    Getter de l'attribut ordonnee
    @return ordonnee : coordonnée Y du point
    """
    def GetOrdonnee(self):
        return self.__ordonnee


    """
    Méthode permettant de calculer la distance, entre deux points
    @param Point : deuxième point
    @return distance : distance entre deux points (instance et paramètre)
    """
    def Distance(self, point):
        point_x = point.GetAbscisse()
        point_y = point.GetOrdonnee()

        distance = sqrt(pow((point_x - self.__abscisse), 2) + pow((point_y - self.__ordonnee), 2))

        return round(distance, 3)

    """
    Méthode permettant l'affichage des informations d'un point
    @return affichage : affiche les informations du point
    """
    def __repr__(self):
        affichage = self.__nom + '(' + str(self.__abscisse) + ';' + str(self.__ordonnee) + ')' 
        return affichage
        
    
    # Définitions des propriétés
    nom = property(SetNom, GetNom)
    abscisse = property(SetAbscisse, GetAbscisse)
    ordonnee = property(SetOrdonnee, GetOrdonnee)

