class Personne :
    def __init__(self, nom, prenom) :
        self.nom = nom
        self.prenom = prenom

    def SePresenter (self, ) :
        print ("Je suis " + self.nom + " " + self.prenom)



personne1 = Personne ("Jhon", "Doe")

personne2 = Personne ("Jean", "Dupond")

personne3 = Personne ("Alexander", "Petersonne")

personne4 = Personne ("Bob", "Flean")

personne1.SePresenter ()
personne2.SePresenter ()
personne3.SePresenter ()
personne4.SePresenter ()