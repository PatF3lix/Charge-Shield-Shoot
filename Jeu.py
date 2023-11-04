from random import randint
# Python3 code to demonstrate working of
# N largest values in dictionary
# Using sorted() + itemgetter() + items()
from operator import itemgetter
from jeu2 import Sleepers as Sleepers3
from jeu3 import *
from jeu3 import Sleepers as Sleepers4
from jeu4 import *
from jeu4 import Sleepers as Sleepers5
from Sleepers_game import *
from Sleepers_game import Sleepers as contender
from Anonyme import *
import time

# # de balles
# 0 :  almanach(moves)
# 1 :  almanach(moves)
# 2 :  almanach(moves)
# 3 :  almanach(moves)
# objet almanach qui garde des moves (dict)
    # methodes pour updater count et prob
# objet move
class Move:
    def __init__(self, move: tuple) -> None:
        self.move_tuple = move
        self.occurence = 1
        self.probabilite = 0
    
    def __repr__(self) -> str:
        return f"{self.occurence} - {self.probabilite}"

    def __eq__(self, other_move: object) -> bool:
        return self.move_tuple == other_move.move_tuple
    
    def __gt__(self, other_move: object) -> bool:
        status = self.probabilite > other_move.probabilite
        return status


class Almanach:
    def __init__(self) -> None:
        self.almanach = {}
        self.nb_moves = 0

    def set_prob(self) -> None:
        for move in self.almanach:
            self.almanach[move].probabilite = self.almanach[move].occurence / self.nb_moves

    def add_move(self, a_move: Move):
        if a_move.move_tuple in self.almanach:
            self.almanach[a_move.move_tuple].occurence += 1
            self.nb_moves += 1
            self.set_prob()
        else:
            self.almanach[a_move.move_tuple] = a_move
            self.nb_moves += 1
            self.set_prob()

class Guesser:
    def __init__(self) -> None:
        self.nostra_dict = {
            3: Almanach(),
            2: Almanach(),
            1: Almanach(), 
            0: Almanach(),
        }
    
    def __str__(self) -> str:
        string = ""
        for key, value in self.nostra_dict.items():
            string += f"{key} balle:"
            for move, move_object in value.almanach.items():
                string += f" {move} - {move_object.probabilite} - {move_object.occurence}"
            string += "\n"
        return string


class Moves:
    NB_MOVES = 0
    TOUT_MOVES = {}
    
    def __init__(self, move: str) -> None:
        self.move = move
        self.occurence = 1
        self.probabilite = 0
        Moves.TOUT_MOVES[self.move] = self
        Moves.NB_MOVES += 1
    
    def __repr__(self) -> str:
        return f"{self.occurence} - {self.probabilite}"

    def __eq__(self, other_word: object) -> bool:
        return self.probabilite == other_word.probabilite
    
    def __gt__(self, other_word: object) -> bool:
        status = self.probabilite > other_word.probabilite
        return status
    
    @staticmethod
    def set_occurence(un_move: str) -> None:
        if un_move not in Moves.TOUT_MOVES.keys():
            Moves(un_move)
        else:
            Moves.TOUT_MOVES[un_move].occurence += 1
            Moves.NB_MOVES += 1

    @staticmethod
    def set_prob() -> None:
        for mot in Moves.TOUT_MOVES.values():
            mot.probabilite = mot.occurence / Moves.NB_MOVES

    @staticmethod
    def reset_moves() -> None:
        Moves.NB_MOVES = 0
        Moves.TOUT_MOVES = {}

def give_meaning(almanach_dict: dict) -> str:
    """
    Source: https://www.geeksforgeeks.org/python-n-largest-values-in-dictionary/
    Utilisation 10 highest result in dict
    User: manjeet_04
    """
    dict = almanach_dict
    # N largest values in dictionary
    # Using sorted() + itemgetter() + items()
    res = dict(sorted(dict.items(), key = itemgetter(1), reverse = True))
    meaning = ""
    for move in res:
        meaning += f"{move} - {res[move].probabilite}\n"
    return meaning

class Sleepers:
    TYPE_ACTION = ["Tir", "Recharge", "Bloque", "Faute"]
    OUR_LAST_ACTION = ""
    STATUS = "ANALYSE"
    ANALYSE_GOAL = 100000000
    ANALYSE = 0

    ENNEMY_LAST_ACTION = ""
    CONSECUTIVE_BLOCK = 0
    ALL_ACTIONS = []

    ENNEMY_BULLETS = 1
    ENNEMY_LIFE_LOST = 0
    ENNEMY_BULLETS_FIRED = 0
    ENNEMY_RECHARGED = 0
    
    def __init__(self) -> None:
        self.vies = 3
        self.munition_chargee = 1
        self.guesser = Guesser()
        self.reset()

    def etat(self) -> tuple:
        return self.vies, self.munition_chargee

    def foul_play(self) -> bool:
        if Sleepers.ENNEMY_BULLETS > 3:
            return True
        if Sleepers.ENNEMY_BULLETS_FIRED > Sleepers.ENNEMY_RECHARGED + 1:
            return True
        if Sleepers.ENNEMY_LIFE_LOST == 3:
            return True
        if Sleepers.ENNEMY_LAST_ACTION == "Erreur":
            return True
        
    def next_action(self, last_action: str) -> str:
        ennemy_bullets = Sleepers.ENNEMY_BULLETS
        almanach_etat_actuel = self.guesser.nostra_dict[ennemy_bullets]
        moves = almanach_etat_actuel.almanach
        more_probable = dict(sorted(moves.items(), key = itemgetter(1), reverse = True))
        choices = []
        for name in more_probable:
            if name[0] == last_action:
                choices.append((name, more_probable[name]))
        if len(choices) > 0:
            if len(choices) > 1:
                test_same_prop = {}
                for name in choices:
                    test_same_prop[name[0]] = name[1]
                
                all_same = True
                test_prob = list(test_same_prop.values())[0].probabilite
                for name in test_same_prop:
                    if test_same_prop[name].probabilite != test_prob:
                        all_same = False
                        break
            
                if all_same:
                    found_tir = False
                    for name_move in choices:
                        if name_move[0][1] == "Tir":
                            found_tir = True
                    
                    if found_tir and self.vies < 2:
                        next_act = "Tir"
                    else:
                        next_act = "Bloque"
                else:
                    next_act = choices[0][0][1]
            else:
                next_act = choices[0][0][1]
                if next_act == "Tir":
                    next_act == "Bloque"
        else:
            next_act = "Bloque"
        return next_act
    
    def mode_atk(self) -> str:
        next_act = self.next_action(Sleepers.ENNEMY_LAST_ACTION)
        if next_act == "Recharge" and self.munition_chargee > 0:
            self.munition_chargee -= 1
            return "Tir"
        elif next_act == "Recharge" and self.munition_chargee <= 0:
            self.munition_chargee += 1
            return "Recharge"
        elif next_act == "Tir":
            return "Bloque"
        elif next_act == "Bloque" and self.munition_chargee < 3:
            self.munition_chargee += 1
            return "Recharge"
        else:
            return "Bloque"

    def decide_action(self) -> str:
        if Sleepers.STATUS == "ANALYSE":
            if Sleepers.ANALYSE >= Sleepers.ANALYSE_GOAL:
                Sleepers.STATUS = "ATK"
                return self.mode_atk()
            else:
                return "Bloque"
        elif Sleepers.STATUS == "ATK":
            return self.mode_atk()
    
    def block_block(self):
        is_block_strat = False
        if Sleepers.CONSECUTIVE_BLOCK > 10000:
            Sleepers.CONSECUTIVE_BLOCK = 0
            is_block_strat = True
        return is_block_strat

    def action(self) -> str:
        if self.foul_play():
            action = "Faute"
            return action
        elif self.block_block():
            if self.munition_chargee > 0 and Sleepers.ENNEMY_BULLETS == 0:
                action = "Tir"
                self.munition_chargee -= 1
            else:
                if self.munition_chargee > 0:
                    action = "Tir"
                    self.munition_chargee -= 1
                else:
                    action = "Recharge"
        else:
            if self.munition_chargee > 0 and Sleepers.ENNEMY_BULLETS == 0:
                action = "Tir"
                self.munition_chargee -= 1
            elif self.munition_chargee <= 0 and Sleepers.ENNEMY_BULLETS == 0:
                action = "Recharge"
                self.munition_chargee += 1
            else:
                action = self.decide_action()

        Sleepers.OUR_LAST_ACTION = action
        return action

    def adversaire(self, action: str) -> None:
        if Sleepers.ENNEMY_LAST_ACTION != "":
            ennemy_bullets = Sleepers.ENNEMY_BULLETS
            dict = self.guesser.nostra_dict[ennemy_bullets]
            this_move = Move((Sleepers.ENNEMY_LAST_ACTION, action))
            dict.add_move(this_move)
            Sleepers.ANALYSE += 1
        if action in Sleepers.TYPE_ACTION:
            if Sleepers.OUR_LAST_ACTION == "Tir" and action != "Bloque":
                Sleepers.ENNEMY_LIFE_LOST += 1
            if Sleepers.OUR_LAST_ACTION != "Bloque" and action == "Tir":
                if Sleepers.ENNEMY_BULLETS > 0:
                    self.vies -= 1
                elif Sleepers.ENNEMY_BULLETS <= 0:
                    Sleepers.ENNEMY_LAST_ACTION = "Erreur"
            if action == "Tir" and Sleepers.ENNEMY_BULLETS > 0:
                Sleepers.ENNEMY_BULLETS -= 1
                Sleepers.ENNEMY_BULLETS_FIRED += 1
            
            if action == "Bloque" and Sleepers.ENNEMY_LAST_ACTION == "Bloque":
                all_block = True
                last_hundo = Sleepers.ALL_ACTIONS
                for act in last_hundo:
                    if act != "Bloque":
                        all_block = False
                if all_block:
                    Sleepers.CONSECUTIVE_BLOCK += 1
            if action == "Recharge" and Sleepers.ENNEMY_BULLETS < 3:
                Sleepers.ENNEMY_RECHARGED += 1
                Sleepers.ENNEMY_BULLETS += 1
            if len(Sleepers.ALL_ACTIONS) >= 100:
                Sleepers.ALL_ACTIONS.pop(0)
                Sleepers.ALL_ACTIONS.append(action)
            else:
                Sleepers.ALL_ACTIONS.append(action)
            Sleepers.ENNEMY_LAST_ACTION = action
        else:
            Sleepers.ENNEMY_LAST_ACTION = "Erreur"

    def reset(self):
        Sleepers.OUR_LAST_ACTION = ""
        Sleepers.STATUS = "ANALYSE"
        Sleepers.ANALYSE = 0

        Sleepers.ENNEMY_LAST_ACTION = ""

        Sleepers.ENNEMY_BULLETS = 1
        Sleepers.ENNEMY_LIFE_LOST = 0
        Sleepers.ENNEMY_BULLETS_FIRED = 0
        Sleepers.ENNEMY_RECHARGED = 0

class Sleepers2:
    TYPE_ACTION = ["Tir", "Recharge", "Bloque", "Faute"]
    OUR_LAST_ACTION = ""

    ENNEMY_LAST_ACTION = ""

    ENNEMY_BULLETS = 1
    ENNEMY_LIFE_LOST = 0
    ENNEMY_BULLETS_FIRED = 0
    ENNEMY_RECHARGED = 0
    
    def __init__(self) -> None:
        self.vies = 3
        self.munition_chargee = 1

    def etat(self) -> tuple:
        return self.vies, self.munition_chargee

    def foul_play(self) -> bool:
        if Sleepers.ENNEMY_BULLETS > 3:
            return True
        if Sleepers.ENNEMY_BULLETS_FIRED > Sleepers.ENNEMY_RECHARGED + 1:
            return True
        if Sleepers.ENNEMY_LIFE_LOST == 3:
            return True
        if Sleepers.ENNEMY_LAST_ACTION == "Erreur":
            return True
        
    
    def availible_options(self) -> list:
        availible_actions = ["Bloque"]
        if 0 < self.munition_chargee <= 3:
            availible_actions.append("Tir")
        if self.munition_chargee < 3:
            availible_actions.append("Recharge")
        return availible_actions


    def action(self) -> str:
        if self.foul_play():
            action = "Faute"
            return action
        else:
            availible_actions = self.availible_options()
            
            nb_actions = len(availible_actions)-1
            action = availible_actions[randint(0,nb_actions)]
            
            if action == "Tir" and self.munition_chargee > 0:
                self.munition_chargee -= 1
            elif action == "Recharge" and self.munition_chargee < 3:
                self.munition_chargee += 1
            elif action == "Bloque":
                pass

            Sleepers2.OUR_LAST_ACTION = action
            return action

    def adversaire(self, action: str) -> None:
        if action in Sleepers2.TYPE_ACTION:
            if Sleepers2.OUR_LAST_ACTION == "Tir" and action != "Bloque":
                Sleepers2.ENNEMY_LIFE_LOST += 1
            if Sleepers2.OUR_LAST_ACTION != "Bloque" and action == "Tir":
                self.vies -= 1
            if action == "Tir":
                Sleepers2.ENNEMY_BULLETS -= 1
                Sleepers2.ENNEMY_BULLETS_FIRED += 1
            if action == "Recharge":
                Sleepers2.ENNEMY_RECHARGED += 1
                Sleepers2.ENNEMY_BULLETS += 1
            Sleepers2.ENNEMY_LAST_ACTION = action
        else:
            Sleepers2.ENNEMY_LAST_ACTION = "Erreur"
    
    @staticmethod
    def reset():
        Sleepers2.OUR_LAST_ACTION = ""

        Sleepers2.ENNEMY_LAST_ACTION = ""

        Sleepers2.ENNEMY_BULLETS = 1
        Sleepers2.ENNEMY_LIFE_LOST = 0
        Sleepers2.ENNEMY_BULLETS_FIRED = 0
        Sleepers2.ENNEMY_RECHARGED = 0

def game():
    # winning_moves = {}
    win_counter = 0
    lost_counter = 0
    # for x in range(1):
    # Moves.reset_moves()
    # # Sleepers.reset()
    # Sleepers4.reset()
    # Sleepers2.reset()
    # Sleepers5.reset()
    # player1 = Sleepers()
    # player1 = Sleepers3()
    # player1 = Sleepers5()
    player1 = contender()
    player2 = Anonyme()
    # player2 = Sleepers4()
    # player2 = Sleepers3()
    # player2 = Sleepers5()
    # this_game_moves = []
    # this_game_moves_p2 = []
    bloque_compteur1 = 0
    bloque_compteur2 = 0
    p2_last_action = ""
    starttime = time.time()
    currenttime = time.time()

    sortir = False
    while not sortir:
        coup_p1 = player1.action()
        # this_game_moves.append(coup_p1)

        coup_p2 = player2.action()
        # this_game_moves_p2.append(coup_p2)

        print(f"{coup_p1} - Moi: {player1.vies} vies")
        print(f"{coup_p2} - Adversaire: {player2.vie} vies")

        if coup_p1 == "Faute":
            print("Player 1 call foul")
            sortir = True

        if coup_p2 == "Faute":
            print("Player 2 call foul")
            sortir = True

        player1.adversaire(coup_p2)
        player2.adversaire(coup_p1)

        if player1.OUR_LAST_ACTION == "Bloque" and coup_p1 == "Bloque":
            bloque_compteur1 += 1
        else:
            bloque_compteur1 = 0

        if p2_last_action == "Bloque" and coup_p2 == "Bloque":
            bloque_compteur2 += 1
        else:
            bloque_compteur2 = 0

        p2_last_action = coup_p2

        # print(player1.guesser)
        mes_vies = player1.vies
        ses_vies = 3 - player1.ENNEMY_LIFE_LOST

        # print(player1.guesser)
        

        # if Sleepers.STATUS != "ANALYSE":
        #     print(player1.guesser)

        currenttime = time.time()
        if currenttime-starttime > 20:
            if  bloque_compteur1 > bloque_compteur2:
                print(f"Pénalité {bloque_compteur1}:{bloque_compteur2}, {player2} gagne!")
                sortie = True
            elif bloque_compteur2 > bloque_compteur1:
                print(f"Pénalité {bloque_compteur2}:{bloque_compteur1}, {player1} gagne!")
                sortie = True
            else:
                print(f"Pénalité {bloque_compteur1}:{bloque_compteur1} et Égalité! Le gagnant aléatoire est Fuck this!")
                sortie = True

        if mes_vies <= 0 or ses_vies <= 0:
            if mes_vies == 0:
                # print("J'ai perdu")
                lost_counter += 1
            if ses_vies == 0:
                # print("J'ai gagne")
                win_counter += 1
            # if player2.etat()[0] == 0:
                # move_name = ""
                # move_name_p2 = ""
                # for action in this_game_moves:
                #     move_name += action[0]

                # for action in this_game_moves_p2:
                #     move_name_p2 += action[0]
                # moves = (move_name, move_name_p2)
                # if moves in winning_moves:
                #     winning_moves[moves] += 1
                # else:
                #     winning_moves[moves] = 1
            sortir = True
            # with open("winnings", "w", encoding="utf-8") as file:
            #     for moves, occurence in winning_moves.items():
            #         file.write(f"{moves} - {occurence}\n")
            # Moves.set_prob()
            # print(Moves.TOUT_MOVES)`
        # print(player1.guesser)
    #     # print(player2.guesser)
    # print(3 - Sleepers.ENNEMY_LIFE_LOST)
    print(f"Gagner: {win_counter} - Perdu: {lost_counter}")
    print(player1.guesser)

if __name__ == "__main__":
    game()