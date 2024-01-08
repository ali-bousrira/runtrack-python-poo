class Vehicule :
    def __init__ (self, marque, modele, annee, prix) :
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule (self) :
        print (f"la marque est {self.marque}, le modele est {self.modele}, l'année est {self.annee} et le prix du vehicule est {self.prix}")

    def demarrer (self):
        print ("attention,je roule")

class Voiture (Vehicule) :
    def __init__ (self, marque, modele, annee, prix) :
        super().__init__(marque, modele, annee, prix)
        self.portes = 4

    def informationsVehicule (self) :
        print (f"la marque est {self.marque} \n le modele est {self.modele} \n l'année est {self.annee} \n le prix du vehicule est {self.prix} \n le nombre de portes est {self.portes}")

class Moto (Vehicule) :
    def __init__(self, marque, modele, annee, prix) :
        super().__init__(marque, modele, annee, prix)
        self.roue = 2

    def informationsVehicule (self) :
        print (f"la marque est {self.marque} \n le modele est {self.modele} \n l'année est {self.annee} \n le prix du vehicule est {self.prix} \n le nombre de roue est {self.roue}")

    def demarrer(self):
        print ("need for speed")


voiture = Voiture ("Mercedes","Classe A",2020,18500)
voiture.informationsVehicule ()
voiture.demarrer ()

moto = Moto ("Yamaha", "1200 Vmax", 1987, 4500)
moto.informationsVehicule ()
moto.demarrer ()