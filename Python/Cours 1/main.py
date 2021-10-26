# coding: utf-8

# Import des classes 
from Robot import Robot
from CompteBancaire import CompteBancaire
from Point import Point
from Cercle import Cercle

"""
=======================
Test de la classe Robot
=======================
"""

print("Test de la classe Robot :")

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


"""
================================
Test de la classe CompteBancaire
================================
"""

print("\nTest de la classe CompteBancaire :")

compte = CompteBancaire("120500045860", "Jeannot", 1000, True)

compte.debit(450)
compte.credit(200)

print(compte)

compte.debit(800)

print(compte)


"""
=======================
Test de la classe Point
=======================
"""

print("\nTest de la classe Point :")

A = Point("A", 2, 3)
B = Point("B", 4, 1)

print(A)

print("Distance entre le point A et le point B : ", A.distance(B))


"""
========================
Test de la classe Cercle
========================
"""

print("\nTest de la classe Cercle :")

E = Point("E", -2, 1)
F = Point("F", 3, 1)
O = Point("O", 0, 0)

cercle = Cercle("C", E, 5)

print(cercle)

perimetre = "Perimetre du cercle : " + str(cercle.perimetre())
surface = "Surface du cercle : " + str(cercle.surface())

print(perimetre)
print(surface)

if cercle.testAppartenance(F):
    print("Le point F appartient au cercle.")
else:
    print("Le point F n'appartient pas au cercle.")

if cercle.testAppartenance(O):
    print("Le point O appartient au cercle.")
else:
    print("Le point O n'appartient pas au cercle.")