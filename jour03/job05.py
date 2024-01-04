from random import randint

class Personnage :
    def __init__ (self, nom = 0, vie = 0) :
        if nom == 0 :
            self.nom = input ("donnr le nom du personnage : ")
        self.vie = vie

    def modif_vie (self, x):
        self.vie += x

    def get_vie (self) :
        return (self.vie)

    def attaquer (self, enemy, test = 0) :
        if test == 0 :
            choi = input ("vouler vous attaque ? oui ou non :\n")
            while (not choi == "oui") and (not choi == "non") :
                choi = input ("vouler vous attaque ? oui ou non :\n")
            if choi == "oui":
                enemy.modif_vie (-randint (6, 12))
        else :
            enemy.modif_vie (-randint (6, 12))

class Jeux :
    def __init__ (self):
        self.list_dificult_joeur = [70, 50, 70, 70]
        self.list_dificult_enemy = [35, 50, 100, 125]

    def choisirNiveau (self) :
        while True:
            try:
                niveau = int(input("donner le niveau du jeux de 1 a 4: "))
                if 1 <= niveau <= 4 :
                    break
                else :
                    print ("le niveau n'est pas entre 1 et 4") 
            except ValueError:
                print("le nombre doint etre un entier")
        self.niveau =niveau
    
    def lancer_jeux (self) :
        joueur = Personnage (vie = self.list_dificult_joeur [self.niveau - 1])
        enemy = Personnage (nom = "enemy", vie = self.list_dificult_enemy [self.niveau - 1])
        print ("vous aver " + str (joueur.vie))
        print ("l'enemy à " + str (enemy.vie))
        lancer = True
        while lancer :

            joueur.attaquer (enemy)
            if joueur.vie <= 0:
                print ("vous aver perdue il rest " + str (enemy.vie) + " pv pour l'enemy")
                lancer = False
                print ("bonne chance la prochaine fois")
            enemy.attaquer (joueur, test = 1)
            if enemy.vie <= 0 :
                print ("vous aver gagner il vous rest " + str (joueur.vie) + " pv")
                lancer = False
                print ("bien jouer")
            print ("il vous rest " + str (joueur.vie) + " pv et l'enemy lui reste " + str (enemy.vie) + " pv")


    

jeux = Jeux ()

jeux.choisirNiveau ()

jeux.lancer_jeux ()