class Rectangle:

    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur


    """
    GETTER & SETTER
    """
    def getLongueur(self):
        return self.__longueur
    
    def getLargeur(self):
        return self.__largeur

    def setLongueur(self, longueur):
        self.__longueur = longueur
    
    def setLargeur(self, largeur):
        self.__largeur = largeur

    
    longueur = property(getLongueur, setLongueur)
    largeur = property(getLargeur, setLargeur)
    

""""
TEST
"""    
rectangle_1 = Rectangle(20, 30)
rectangle_2 = Rectangle(20, 20)