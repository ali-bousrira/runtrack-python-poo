class Personnage :
    
    def __init__ (self, x = 0, y = 0) :
        self.x = x
        self.y = y

    def gauche (self) :
        self.x -= 1

    def droit (self) :
        self.x += 1

    def haut (self) :
        self.y += 1

    def bas (self) :
        self.y -= 1

    def position (self) :
        return self.x, self.y
    

Personnage = Personnage ()

Personnage.gauche ()

print (Personnage.position ())

Personnage.haut ()

print (Personnage.position ())
