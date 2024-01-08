class Rectangle :
    def __init__ (self, longueur = 5, larger = 2) :
        self.__longueur = longueur
        self.__larger = larger

    def perimetre (self) :
        return self.__larger * 2 + self.__longueur * 2
        
    def surface (self) :
        return self.__larger * self.__longueur

    def get_largeur (self) :
        return (self.__larger)
    
    def get_longueur (self) :
        return (self.__longueur)
    
    def set_largeur (self, x) :
        self.__larger = x

    def set_longeur (self, x) :
        self.__longueur = x

class Parallelepipede (Rectangle) :
    def __init__ (self, hauteur) :
        super().__init__()
        self.hauteur = hauteur
    
    def volume (self) :
        return self.surface () * self.hauteur

rec = Rectangle ()

para = Parallelepipede (4)

print ("longeur = " + str (rec.get_longueur ()))
print ("largeur = " + str (rec.get_largeur ()))
print ("perimetre = " + str (rec.perimetre ()))
print ("surface = " + str (rec.surface ()))

rec.set_longeur (15)
rec.set_largeur (8)

print ("longeur = " + str (rec.get_longueur ()))
print ("largeur = " + str (rec.get_largeur ()))

print ("hauteur = " + str (para.hauteur))
print ("volume = " + str (para.volume ()))
