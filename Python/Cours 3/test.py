'''
Create child class Animal of class ABC
Add abstract methode 'cri' with pass
'''                                                                      
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
        
    @abstractmethod
    def cri(self):
        pass
    

'''
Create child class Lion of class Animal
'''
class Lion(Animal):
    def cri(self):
        print("{} : Grrrr".format(self.name))
        
'''
Create child class owl of class Animal
'''
class Owl(Animal):
    def cri(self):
        print("{} : Je hulule".format(self.name))
        
        
alice = Owl("Alice")
samba = Lion("Samba")

alice.cri()
samba.cri()
