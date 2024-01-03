class Livre :
    def __init__ (self) : 
        self.__titre = "The darkness"
        self.__auteur = "Jhonny D. Wagon"
        self.__pages = 250

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
        

livre = Livre ()

livre.set_pages ('&')