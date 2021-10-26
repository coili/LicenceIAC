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
        assert isinstance(longueurRectangle, (int, float)), "La longueur doit etre un nombre."
        assert longueurRectangle >= 0, "La longueur doit etre positive."
        self.__longueur = longueurRectangle
    
    def setLargeur(self, largeurRectangle):
        assert isinstance(largeurRectangle, (int, float)), "La largeur doit etre un nombre."
        assert largeurRectangle >= 0, "La largeur doit etre positive."
        self.__largeur = largeurRectangle
    

""""
TEST
"""    
rectangle_1 = Rectangle(20, 30)
rectangle_2 = Rectangle(20, 20)
rectangle_3 = Rectangle(20, 15)

rectangle_3.setLongueur(25)

print(rectangle_3.getLongueur())