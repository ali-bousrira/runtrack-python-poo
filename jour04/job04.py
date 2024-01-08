class Forme :
    def aire (self) :
        return 0
    
class Rectangle (Forme) :
    def __init__ (self, largeur, longueur) :
        super().__init__()
        self.longueur =longueur
        self.largeur = largeur

    def aire (self) :
        return self.longueur * self.largeur
    
form = Forme ()
print ("l'aire est = " + str (form.aire ()))

rec = Rectangle (5,8)
print ("l'aire est = " + str (rec.aire ()))