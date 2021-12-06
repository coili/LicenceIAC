from Vehicule import Vehicule

class Velo(Vehicule):
    
    def __init__(self, marque, vitesse, nbPlateaux):
        Vehicule.__init__(self, marque, vitesse)
        self.__nbPlateaux = nbPlateaux
        
    def getPlateaux(self):
        return self.__nbPlateaux
    
    def afficher(self):
        Vehicule.afficher(self)
        print("Nombre de plateaux : ", self.getPlateaux())