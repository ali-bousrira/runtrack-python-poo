import random

#cartes
class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

#distubution des cartes
class Jeu:
    def __init__(self):
        couleurs = ['Cœur', 'Carreau', 'Trèfle', 'Pique']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        self.paquet = [Carte(v, c) for v in valeurs for c in couleurs]

    def melanger(self):
        random.shuffle(self.paquet)

    def distribuer_cartes(self, nombre_cartes=2):
        cartes = []
        for _ in range(nombre_cartes):
            carte = self.paquet.pop()
            cartes.append(carte)
        return cartes

#jeux pricipal
class Blackjack:
    def __init__(self):
        self.jeu = Jeu()
        self.jeu.melanger()
        self.main_joueur = self.jeu.distribuer_cartes()
        self.main_enemy = self.jeu.distribuer_cartes()

    def calculer_points(self, main):
        total_points = 0
        nombre_as = 0

        for carte in main:
            if carte.valeur in ['Valet', 'Dame', 'Roi']:
                total_points += 10
            elif carte.valeur == 'As':
                nombre_as += 1
            else:
                total_points += int(carte.valeur)

        for _ in range(nombre_as):
            if total_points + 11 <= 21:
                total_points += 11
            else:
                total_points += 1

        return total_points

    def afficher_mains(self, afficher_enemy=False):
        print("Main du joueur:")
        for carte in self.main_joueur:
            print(f"{carte.valeur} de {carte.couleur}")

        if afficher_enemy:
            print("\nMain de l'nemy:")
            for carte in self.main_enemy:
                print(f"{carte.valeur} de {carte.couleur}")

    def jouer(self):
        while True:
            self.afficher_mains()
            points_joueur = self.calculer_points(self.main_joueur)

            if points_joueur == 21:
                print("Blackjack ! Vous avez gagné.")
                break
            elif points_joueur > 21:
                print("Vous avez dépassé 21. Vous avez perdu.")
                break

            action = input("Voulez-vous prendre une carte supplémentaire ? (oui/non): ")

            if action.lower() == 'oui':
                self.main_joueur.extend(self.jeu.distribuer_cartes())
            else:
                break

        points_enemy = self.calculer_points(self.main_enemy)

        while points_enemy < 17:
            self.main_enemy.extend(self.jeu.distribuer_cartes())
            points_enemy = self.calculer_points(self.main_enemy)

        self.afficher_mains(afficher_enemy=True)

        if points_joueur > 21:
            print("Vous avez dépassé 21. Vous avez perdu.")
        elif points_enemy > 21:
            print("Le enemy a dépassé 21. Vous avez gagné !")
        elif points_joueur > points_enemy:
            print("Vous avez plus de points que l'enemy. Vous avez gagné !")
        elif points_joueur < points_enemy:
            print("Le enemy a plus de points. Vous avez perdu.")
        else:
            print("Égalité !")


#program pricipal
if __name__ == "__main__":
    jeu_blackjack = Blackjack()
    jeu_blackjack.jouer()
