class Produit :
    def __init__ (self, nom, prixHT, TVA) :
        self.nom = nom
        self.prixHT = prixHT
        self.TVA =TVA

    def CalculerPrixTTC (self) :
        return self.prixHT + (self.prixHT * self.TVA / 100)
    
    def afficher (self) :
        return f"le nom du produit est {self.nom}, le prixHT est {self.prixHT} , le TVA est {self.TVA} et le prix TTC est {self.CalculerPrixTTC ()}"

    def modif_nom (self, nom) :
        self.nom = nom

    def modif_prix(self, prix):
        self.prixHT = prix

    def getNom(self):
        return self.nom

    def getPrix(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA


produit1 = Produit ('test', 25, 4)

print (produit1.afficher ())

produit1.modif_nom (input ("donner le nouvau nom du produit "))

produit1.modif_prix (int (input ("donner le nouveau prix ")))

print (produit1.getNom ())

print (produit1.getPrix ())

print (produit1.getTVA ())

