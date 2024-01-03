class Livre :
    def __init__ (self) : 
        self.__titre = "The darkness"
        self.__auteur = "Jhonny D. Wagon"
        self.__pages = 250
        self.__disponible = True

    def get_titre (self) :
        return self.__titre
    
    def get_auteur (self) :
        return self.__auteur
    
    def get_pages (self) :
        return self.__pages
    
    def set_titre (self, titre) :
        self.__titre = titre

    def set_auteur (self, auteur) :
        self.__auteur = auteur

    def set_pages (self, pages) :
        try :
            int (pages)
            if pages > 0 :
                self.__pages = pages
            else :
                print ("La largeur doit être un nombre entier positif")
        except :
            print ("La largeur doit être un nombre entier positif")

    def verification (self) :
        return self.__disponible
    

    def emprunter (self) :
        if self.verification () :
            self.__disponible = False
        else :
            print ("le livre n'est pas disponible")
    
    def rendre (self) :
        if not self.verification () :
            self.__disponible = True
        else :
            print ("le livre est deja rendu")

livre = Livre ()

livre.emprunter ()

print (livre.verification ())

livre.rendre ()

print (livre.verification ())