class Commande :
    def __init__ (self, num, list = {}) :
        self.__num_comande = num
        self.__list_plat = list
        self.__statu_commande = "en cours"

    def ajout_comande (self, commande, prix) :
        self.__list_plat [commande] = prix

    def get_num_comande (self) :
        return self.__num_comande
    
    def get_list (self) :
        return self.__list_plat
    
    def get_statu (self) :
        return self.__statu_commande

    def annule (self) :
        self.__statu_commande = "Annulée"

    def __calcul (self) :
        total = 0
        for plat in self.__list_plat :
            total += int (self.__list_plat[plat])
        return total
    
    def affiche (self) :
        print ("la commande num " + str (self.__num_comande) + " avec", end =" ")
        for i in self.__list_plat :
            print ( i + " " + str (self.__list_plat[i]), end =" euro ")
        print ("va couter un total de " + str ( self.__calcul ()) + "euro est il sont " + self.__statu_commande)

    def calcul_TVA (self, tva) :
        total = self.__calcul ()
        return total * tva / 100

commandes = {
    "taco" : 7,
    "frit" : 3,
    "pizza" : 18,
}

test = Commande (5, commandes)


print (test.calcul_TVA (10))

test.affiche ()