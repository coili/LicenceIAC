# coding: utf-8

"""
Classe Robot
@author Colin Senot
"""
class Robot:

    # Dictionnaire correspondant aux nouvelles directions, lors d'un virage à droite 
    dict_direction_droit = {
        'Est': 'Sud',
        'Ouest': 'Nord',
        'Nord': 'Est',
        'Sud': 'Ouest'
    }

    # Dictionnaire correspondant aux nouvelles directions, lors d'un virage à gauche
    dict_direction_gauche = {
        'Est': 'Nord',
        'Ouest': 'Sud',
        'Nord': 'Ouest',
        'Sud': 'Est'
    }

    """
    Constructeur de la classe
    @param nom : nom du robot
    @param abscisse : position x du robot
    @param ordonnee : position y du robot
    @param direction : direction du robot, par défaut Est
    """
    def __init__(self, nom, abscisse=0, ordonnee=0, direction="Est"):
        assert isinstance(nom, str), "Le nom doit etre une chaine de caracteres."
        assert isinstance(abscisse, int), "L'abscisse doit etre un entier."
        assert isinstance(ordonnee, int), "L'ordonnee doit etre un entier."
        assert isinstance(direction, str), "La direction doit etre une chaine de caracteres."

        self.__nom  = nom
        self.__abscisse = abscisse 
        self.__ordonnee = ordonnee
        self.__direction = direction

    """
    Setter de l'attribut nom
    @param nom : nouvelle nom
    """
    def setNom(self, nom):
        assert isinstance(nom, str), "Le nom doit etre une chaine de caracteres."
        self.__nom = nom

    """
    Getter de l'attribut nom
    @return nom : nom
    """
    def getNom(self):
        return self.__nom

    """
    Setter de l'attribut abscisse
    @param abscisse : nouvelle abscisse
    """
    def setAbscisse(self, abscisse):
        assert isinstance(abscisse, int), "L'abscisse doit etre un entier."
        self.__abscisse = abscisse

    """
    Getter de l'attribut abscisse
    @return abscisse : abscisse
    """
    def getAbscisse(self):
        return self.__abscisse

    """
    Setter de l'attribut ordonnee
    @param ordonnee : nouvelle ordonnee
    """
    def setOrdonnee(self, ordonnee):
        assert isinstance(ordonnee, int), "L'ordonnee doit etre un entier."
        self.__ordonnee = ordonnee

    """
    Getter de l'attribut ordonnee
    @return ordonnee : ordonnee
    """
    def getOrdonnee(self):
        return self.__ordonnee

    """
    Setter de l'attribut direction
    @param direction : nouvelle direction
    """
    def setDirection(self, direction):
        assert isinstance(direction, str), "La distance doit etre une chaine de caracteres."
        self.__direction = direction

    """
    Getter de l'attribut direction
    @return direction : direction
    """
    def getDirection(self):
        return self.__direction

    """
    Méthode permettant au robot d'avancer
    """
    def avance(self):
        if self.__direction == "Est":
            self.__abscisse += 1
        elif self.__direction == "Ouest":
            self.__abscisse -= 1
        elif self.__direction == "Nord":
            self.__ordonnee += 1
        else:
            self.__ordonnee -= 1

    """
    Méthode permettant au robot de tourner à droite
    """
    def droite(self):
        self.setDirection(self.__class__.dict_direction_droit[self.__direction])

    """
    Méthode permettant au robot de tourner à gauche
    """
    def gauche(self):
        self.setDirection(self.__class__.dict_direction_gauche[self.__direction])

    """
    Méthode permettant d'afficher l'état du robot
    @return affichage : affichage de l'état du robot
    """
    def __repr__(self):
        affichage = "Etat du robot " + self.__nom + " : \n" 
        affichage += "- Abscisse : " + str(self.__abscisse) + "\n"
        affichage += "- Ordonnée : " + str(self.__ordonnee) + "\n"
        affichage += "- Orientation : " + self.__direction + "\n"
        return affichage


    # Définitions des propriétés
    nom = property(getNom, setNom)
    abscisse = property(getAbscisse, setAbscisse)
    ordonnee = property(getOrdonnee, setOrdonnee)
    direction = property(getDirection, setDirection)