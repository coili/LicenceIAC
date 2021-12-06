# coding: utf-8

class Vehicule:
    
    def __init__(self, marque, vitesse):
        self.__marque = marque
        self.__vitesse = vitesse
        
    def Afficher(self):
        print("Marque : ", self.GetMarque())
        print("Vitesse : ", self.GetVitesse())
    
    def GetMarque(self):
        return self.__marque
    
    def GetVitesse(self):
        return self.__vitesse
    
    def Rouler(self):
        print("Le véhicule avance.")
        
    def Freiner(self):
        print("Le véhicule freine.")
        
    def Polluer(self):
        print("Le véhicule pollue.")