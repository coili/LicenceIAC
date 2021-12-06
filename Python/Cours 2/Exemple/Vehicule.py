# coding: utf-8

class Vehicule:
    
    def __init__(self, marque, vitesse):
        self.__marque = marque
        self.__vitesse = vitesse
        
    def afficher(self):
        print("Marque : ", self.getMarque())
        print("Vitesse : ", self.getVitesse())
        
    def getMarque(self):
        return self.__marque
    
    def getVitesse(self):
        return self.__vitesse
    
    def rouler(self):
        print("Le véhicule avance.")
        
    def freiner(self):
        print("Le véhicule freine.")
        
    def polluer(self):
        print("Le véhicule pollue.")