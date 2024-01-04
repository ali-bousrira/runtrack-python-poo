class CompteBancaire :
    def __init__ (self, num, nom, prenom, solde, decouvert) :
        self.__num_compte = num
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher (self) :
        text = (f"le numéro de compte est: {self.__num_compte}, le nom complet d'utilisateur est:{self.__prenom} {self.__nom}, et le solde est de :{self.__solde}")
        print (text)
    
    def afficherSolde (self) :
        text = (f"le solde est : {self.__solde}")
        print (text)
    
    def versement (self, montant) :
        self.__solde += montant

    def retrait (self, montant) :
        if self.__solde >= montant :
            self.__solde -= montant
            text = (f"le nouveau solde est {self.__solde}")
            print (text)
        elif self.__decouvert == True:
            self.__solde -= montant
            text = (f"le nouveau solde est {self.__solde} !!!vous etes en decouvert!!!")
            print (text)
        else :
            print ("voutre solde est insufisant et vous a ves pas le droit au decouvert")

    def agios (self, taut) :
        if not self.__decouvert and self.__solde < 0:
            self.__solde -= self.__solde * taut /100
        else :
            print ("le agios ne saplique pas a se compte")
    
    def virement (self, destination, montant) :
        try :
            if self.__solde >= montant :
                    self.__solde -= montant
                    destination.versement (montant)
                    print ("virement executer avec succes")
            else :
                print ("votre solde n'est pas sufisant")
        except :
            print ("la distination nexiste pas")
                

jhonny = CompteBancaire (13, "Jack", "Jhonny", 789, True)
luke = CompteBancaire (7, "Luke", "Lucky", 987456, True)

luke.afficher ()
jhonny.afficher ()

jhonny.retrait (1000)
jhonny.afficherSolde ()

luke.virement (jhonny, 211)

luke.afficherSolde ()
jhonny.afficherSolde ()