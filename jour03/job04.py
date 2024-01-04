class Joueur:
   def __init__(self, nom, numero, position, buts=0, passes=0, cartons_jaunes=0, cartons_rouges=0):
       self.nom = nom
       self.numero = numero
       self.position = position
       self.buts = buts
       self.passes = passes
       self.cartons_jaunes = cartons_jaunes
       self.cartons_rouges = cartons_rouges

   def marque_but(self):
       self.buts += 1

   def ajout_passe_dessicive(self):
       self.passes += 1

   def ajout_carton_joune(self):
       self.cartons_jaunes += 1

   def ajout_carton_rouge(self):
       self.cartons_rouges += 1

   def affiche_stat(self):
       print(f"Nom: {self.nom}\nNuméro: {self.numero}\nPosition: {self.position}\nButs: {self.buts}\nPasses: {self.passes}\nCartons Jaunes: {self.cartons_jaunes}\nCartons Rouges: {self.cartons_rouges}")


class Equipe:
   def __init__(self, nom):
       self.nom = nom
       self.joueurs = []

   def ajouterJoueur(self, joueur):
       self.joueurs.append(joueur)

   def affiche(self):
       for joueur in self.joueurs:
           joueur.affiche_stat()

   def maj_statistiques(self, joueur, buts=0, passes=0, cartons_jaunes=0, cartons_rouges=0):
       joueur.buts += buts
       joueur.passes += passes
       joueur.cartons_jaunes += cartons_jaunes
       joueur.cartons_rouges += cartons_rouges


joueur1 = Joueur('John Doe', 10, 'Attaquant')
joueur2 = Joueur('Jane Doe', 20, 'Défenseur')

equipe = Equipe('Equipe A')
equipe.ajouterJoueur(joueur1)
equipe.ajouterJoueur(joueur2)

equipe.affiche()

joueur1.marque_but()
joueur2.ajout_carton_rouge ()

equipe.maj_statistiques(joueur1, buts=1)
equipe.maj_statistiques(joueur2, cartons_rouges=1)

equipe.affiche()