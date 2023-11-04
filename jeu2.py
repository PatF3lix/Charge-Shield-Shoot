class Sleepers:

    TYPE_ACTION = ["Tir", "Recharge", "Bloque", "Faute"]
    # OUR_LAST_ACTION = ""
    # STATUS = "BEGIN"
    # ANALYSE_GOAL = 10
    # ANALYSE = 0

    # ENNEMY_LAST_ACTION = ""

    # ENNEMY_BULLETS = 1
    # ENNEMY_LIFE_LOST = 0
    # ENNEMY_BULLETS_FIRED = 0
    # ENNEMY_RECHARGED = 0

    def __init__(self) -> None:
        self.vies = 3
        self.munition_chargé = 1
        self.vies_adversaire = 3
        self.munition_adversaire = 1
        self.turns = 1

    def action(self) -> str:

        """
        Message de la part de ton enseignant:
        Perds l'habitude de mettre une tonne de retour dans ton code.
        Tu devrais plutot avoir une variable que tu mets a jour en fonction
        de tes conditions(ifs) et tu la retournes uniquement a la fin.
        Ca va faciliter le debogage et la lecture de ton code !

        Keven        
        
        """
        self.turns += 1
        #  vies adversaire   3               munition adversaire 0
        if self.vies_adversaire == 3 and self.munition_adversaire == 0:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 2:
                if self.turns <= 9:
                    self.munition_chargé += 1
                    return "Recharge"
                elif self.turns >= 15:
                    self.munition_chargé -= 1
                    return "Tir"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                if self.turns % 15 == 0:
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"             
            elif self.vies == 2 and self.munition_chargé == 1:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
        #  vies adversaire 3                 munition adversaire  1
        elif self.vies_adversaire == 3 and self.munition_adversaire == 1:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns <= 3:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns <= 10 or self.turns % 15 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns <= 10 or self.turns % 15 == 0 or self.turns % 9:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns <= 8 or self.turns % 15 == 0 or self.turns % 13:
                    return "Bloque"
                elif self.turns <= 12:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 3 == 0 or self.turns <=3:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    self.munition_chargé -= 1
                    return "Tir"
                elif self.turns % 10 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
        #  vies adversaire 3                 munition adversaire  2
        elif self.vies_adversaire == 3 and self.munition_adversaire == 2:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 1:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns <= 3 or self.turns % 3 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                if self.turns <= 3 or self.turns % 3 == 0:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns <= 10:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns <= 10:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns <= 10:
                    return "Bloque"
                elif self.turns <= 15:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 3 == 0 or self.turns <=3:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    if self.munition_chargé > 0:
                        self.munition_chargé -= 1
                        return "Tir"
                elif self.turns % 10 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
        #  vies adversaire 3                 munition adversaire  3
        elif self.vies_adversaire == 3 and self.munition_adversaire == 3:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                if self. turns % 3 == 0 or self.turns <= 3:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns >= 10 or self.turns % 3 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    return "Bloque"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns >= 10 or self.turns % 3 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    return "Bloque"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns % 5 == 0 or self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 5 == 0 or self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"

        elif self.vies_adversaire == 2 and self.munition_adversaire == 0:
            if self.vies == 3 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 2:
                if self.turns <= 9:
                    self.munition_chargé += 1
                    return "Recharge"
                elif self.turns >= 15:
                    self.munition_chargé -= 1
                    return "Tir"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                if self.turns % 15 == 0:
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"             
            elif self.vies == 2 and self.munition_chargé == 1:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
        #  vies adversaire 3                 munition adversaire  1
        elif self.vies_adversaire == 3 and self.munition_adversaire == 1:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns <= 3:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns <= 10 or self.turns % 15 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns <= 10 or self.turns % 15 == 0 or self.turns % 9:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns <= 8 or self.turns % 15 == 0 or self.turns % 13:
                    return "Bloque"
                elif self.turns <= 12:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 3 == 0 or self.turns <=3:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    self.munition_chargé -= 1
                    return "Tir"
                elif self.turns % 10 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
        #  vies adversaire 3                 munition adversaire  2
        elif self.vies_adversaire == 3 and self.munition_adversaire == 2:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 1:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns <= 3 or self.turns % 3 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                if self.turns <= 3 or self.turns % 3 == 0:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns <= 10:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns <= 10:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns <= 10:
                    return "Bloque"
                elif self.turns <= 15:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 3 == 0 or self.turns <=3:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    if self.munition_chargé > 0:
                        self.munition_chargé -= 1
                        return "Tir"
                elif self.turns % 10 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
        #  vies adversaire 3                 munition adversaire  3
        elif self.vies_adversaire == 3 and self.munition_adversaire == 3:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                if self. turns % 3 == 0 or self.turns <= 3:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns >= 10 or self.turns % 3 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    return "Bloque"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns >= 10 or self.turns % 3 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    return "Bloque"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns % 5 == 0 or self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 5 == 0 or self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            
        elif self.vies_adversaire == 2 and self.munition_adversaire == 1:
            if self.vies == 3 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 2:
                if self.turns <= 9:
                    self.munition_chargé += 1
                    return "Recharge"
                elif self.turns >= 15:
                    self.munition_chargé -= 1
                    return "Tir"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                if self.turns % 15 == 0:
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"             
            elif self.vies == 2 and self.munition_chargé == 1:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
        #  vies adversaire 3                 munition adversaire  1
        elif self.vies_adversaire == 3 and self.munition_adversaire == 1:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns <= 3:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns <= 10 or self.turns % 15 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns <= 10 or self.turns % 15 == 0 or self.turns % 9:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns <= 8 or self.turns % 15 == 0 or self.turns % 13:
                    return "Bloque"
                elif self.turns <= 12:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 3 == 0 or self.turns <=3:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    self.munition_chargé -= 1
                    return "Tir"
                elif self.turns % 10 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
        #  vies adversaire 3                 munition adversaire  2
        elif self.vies_adversaire == 3 and self.munition_adversaire == 2:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 1:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns <= 3 or self.turns % 3 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                if self.turns <= 3 or self.turns % 3 == 0:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns <= 10:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns <= 10:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns <= 10:
                    return "Bloque"
                elif self.turns <= 15:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 3 == 0 or self.turns <=3:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    if self.munition_chargé > 0:
                        self.munition_chargé -= 1
                        return "Tir"
                elif self.turns % 10 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
        #  vies adversaire 3                 munition adversaire  3
        elif self.vies_adversaire == 3 and self.munition_adversaire == 3:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                if self. turns % 3 == 0 or self.turns <= 3:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns >= 10 or self.turns % 3 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    return "Bloque"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns >= 10 or self.turns % 3 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    return "Bloque"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns % 5 == 0 or self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 5 == 0 or self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
           

        elif self.vies_adversaire == 2 and self.munition_adversaire == 2:
            if self.vies == 3 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 2:
                if self.turns <= 9:
                    self.munition_chargé += 1
                    return "Recharge"
                elif self.turns >= 15:
                    self.munition_chargé -= 1
                    return "Tir"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                if self.turns % 15 == 0:
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"             
            elif self.vies == 2 and self.munition_chargé == 1:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
        #  vies adversaire 3                 munition adversaire  1
        elif self.vies_adversaire == 3 and self.munition_adversaire == 1:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns <= 3:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns <= 10 or self.turns % 15 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns <= 10 or self.turns % 15 == 0 or self.turns % 9:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns <= 8 or self.turns % 15 == 0 or self.turns % 13:
                    return "Bloque"
                elif self.turns <= 12:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 3 == 0 or self.turns <=3:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    self.munition_chargé -= 1
                    return "Tir"
                elif self.turns % 10 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
        #  vies adversaire 3                 munition adversaire  2
        elif self.vies_adversaire == 3 and self.munition_adversaire == 2:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 1:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns <= 3 or self.turns % 3 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                if self.turns <= 3 or self.turns % 3 == 0:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns <= 10:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns <= 10:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns <= 10:
                    return "Bloque"
                elif self.turns <= 15:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 3 == 0 or self.turns <=3:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    if self.munition_chargé > 0:
                        self.munition_chargé -= 1
                        return "Tir"
                elif self.turns % 10 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
        #  vies adversaire 3                 munition adversaire  3
        elif self.vies_adversaire == 3 and self.munition_adversaire == 3:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                if self. turns % 3 == 0 or self.turns <= 3:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns >= 10 or self.turns % 3 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    return "Bloque"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns >= 10 or self.turns % 3 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    return "Bloque"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns % 5 == 0 or self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 5 == 0 or self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
         

        elif self.vies_adversaire == 2 and self.munition_adversaire == 3:
            if self.vies == 3 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 2:
                if self.turns <= 9:
                    self.munition_chargé += 1
                    return "Recharge"
                elif self.turns >= 15:
                    self.munition_chargé -= 1
                    return "Tir"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                if self.turns % 15 == 0:
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"             
            elif self.vies == 2 and self.munition_chargé == 1:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
        #  vies adversaire 3                 munition adversaire  1
        elif self.vies_adversaire == 3 and self.munition_adversaire == 1:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns <= 3:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns <= 10 or self.turns % 15 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns <= 10 or self.turns % 15 == 0 or self.turns % 9:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns <= 8 or self.turns % 15 == 0 or self.turns % 13:
                    return "Bloque"
                elif self.turns <= 12:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 3 == 0 or self.turns <=3:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    self.munition_chargé -= 1
                    return "Tir"
                elif self.turns % 10 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
        #  vies adversaire 3                 munition adversaire  2
        elif self.vies_adversaire == 3 and self.munition_adversaire == 2:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 1:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns <= 3 or self.turns % 3 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                if self.turns <= 3 or self.turns % 3 == 0:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns <= 10:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns <= 10:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns <= 10:
                    return "Bloque"
                elif self.turns <= 15:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 3 == 0 or self.turns <=3:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    if self.munition_chargé > 0:
                        self.munition_chargé -= 1
                        return "Tir"
                elif self.turns % 10 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
        #  vies adversaire 3                 munition adversaire  3
        elif self.vies_adversaire == 3 and self.munition_adversaire == 3:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                if self. turns % 3 == 0 or self.turns <= 3:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns >= 10 or self.turns % 3 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    return "Bloque"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns >= 10 or self.turns % 3 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    return "Bloque"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns % 5 == 0 or self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 5 == 0 or self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
           

        elif self.vies_adversaire == 1 and self.munition_adversaire == 0:
            if self.vies == 3 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 2:
                if self.turns <= 9:
                    self.munition_chargé += 1
                    return "Recharge"
                elif self.turns >= 15:
                    self.munition_chargé -= 1
                    return "Tir"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                if self.turns % 15 == 0:
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"             
            elif self.vies == 2 and self.munition_chargé == 1:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
        #  vies adversaire 3                 munition adversaire  1
        elif self.vies_adversaire == 3 and self.munition_adversaire == 1:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns <= 3:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns <= 10 or self.turns % 15 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns <= 10 or self.turns % 15 == 0 or self.turns % 9:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns <= 8 or self.turns % 15 == 0 or self.turns % 13:
                    return "Bloque"
                elif self.turns <= 12:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 3 == 0 or self.turns <=3:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    self.munition_chargé -= 1
                    return "Tir"
                elif self.turns % 10 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
        #  vies adversaire 3                 munition adversaire  2
        elif self.vies_adversaire == 3 and self.munition_adversaire == 2:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 1:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns <= 3 or self.turns % 3 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                if self.turns <= 3 or self.turns % 3 == 0:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns <= 10:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns <= 10:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns <= 10:
                    return "Bloque"
                elif self.turns <= 15:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 3 == 0 or self.turns <=3:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    if self.munition_chargé > 0:
                        self.munition_chargé -= 1
                        return "Tir"
                elif self.turns % 10 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
        #  vies adversaire 3                 munition adversaire  3
        elif self.vies_adversaire == 3 and self.munition_adversaire == 3:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                if self. turns % 3 == 0 or self.turns <= 3:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns >= 10 or self.turns % 3 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    return "Bloque"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns >= 10 or self.turns % 3 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    return "Bloque"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns % 5 == 0 or self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 5 == 0 or self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
           

        elif self.vies_adversaire == 1 and self.munition_adversaire == 1:
            if self.vies == 3 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 2:
                if self.turns <= 9:
                    self.munition_chargé += 1
                    return "Recharge"
                elif self.turns >= 15:
                    self.munition_chargé -= 1
                    return "Tir"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                if self.turns % 15 == 0:
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"             
            elif self.vies == 2 and self.munition_chargé == 1:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
        #  vies adversaire 3                 munition adversaire  1
        elif self.vies_adversaire == 3 and self.munition_adversaire == 1:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns <= 3:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns <= 10 or self.turns % 15 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns <= 10 or self.turns % 15 == 0 or self.turns % 9:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns <= 8 or self.turns % 15 == 0 or self.turns % 13:
                    return "Bloque"
                elif self.turns <= 12:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 3 == 0 or self.turns <=3:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    self.munition_chargé -= 1
                    return "Tir"
                elif self.turns % 10 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
        #  vies adversaire 3                 munition adversaire  2
        elif self.vies_adversaire == 3 and self.munition_adversaire == 2:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 1:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns <= 3 or self.turns % 3 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                if self.turns <= 3 or self.turns % 3 == 0:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns <= 10:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns <= 10:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns <= 10:
                    return "Bloque"
                elif self.turns <= 15:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 3 == 0 or self.turns <=3:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    if self.munition_chargé > 0:
                        self.munition_chargé -= 1
                        return "Tir"
                elif self.turns % 10 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
        #  vies adversaire 3                 munition adversaire  3
        elif self.vies_adversaire == 3 and self.munition_adversaire == 3:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                if self. turns % 3 == 0 or self.turns <= 3:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns >= 10 or self.turns % 3 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    return "Bloque"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns >= 10 or self.turns % 3 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    return "Bloque"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns % 5 == 0 or self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 5 == 0 or self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
           
     
        elif self.vies_adversaire == 1 and self.munition_adversaire == 2:
            if self.vies == 3 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 2:
                if self.turns <= 9:
                    self.munition_chargé += 1
                    return "Recharge"
                elif self.turns >= 15:
                    self.munition_chargé -= 1
                    return "Tir"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                if self.turns % 15 == 0:
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"             
            elif self.vies == 2 and self.munition_chargé == 1:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
        #  vies adversaire 3                 munition adversaire  1
        elif self.vies_adversaire == 3 and self.munition_adversaire == 1:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns <= 3:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns <= 10 or self.turns % 15 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns <= 10 or self.turns % 15 == 0 or self.turns % 9:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns <= 8 or self.turns % 15 == 0 or self.turns % 13:
                    return "Bloque"
                elif self.turns <= 12:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 3 == 0 or self.turns <=3:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    self.munition_chargé -= 1
                    return "Tir"
                elif self.turns % 10 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
        #  vies adversaire 3                 munition adversaire  2
        elif self.vies_adversaire == 3 and self.munition_adversaire == 2:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 1:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns <= 3 or self.turns % 3 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                if self.turns <= 3 or self.turns % 3 == 0:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns <= 10:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns <= 10:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns <= 10:
                    return "Bloque"
                elif self.turns <= 15:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 3 == 0 or self.turns <=3:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    if self.munition_chargé > 0:
                        self.munition_chargé -= 1
                        return "Tir"
                elif self.turns % 10 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
        #  vies adversaire 3                 munition adversaire  3
        elif self.vies_adversaire == 3 and self.munition_adversaire == 3:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                if self. turns % 3 == 0 or self.turns <= 3:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns >= 10 or self.turns % 3 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    return "Bloque"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns >= 10 or self.turns % 3 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    return "Bloque"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns % 5 == 0 or self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 5 == 0 or self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            

        elif self.vies_adversaire == 1 and self.munition_adversaire == 3:
            if self.vies == 3 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 2:
                if self.turns <= 9:
                    self.munition_chargé += 1
                    return "Recharge"
                elif self.turns >= 15:
                    self.munition_chargé -= 1
                    return "Tir"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                if self.turns % 15 == 0:
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"             
            elif self.vies == 2 and self.munition_chargé == 1:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
        #  vies adversaire 3                 munition adversaire  1
        elif self.vies_adversaire == 3 and self.munition_adversaire == 1:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns <= 3:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns <= 10 or self.turns % 15 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns <= 10 or self.turns % 15 == 0 or self.turns % 9:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns <= 8 or self.turns % 15 == 0 or self.turns % 13:
                    return "Bloque"
                elif self.turns <= 12:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 3 == 0 or self.turns <=3:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    self.munition_chargé -= 1
                    return "Tir"
                elif self.turns % 10 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
        #  vies adversaire 3                 munition adversaire  2
        elif self.vies_adversaire == 3 and self.munition_adversaire == 2:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                if self.turns <= 5 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 1:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                self.munition_chargé += 1
                return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns <= 3 or self.turns % 3 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                if self.turns <= 3 or self.turns % 3 == 0:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns <= 10:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns <= 10:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns <= 10:
                    return "Bloque"
                elif self.turns <= 15:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 3 == 0 or self.turns <=3:
                    return "Bloque"
                elif self.turns % 5 == 0:
                    if self.munition_chargé > 0:
                        self.munition_chargé -= 1
                        return "Tir"
                elif self.turns % 10 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
        #  vies adversaire 3                 munition adversaire  3
        elif self.vies_adversaire == 3 and self.munition_adversaire == 3:
            # vies joueur                   munition joueur
            if self.vies == 3 and self.munition_chargé == 0:
                if self. turns % 3 == 0 or self.turns <= 3:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 3 and self.munition_chargé == 1:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 2:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 3 and self.munition_chargé == 3:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 2 and self.munition_chargé == 0:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 1:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 2:
                if self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé += 1
                    return "Recharge"
            elif self.vies == 2 and self.munition_chargé == 3:
                self.munition_chargé -= 1
                return "Tir"
            if self.vies == 1 and self.munition_chargé == 0:
                if self.turns >= 10 or self.turns % 3 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    return "Bloque"
            elif self.vies == 1 and self.munition_chargé == 1:
                if self.turns >= 10 or self.turns % 3 == 0:
                    self.munition_chargé += 1
                    return "Recharge"
                else:
                    return "Bloque"
            elif self.vies == 1 and self.munition_chargé == 2:
                if self.turns % 5 == 0 or self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
            elif self.vies == 1 and self.munition_chargé == 3:
                if self.turns % 5 == 0 or self.turns % 2 == 0:
                    return "Bloque"
                else:
                    self.munition_chargé -= 1
                    return "Tir"
                    
          
    def adversaire(self, action: str) -> None:
        # if action in Sleepers.TYPE_ACTION:
        #     if Sleepers.OUR_LAST_ACTION == "Tir" and action != "Bloque":
        #         Sleepers.ENNEMY_LIFE_LOST += 1
        #     if Sleepers.OUR_LAST_ACTION != "Bloque" and action == "Tir":
        #         if Sleepers.ENNEMY_BULLETS > 0:
        #             self.vies -= 1
        #         elif Sleepers.ENNEMY_BULLETS <= 0:
        #             Sleepers.ENNEMY_LAST_ACTION = "Erreur"
        #     if action == "Tir" and Sleepers.ENNEMY_BULLETS > 0:
        #         Sleepers.ENNEMY_BULLETS -= 1
        #         Sleepers.ENNEMY_BULLETS_FIRED += 1
        #     if action == "Recharge" and Sleepers.ENNEMY_BULLETS < 3:
        #         Sleepers.ENNEMY_RECHARGED += 1
        #         Sleepers.ENNEMY_BULLETS += 1
        #     Sleepers.ENNEMY_LAST_ACTION = action
        # else:
        #     Sleepers.ENNEMY_LAST_ACTION = "Erreur"
        pass

    # @staticmethod
    # def reset():
    #     Sleepers.OUR_LAST_ACTION = ""
    #     Sleepers.STATUS = "BEGIN"

    #     Sleepers.ENNEMY_LAST_ACTION = ""

    #     Sleepers.ENNEMY_BULLETS = 1
    #     Sleepers.ENNEMY_LIFE_LOST = 0
    #     Sleepers.ENNEMY_BULLETS_FIRED = 0
    #     Sleepers.ENNEMY_RECHARGED = 0

    def etat(self):
        
        return self.vies, self.munition_chargé

    def faute(self):
        pass



