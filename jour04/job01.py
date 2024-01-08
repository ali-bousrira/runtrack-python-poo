class Personne :
    def __init__ (self, age = 14) :
        self.age = age

    def afficherAge (self) :
        print ("l'age de cette personne est " + str (self.age))

    def bonjour (self) :
        print ("Hello")

    def modifAge (self, nouveau_age) :
        self.age = nouveau_age

    
class Eleve (Personne):


    def allerEnCours (self) :
        print ("Je vais en cours")

    def afficherAge (self) :
        print ("J'ais " + str (self.age) + " ans")


class Professeur (Personne):
    def __init__ (self, matiereEnseignée) :
        self.__matiere = matiereEnseignée

    def enseiger (self) :
        print ("Le cours va commencer")

jack = Personne ()

bob = Eleve ()

bob.afficherAge ()

