class Animal :
    def __init__(self) :
        self.age = 0
        self.prenom = ""

    def vieillir (self) :
        self.age += 1

    def print_age (self) :
        print ("l'age de l'animal " + str (self.age) + " ans")

    def nommer (self) :
        self.prenom = input ("donner le nom de lanimal ")

    def print_prenom (self) : 
        print ("L'animal se nomme " + self.prenom)


animal1 = Animal ()

animal1.print_age ()

animal1.vieillir ()

animal1.print_age ()

animal1.nommer ()

animal1.print_prenom ()