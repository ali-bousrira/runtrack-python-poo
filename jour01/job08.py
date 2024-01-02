from math import pi

class Cercle :

    def __init__ (self, rayon = 5) :
        self.rayon = rayon

    def changerRayon (self) :
        self.rayon = int (input ("donner le nouvau rayon "))

    def circonférence (self) :
        return float (format (2 * float (format (pi, '.2f')) * self.rayon, '.2f'))
    
    def aire (self) :
        return float (format (float (format (pi, '.2f')) * self.rayon ** 2, '.2f'))
    
    def diametre (self) :
        return 2 * self.rayon
    
    def afficherInfos (self) :
        return f"le circonférence est {self.circonférence ()} et l'aire est {self.aire ()} et le diametre est {self.diametre ()}"
    


cercle = Cercle ()

print (cercle.afficherInfos ())
