# coding: utf-8

from Vehicule import Vehicule
from Moto import Moto
from Voiture import Voiture
from Velo import Velo

vehicule = Vehicule("Audi", 90)

vehicule.Rouler()
vehicule.Freiner()
vehicule.Polluer()

vehicule.Afficher()

print("\n")

moto = Moto("BMW", 100)
moto.Rouler()

print("\n")

velo = Velo("Btwin", 20, 6)
velo.Afficher()
velo.Polluer()

print("\n")

voiture = Voiture("Volkswagen", 200, 5)
voiture.Afficher()
voiture.AllumerAutoRadio()

try:
    voiture.RoueArriere()
except:
    print("Erreur: La voiture ne peut pas faire de roue arrière.")