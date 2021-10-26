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
        assert isinstance(numero, str), "Le numero doit etre une chaine de caracteres."
        assert isinstance(nom, str), "Le nom du compte doit etre une chaine de caracteres."
        assert isinstance(solde, int), "Le solde doit etre un entier."

        self.__numero = numero
        self.__nom = nom
        self.__solde = solde
        self.__decouvert = decouvert

    
    """
    Setter de l'attribut numero
    @param numero : nouveau numero
    """
    def setNumero(self, numero):
        assert isinstance(numero, str), "Le numero doit etre une chaine de caracteres."
        self.__numero = numero

    """
    Getter de l'attribut numero
    @return numero : numero du compte
    """
    def getNumero(self):
        return self.__numero

    """
    Setter de l'attribut nom
    @param nom : nouveau nom
    """
    def setNom(self, nom):
        assert isinstance(nom, str), "Le nom du compte doit etre une chaine de caracteres."
        self.__nom = nom

    """
    Getter de l'attribut nom
    @return nom : nom du compte
    """
    def getNom(self):
        return self.__nom

    """
    Setter de l'attribut solde
    @param solde : nouveau solde
    """
    def setSolde(self, solde):
        assert isinstance(solde, int), "Le solde doit etre un entier."
        self.__solde = solde

    """
    Getter de l'attribut solde
    @return solde : solde du compte
    """
    def getSolde(self):
        return self.__solde

    """
    Setter de l'attribut decouvert
    @param decouvert : nouveau decouvert
    """
    def setDecouvert(self, decouvert):
        assert isinstance(decouvert, bool), "Le decouvert doit etre un booleen."
        self.__decouvert = decouvert

    """
    Getter de l'attribut decouvert
    @return decouvert : decouvert du compte
    """
    def getDecouvert(self):
        return self.__decouvert


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


    # Définitions des propriétés
    nom = property(getNom, setNom)
    numero = property(getNumero, setNumero)
    solde = property(getSolde, setSolde)
    decouvert = property(getDecouvert, setDecouvert)


