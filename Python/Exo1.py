"""
Classe CompteBancaire
@author : Colin Senot
"""
class CompteBancaire:

    """
    Constructeur de la classe
    @param numero : correspond au numéro du compte
    @param nom : nom du propriétaire
    @param solde : solde du compte
    """
    def __init__(self, numero, nom, solde):
        self.numero = numero
        self.nom = nom
        self.solde = solde

    """
    Méthode credit : ajoute une somme d'argent au solde
    @param somme : somme d'argent à ajouter
    """
    def credit(self, somme):
        self.solde += somme

    """
    Méthode debit : retire une somme d'argent au solde
    @param somme : somme d'argent à retirer
    """
    def debit(self, somme):
        self.solde -= somme

    """
    Méthode afficher : affiche les détails du compte
    """
    def afficher(self):
        print("Compte numéro : ", self.numero)
        print("Propriétaire : ", self.nom)
        print("Solde du compte : ", self.solde, " €")
