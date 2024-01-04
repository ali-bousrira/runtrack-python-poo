class Ville :
    def __init__ (self, nom, nom_abitant) :
        self.__nom = nom
        self.__nomb_abitant = nom_abitant

    def affiche_abitant (self) :
        return f"Population de la ville de {self.__nom}: {self.__nomb_abitant} habitants"
    
    def get_nom_abitant (self) :
        return self.__nomb_abitant
    
    def set_nomb_abitant (self, x) :
        self.__nomb_abitant = x

class Personne :
    def __init__ (self, nom, age, ville) :
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.__ajouterPopulation ()

    def __ajouterPopulation (self) :
        self.__ville.set_nomb_abitant ( self.__ville.get_nom_abitant () + 1)


paris = Ville ("Paris", 1000000)

print (paris.affiche_abitant ())

marseille = Ville ("Marseille", 861635)

print (marseille.affiche_abitant ())


jhon = Personne ("Jhon", 45, paris)
myrtille = Personne ("Myrtille", 4, paris)
chloé = Personne ("Chloé", 18, marseille)


print (paris.affiche_abitant ())
print (marseille.affiche_abitant ())