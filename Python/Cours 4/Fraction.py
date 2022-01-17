'''
Classe Fraction
'''
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        
    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)
    
    '''
    Operations
    '''
    def add(self, fraction):
        numerator = self.numerator * fraction.denominator + self.denominator * fraction.numerator
        denominator = self.denominator * fraction.denominator
        return Fraction(numerator, denominator).simplify()

    def substract(self, fraction):
        numerator = self.numerator * fraction.denominator - self.denominator * fraction.numerator
        denominator = self.denominator * fraction.denominator
        return Fraction(numerator, denominator).simplify()
    
    def multiply(self, fraction):
        numerator = self.numerator * fraction.numerator
        denominator = self.denominator * fraction.denominator
        return Fraction(numerator, denominator).simplify()
    
    def divide(self, fraction):
        numerator = self.numerator * fraction.denominator
        denominator = self.denominator * fraction.numerator
        return Fraction(numerator, denominator).simplify()
    
    
    '''
    Euclide pour simplifier les fractions
    '''
    def pgcd(self, a, b):
        if b == 0:
            return a
        return self.pgcd(b, a % b)
    
    def simplify(self):
        pgcd = self.pgcd(self.numerator, self.denominator)
        return Fraction(self.numerator // pgcd, self.denominator // pgcd)
    
    
    '''
    Getters and Setters
    '''
    def GetNumerator(self):
        return self.numerator
    
    def GetDenominator(self):
        return self.denominator
    
    def SetNumerator(self, numerator):
        self.numerator = numerator
        
    def SetDenominator(self, denominator):
        self.denominator = denominator

    
    
fraction1 = Fraction(1, 2)
fraction2 = Fraction(1, 3)
fraction3 = Fraction(6, 8)

print(fraction1.add(fraction2))
print(fraction3.simplify())
print(fraction3.pgcd(6, 8))

