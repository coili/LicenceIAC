class Rectangle:

    def __init__(self, longueurRectangle=0, largeurRectangle=0):
        self.__longueur = longueurRectangle
        self.__largeur = largeurRectangle


    """
    GETTER & SETTER
    """
    def getLongueur(self):
        return self.__longueur
    
    def getLargeur(self):
        return self.__largeur

    def setLongueur(self, longueurRectangle):
        self.__longueur = longueurRectangle
    
    def setLargeur(self, largeurRectangle):
        self.__largeur = largeurRectangle

    
    longueur = property(getLongueur, setLongueur)
    largeur = property(getLargeur, setLargeur)
    

""""
TEST
"""    
rectangle_1 = Rectangle(20, 30)
rectangle_2 = Rectangle(20, 20)
rectangle_3 = Rectangle()

print(rectangle_3.longueur)