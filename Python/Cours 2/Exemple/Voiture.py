# coding: utf-8

from Vehicule import Vehicule

class Voiture(Vehicule):
    
    def __init__(self, marque, vitesse, nbPortes):
        Vehicule.__init__(self, marque, vitesse)
        self.__nbPortes = nbPortes
        
    def GetPortes(self):
        return self.__nbPortes
    
    def Afficher(self):
        Vehicule.Afficher(self)
        print("Nombre de portes : ", self.__nbPortes)
        
    def AllumerAutoRadio(self):
        print("L'auto radio est allumé")