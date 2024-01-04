class Tache:
   def __init__(self, titre, description, status):
       self.titre = titre
       self.description = description
       self.status = status

class ListeDeTaches:
   def __init__(self):
       self.taches = []

   def ajouterTache(self, tache):
       self.taches.append(tache)

   def supprimerTache(self, tache):
       self.taches.remove(tache)

   def marquerCommeFinie(self, tache):
       tache.status = "Terminé"

   def afficherListe(self):
       return self.taches

   def filterListe(self, status):
       return [tache for tache in self.taches if tache.status == status]

tache1 = Tache("tache 1", "Description de la tache 1", "À faire")
tache2 = Tache("tache 2", "Description de la tache 2", "À faire")
tache3 = Tache("tache 3", "Description de la tache 3", "Terminé")

listeDeTaches = ListeDeTaches()

listeDeTaches.ajouterTache(tache1)
listeDeTaches.ajouterTache(tache2)
listeDeTaches.ajouterTache(tache3)

listeDeTaches.supprimerTache(tache1)

listeDeTaches.marquerCommeFinie(tache2)

print(listeDeTaches.afficherListe())

print(listeDeTaches.filterListe("a faire"))