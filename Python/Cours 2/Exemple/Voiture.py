from Vehicule import Vehicule

class Voiture(Vehicule):
    
    def __init__(self, marque, vitesse, nbPortes):
        Vehicule.__init__(self, marque, vitesse)
        self.__nbPortes = nbPortes
        
    def getPortes(self):
        return self.__nbPortes
    
    def afficher(self):
        Vehicule.afficher(self)
        print("Nombre de portes : ", self.__nbPortes)
        
    def allumerAutoRadio(self):
        print("L'auto radio est allumé")