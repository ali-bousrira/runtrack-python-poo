class Point :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    
    def afficherLesPoints (self) :
        print ("les coordonnées des point sont " + str (self.x) + ", " + str (self.y))

    def afficherX (self) :
        print ("la valeur de x est " + str (self.x))

    def afficherY (self) : 
        print ("la valeur de y est " + str (self.y))

    def changerX (self) :
        self.x = int(input ("donner la nouvele valeur de x "))

    def changerY (self) :
        self.y = int(input ("donner la nouvele valeur de y "))


Point = Point (25 , 32)

Point.afficherLesPoints ()

Point.afficherX ()

Point.afficherY ()

Point.changerX ()

Point.changerY ()

Point.afficherX ()

Point.afficherY ()
