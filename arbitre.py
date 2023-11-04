import time
import random as r
import joueur_simple as j
import joueur_simple as t1
import joueur_simple as t2
import XinYimin as t3
import Sleepers_game as t4
import jeu_Ilias_Olive as t5
import licornes as t6
import Rambo as t7
import phantoms as t8

class Bracket:
    def __init__(self, lower1=None, lower2=None, p1 = None, p2 = None, end = False) -> None:
        self.p1 = p1
        self.p2 = p2
        self.lower1 = lower1
        self.lower2 = lower2
        self.winner = None
        self.end = end

    def update_winners(self):
        if self.lower1:
            if self.lower1.winner:
                self.p1 = self.lower1.winner
                self.p1.reset()
                self.end = True
            else:
                self.lower1.update_winners()

        if self.lower2:
            if self.lower2.winner:
                self.p2 = self.lower2.winner
                self.p2.reset()
                self.end = True
            else:
                self.lower2.update_winners()

    def run_sub_games(self):
        if self.lower1 and not self.lower1.winner:
            if not self.lower1.end:
                self.lower1.run_sub_games()
                self.lower2.run_sub_games()
            else:
                self.lower1.play_bracket()
                self.lower2.play_bracket()
        else:
            self.play_bracket()

    def play_bracket(self):
        game = Arbitre(self.p1, self.p2)
        self.winner = game.gameloop()

class Tournament:

    def __init__(self) -> None:
        player_list = [t1.Team(), t8.Phantoms(), t3.Anonyme(), t2.Team(), t5.jeu(), t6.Licornes(), t7.Rambo(), t4.Sleepers()]
        #player_list = [t8.Phantoms(), t8.Phantoms(), t8.Phantoms(), t8.Phantoms(), t4.Sleepers(), t4.Sleepers(), t4.Sleepers(), t4.Sleepers()]
        r.shuffle(player_list)
        self.p1 = player_list.pop()
        self.p2 = player_list.pop()
        self.p3 = player_list.pop()
        self.p4 = player_list.pop()
        self.p5 = player_list.pop()
        self.p6 = player_list.pop()
        self.p7 = player_list.pop()
        self.p8 = player_list.pop()

        self.win_bracket = Bracket(#7
                            Bracket(#5
                                    Bracket(None, None, self.p1, self.p2, True),#1
                                    Bracket(None, None, self.p3, self.p4, True))#2
                           ,Bracket(#6
                                    Bracket(None, None, self.p5, self.p6, True),#3
                                    Bracket(None, None, self.p7, self.p8, True)))#4
        self.draw_tourney()

    def draw_tourney(self):
        dessin_tournoi = []
        space = " "
        dessin_tournoi.append(f"{str(self.p1):_<15}__")
        dessin_tournoi.append(f"{space:<15}  |_#1_")
        dessin_tournoi.append(f"{str(self.p2):_<15}__|    |")
        dessin_tournoi.append(f"{space:<15}       |_#5___")
        dessin_tournoi.append(f"{str(self.p3):_<15}__     |      |")
        dessin_tournoi.append(f"{space:<15}  |_#2_|      |")
        dessin_tournoi.append(f"{str(self.p4):_<15}__|           |")
        dessin_tournoi.append(f"{space:<15}              |_#7")
        dessin_tournoi.append(f"{str(self.p5):_<15}__            |")
        dessin_tournoi.append(f"{space:<15}  |_#3_       |")
        dessin_tournoi.append(f"{str(self.p6):_<15}__|    |      |")
        dessin_tournoi.append(f"{space:<15}       |_#6___|")
        dessin_tournoi.append(f"{str(self.p7):_<15}__     |")
        dessin_tournoi.append(f"{space:<15}  |_#4_|")
        dessin_tournoi.append(f"{str(self.p8):_<15}__| ")

        for line in dessin_tournoi:
            print(line)

        time.sleep(5)
    #Joue tout les parties à rebourd
    def run_games(self):
        #Tant que le gagnant du duel pour la victoire est introuvé
        while self.win_bracket.winner is None:
            #Joue les parties plus creuses
            self.win_bracket.run_sub_games()
            #Si le gagnant n'est toujours pas trouvé, fais une mise à jour
            if not self.win_bracket.winner:
                self.update()
        print(f"{self.win_bracket.winner} gagne le tournoi!")
        Tournament.roll()
        return self.win_bracket.winner
        

    @staticmethod
    def roll():

        for i in range(30):
            pos = i % 4
            player = ""
            if pos == 0:
                player = "|"
            if pos == 1:
                player = "/"
            if pos == 2:
                player = "-"
            if pos == 3:
                player = "\\"
            left_space = i * " "
            #Si vous voulez le faire sur une seule ligne vous pouvez
            #utiliser le caractère spécial \r, faire un print sans retour de ligne
            print('\r' + left_space + player, end='')
            time.sleep(0.1)
        

    def update(self):
        self.win_bracket.update_winners()

class Arbitre:

    def __init__(self, player1:j.Joueur, player2:j.Joueur) -> None:
        self.starttime = time.time()
        self.currenttime = time.time()
        self.p1 = player1
        self.p2 = player2
        self.data1 = j.Joueur()
        self.data2 = j.Joueur()
        
    def gameloop(self) -> j.Joueur:
        TYPE_ACTION = ["Tir", "Recharge", "Bloque", "Faute"]
        sortie = False
        gagnant = None

        while not sortie:
            action_p1 = self.p1.action()
            action_p2 = self.p2.action()
            #Vérifie les appels de fautes et les valides
            if(action_p1 == TYPE_ACTION[3]):
                if self.data2.faute:
                    gagnant = self.p1
                    print(f"{self.p1} gagne avec un bon appel de faute!")
                else:
                    gagnant = self.p2
                    print(f"{self.p2} gagne dû à une mauvaise faute de {self.p1}")
                return gagnant

            if(action_p2 == TYPE_ACTION[3]):
                if self.data1.faute:
                    gagnant = self.p2
                    print(f"{self.p2} gagne avec un bon appel de faute!")
                else:
                    gagnant = self.p1
                    print(f"{self.p1} gagne dû à une mauvaise faute de {self.p2}")
                return gagnant
            
            #Met à jours les actions avant de mettre à jour les données
            self.data1.derniere_action = action_p1
            self.data2.derniere_action = action_p2

            #Exécute l'action de chaque joueuer sur l'autre (mets à jour les données)
            shot1 = getattr(self.data1, action_p1.lower())(self.data2)
            shot2 = getattr(self.data2, action_p2.lower())(self.data1)

            #Renvois l'actions aux joueurs respectifs
            self.p2.adversaire(action_p1)
            self.p1.adversaire(action_p2)

            #Sélectionne les symboles pour l'animation
            dessins1 = ["⌐ -", "˜⌐", ")"]
            dessins2 = ["- ¬", "¬˜", "("]
            dessin1 = dessins1[TYPE_ACTION.index(action_p1)]
            dessin2 = dessins2[TYPE_ACTION.index(action_p2)]
            avatar1 = "ß" if not shot1 else "X"
            avatar2 = "δ" if not shot2 else "X"
            space = 5*" "
            fill = 8*space
            #print(f"{self.p1} [{self.data1.vies}] {avatar1}{dessin1:>3}{space}{dessin2:3}{avatar2} [{self.data2.vies}] {self.p2} ", end='\r')
            #time.sleep(0.20)
            
            #Vérifie les conditions de victoire
            if self.data1.vies <= 0 or self.data2.vies <= 0:
                sortie = True

            if self.data1.vies <= 0 and self.data2.vies <= 0:
                print("")
                gagnant = r.sample([self.p1, self.p2], 1)[0]
                sortie = True
                print(f"Égalité! Le gagnant aléatoire est {gagnant}!")

            elif self.data1.vies <= 0:
                gagnant = self.p2
                sortie = True
                print(f"{self.p2} gagne!{fill}")

            elif self.data2.vies <= 0:
                gagnant = self.p1
                sortie = True
                print(f"{self.p1} gagne!{fill}")

            #Vérifie que le jeu ne dépasse pas le temps alloué
            #et pénalise le joueur ayant le plus bloqué 
            #avant l'arrêt de jeu
            self.currenttime = time.time()
            if self.currenttime-self.starttime > 20:
                bc1 = self.data1.bloque_compteur
                bc2 = self.data2.bloque_compteur
                if  bc1 > bc2:
                    gagnant = self.p2
                    print(f"Pénalité {bc1}:{bc2}, {self.p2} gagne!")
                    sortie = True
                elif bc2 > bc1:
                    gagnant = self.p1
                    print(f"Pénalité {bc1}:{bc2}, {self.p1} gagne!")
                    sortie = True
                else:
                    gagnant = r.sample([self.p1, self.p2], 1)[0]
                    print(f"Pénalité {bc1}:{bc2} et Égalité! Le gagnant aléatoire est {gagnant}!")
                    sortie = True
        return gagnant
            
tourney = Tournament()
#tourney.draw_tourney()
tourney.run_games()
