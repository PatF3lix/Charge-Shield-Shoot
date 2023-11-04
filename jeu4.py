from random import randint
# Python3 code to demonstrate working of
# N largest values in dictionary
# Using sorted() + itemgetter() + items()
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

    def add_move(self, move: Move):
        if move in self.almanach.values():
            self.almanach[move.move_tuple].occurence += 1
            self.nb_moves += 1
            self.set_prob()
        else:
            self.almanach[move.move_tuple] = move
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
    OUR_LAST_ACTION = ""
    STATUS = "ANALYSE"
    ANALYSE_GOAL = 1000
    ANALYSE = 0

    ENNEMY_LAST_ACTION = ""

    ENNEMY_BULLETS = 1
    ENNEMY_LIFE_LOST = 0
    ENNEMY_BULLETS_FIRED = 0
    ENNEMY_RECHARGED = 0
    
    def __init__(self) -> None:
        self.vies = 3
        self.munition_chargee = 1
        self.guesser = Guesser()

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
        
    def next_action(self, last_action: str) -> dict:
        ennemy_bullets = Sleepers.ENNEMY_BULLETS
        almanach_etat_actuel = self.guesser.nostra_dict[ennemy_bullets]
        moves = almanach_etat_actuel.almanach
        more_probable = dict(sorted(moves.items(), key = itemgetter(1), reverse = True))
        choices = []
        for name in more_probable:
            if name[0] == last_action:
                choices.append(name)
        if len(choices) > 0:
            next_action = choices[0][1]
        else:
            next_action = "Bloque"
        return next_action
    
    def mode_atk(self) -> str:
        next_action = self.next_action(Sleepers.ENNEMY_LAST_ACTION)
        if next_action == "Recharge" and self.munition_chargee > 0:
            self.munition_chargee -= 1
            return "Tir"
        elif next_action == "Tir":
            return "Bloque"
        elif next_action == "Bloque" and self.munition_chargee < 3:
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
        

    def action(self) -> str:
        if self.foul_play():
            action = "Faute"
            return action
        else:
            if self.munition_chargee > 0 and Sleepers.ENNEMY_BULLETS == 0:
                action = "Tir"
                self.munition_chargee -= 1
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
            if action == "Recharge" and Sleepers.ENNEMY_BULLETS < 3:
                Sleepers.ENNEMY_RECHARGED += 1
                Sleepers.ENNEMY_BULLETS += 1
            Sleepers.ENNEMY_LAST_ACTION = action
        else:
            Sleepers.ENNEMY_LAST_ACTION = "Erreur"

    @staticmethod
    def reset():
        Sleepers.OUR_LAST_ACTION = ""
        Sleepers.STATUS = "ANALYSE"

        Sleepers.ENNEMY_LAST_ACTION = ""

        Sleepers.ENNEMY_BULLETS = 1
        Sleepers.ENNEMY_LIFE_LOST = 0
        Sleepers.ENNEMY_BULLETS_FIRED = 0
        Sleepers.ENNEMY_RECHARGED = 0


if __name__ == "__main__":
    pass