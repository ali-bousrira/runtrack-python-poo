class Forme :
    def aire (self) :
        return 0

class Cercle (Forme) :
    
    def __init__ (self, radius) :
        from math import pi
        self.radius = radius
        self.pi = float (format (pi, '.3f'))

    def aire (self) :
        return self.pi * self.radius ** 2
    
form = Forme ()
print ("l'aire est = " + str (form.aire ()))

cercle = Cercle (5) 
print ("l'aire est = " + str (cercle.aire ()))