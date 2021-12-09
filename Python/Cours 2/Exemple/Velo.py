# coding: utf-8

from Vehicule import Vehicule

class Velo(Vehicule):
    
    def __init__(self, marque, vitesse, nbPlateaux):
        Vehicule.__init__(self, marque, vitesse)
        self.__nbPlateaux = nbPlateaux
        
    def GetPlateaux(self):
        return self.__nbPlateaux
    
    def Afficher(self):
        Vehicule.Afficher(self)
        print("Nombre de plateaux : ", self.GetPlateaux())
        
    def RoueArriere(self):
        print("Je cabre.")
        
    def Polluer(self):
        print("Je pollue mais qu'un petit peu, ici on respecte l'environnement.")