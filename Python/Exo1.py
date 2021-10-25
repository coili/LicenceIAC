# coding: utf-8

"""
Classe CompteBancaire
@author : Colin Senot
"""
class CompteBancaire:

    """
    Constructeur de la classe
    @param numero : correspond au numéro du compte
    @param nom : nom du titulaire
    @param solde : solde du compte
    @param decouvert : autorisé à être en découvert
    """
    def __init__(self, numero, nom, solde=0, decouvert=False):
        self.__numero = numero
        self.__nom = nom
        self.__solde = solde
        self.__decouvert = decouvert

    """
    Méthode credit : ajoute une somme d'argent au solde
    @param somme : somme d'argent à ajouter
    """
    def credit(self, somme):
        self.__solde += somme

    """
    Méthode debit : retire une somme d'argent au solde
    @param somme : somme d'argent à retirer
    """
    def debit(self, somme):
        self.__solde -= somme

    """
    Méthode afficher : affiche les détails du compte
    @return affichage : affiche les détails du compte
    """
    def __repr__(self):
        affichage = "Etat du compte numéro " + self.__numero + " : \n" 
        affichage += "- Propriétaire : " + self.__nom + "\n"
        affichage += "- Solde : " + str(self.__solde) + " €\n"
        affichage += "- Découvert autorisé : " + str(self.__decouvert) + "\n"
        return affichage


"""
=================
Mise en situation
=================
"""

compte = CompteBancaire("120500045860", "Jeannot", 1000, True)

compte.debit(450)
compte.credit(200)

print(compte)

compte.debit(800)

print(compte)