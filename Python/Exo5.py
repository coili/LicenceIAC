# coding: utf-8

"""
Classe Robot
@author Colin Senot
"""
class Robot:

    """
    Constructeur de la classe
    @param nom : nom du robot
    @param x : position x du robot
    @param y : position y du robot
    @param direction : direction du robot, par défaut Est
    """
    def __init__(self, nom, x=0, y=0, direction="Est"):
        self.__nom  = nom
        self.__x = x 
        self.__y = y
        self.__direction = direction

    """
    Setter de l'attribut direction
    @param direction : nouvelle direction
    """
    def setDirection(self, direction):
        self.__direction = direction

    """
    Méthode permettant au robot d'avancer
    """
    def avance(self):
        if self.__direction == "Est":
            self.__x += 1
        elif self.__direction == "Ouest":
            self.__x -= 1
        elif self.__direction == "Nord":
            self.__y += 1
        else:
            self.__y -= 1

    """
    Méthode permettant au robot de tourner à droite
    """
    def droite(self):
        if self.__direction == "Est":
            self.setDirection("Sud")
        elif self.__direction == "Ouest":
            self.setDirection("Nord")
        elif self.__direction == "Nord":
            self.setDirection("Est")
        else:
            self.setDirection("Ouest")

    """
    Méthode permettant au robot de tourner à gauche
    """
    def gauche(self):
        if self.__direction == "Est":
            self.setDirection("Nord")
        elif self.__direction == "Ouest":
            self.setDirection("Sud")
        elif self.__direction == "Nord":
            self.setDirection("Ouest")
        else:
            self.setDirection("Est")

    """
    Méthode permettant d'afficher l'état du robot
    @return affichage : affichage de l'état du robot
    """
    def __repr__(self):
        affichage = "Etat du robot " + self.__nom + " : \n" 
        affichage += "- Abscisse : " + str(self.__x) + "\n"
        affichage += "- Ordonnée : " + str(self.__y) + "\n"
        affichage += "- Orientation : " + self.__direction + "\n"
        return affichage


"""
=================
Mise en situation
=================
"""

robot = Robot("Asimo", 7, -2)

robot.avance()
robot.avance() 
robot.avance()  

robot.gauche()

robot.avance() 
robot.avance() 

robot.droite()

robot.avance()

print(robot)