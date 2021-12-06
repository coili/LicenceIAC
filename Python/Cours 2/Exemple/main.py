from Vehicule import Vehicule
from Moto import Moto
from Voiture import Voiture
from Velo import Velo

vehicule = Vehicule("Audi", 90)

vehicule.rouler()
vehicule.freiner()
vehicule.polluer()

vehicule.afficher()

print("\n")

moto = Moto("BMW", 100)
moto.rouler()

print("\n")

velo = Velo("Btwin", 20, 6)
velo.afficher()

print("\n")

voiture = Voiture("Volkswagen", 200, 5)
voiture.afficher()