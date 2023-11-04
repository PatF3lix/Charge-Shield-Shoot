# Python3 code to demonstrate working of
# N largest values in dictionary
# Using sorted() + itemgetter() + items()
"""
    Source: https://www.geeksforgeeks.org/python-n-largest-values-in-dictionary/
    Utilisation:  quand je check les cas les plus probable j'utilise ca pour trier les possibles.
    User: manjeet_04
"""
from operator import itemgetter

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

class Sleepers:
    TYPE_ACTION = ["Tir", "Recharge", "Bloque", "Faute"]
    
    def __init__(self) -> None:
        self.vies = 3
        self.munition_chargee = 1
        self.OUR_LAST_ACTION = ""
        self.STATUS = "ANALYSE"
        self.ANALYSE_GOAL = 30
        self.ANALYSE = 0

        self.ENNEMY_LAST_ACTION = ""
        self.CONSECUTIVE_BLOCK = 0
        self.ALL_ACTIONS = []

        self.ENNEMY_BULLETS = 1
        self.ENNEMY_LIFE_LOST = 0
        self.ENNEMY_BULLETS_FIRED = 0
        self.ENNEMY_RECHARGED = 0
        self.guesser = Guesser()

    def etat(self) -> tuple:
        return self.vies, self.munition_chargee

    def foul_play(self) -> bool:
        if self.ENNEMY_BULLETS > 3:
            return True
        if self.ENNEMY_BULLETS_FIRED > self.ENNEMY_RECHARGED + 1:
            return True
        if self.ENNEMY_LIFE_LOST == 3:
            return True
        if self.ENNEMY_LAST_ACTION == "Erreur":
            return True
        
    def next_action(self, last_action: str) -> str:
        ennemy_bullets = self.ENNEMY_BULLETS
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
                # if next_act == "Tir":
                #     next_act == "Bloque"
        else:
            next_act = "Bloque"
        return next_act
    
    def mode_atk(self) -> str:
        next_act = self.next_action(self.ENNEMY_LAST_ACTION)
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
        if self.STATUS == "ANALYSE":
            if self.ANALYSE >= self.ANALYSE_GOAL:
                self.STATUS = "ATK"
                return self.mode_atk()
            else:
                return "Bloque"
        elif self.STATUS == "ATK":
            return self.mode_atk()
    
    def block_block(self):
        is_block_strat = False
        if self.CONSECUTIVE_BLOCK > 100:
            self.CONSECUTIVE_BLOCK = 0
            is_block_strat = True
        return is_block_strat

    def action(self) -> str:
        if self.foul_play():
            action = "Faute"
            return action
        elif self.block_block():
            if self.munition_chargee > 0 and self.ENNEMY_BULLETS == 0:
                action = "Tir"
                self.munition_chargee -= 1
            else:
                if self.munition_chargee > 0:
                    action = "Tir"
                    self.munition_chargee -= 1
                else:
                    action = "Recharge"
        else:
            if self.munition_chargee > 0 and self.ENNEMY_BULLETS == 0:
                action = "Tir"
                self.munition_chargee -= 1
            elif self.munition_chargee <= 0 and self.ENNEMY_BULLETS == 0:
                action = "Recharge"
                self.munition_chargee += 1
            else:
                action = self.decide_action()

        self.OUR_LAST_ACTION = action
        return action

    def adversaire(self, action: str) -> None:
        if self.ENNEMY_LAST_ACTION != "":
            ennemy_bullets = self.ENNEMY_BULLETS
            dict = self.guesser.nostra_dict[ennemy_bullets]
            this_move = Move((self.ENNEMY_LAST_ACTION, action))
            dict.add_move(this_move)
            self.ANALYSE += 1
        if action in Sleepers.TYPE_ACTION:
            if self.OUR_LAST_ACTION == "Tir" and action != "Bloque":
                self.ENNEMY_LIFE_LOST += 1
            if self.OUR_LAST_ACTION != "Bloque" and action == "Tir":
                if self.ENNEMY_BULLETS > 0:
                    self.vies -= 1
                elif self.ENNEMY_BULLETS <= 0:
                    self.ENNEMY_LAST_ACTION = "Erreur"
            if action == "Tir" and self.ENNEMY_BULLETS > 0:
                self.ENNEMY_BULLETS -= 1
                self.ENNEMY_BULLETS_FIRED += 1
            
            if action == "Bloque" and self.ENNEMY_LAST_ACTION == "Bloque":
                all_block = True
                last_hundo = self.ALL_ACTIONS
                for act in last_hundo:
                    if act != "Bloque":
                        all_block = False
                if all_block:
                    self.CONSECUTIVE_BLOCK += 1
            if action == "Recharge" and self.ENNEMY_BULLETS < 3:
                self.ENNEMY_RECHARGED += 1
                self.ENNEMY_BULLETS += 1
            if len(self.ALL_ACTIONS) >= 100:
                self.ALL_ACTIONS.pop(0)
                self.ALL_ACTIONS.append(action)
            else:
                self.ALL_ACTIONS.append(action)
            self.ENNEMY_LAST_ACTION = action
        else:
            self.ENNEMY_LAST_ACTION = "Erreur"

    def reset(self):
        pass

    def __str__(self) -> str:
        return f"Sleepers - it's all under the hood."