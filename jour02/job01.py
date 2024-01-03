class Rectangle :
    def __init__ (self) :
        self.__longeur = 10
        self.__largeur = 5

    def get_longeur (self) :
        return self.__longeur
    
    def get_largeur (self) :
        return self.__largeur
    
    def set_longeur (self, x) :
        self.__longeur = x
    
    def set_largeur (self, x) :
        self.__largeur = x
    

rec = Rectangle ()

print (rec.get_longeur ())
print (rec.get_largeur ())


rec.set_longeur (8)
rec.set_largeur (3)

print (rec.get_longeur ())
print (rec.get_largeur ())