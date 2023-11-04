# 2194517 Xin 2295847 Yimin


from time import  localtime, mktime




class Anonyme:

    type_action = ["Tir", "Recharge", "Bloque", "Faute"]

    def __init__(self) -> None:
        self.vie = 3
        self.munition = 1
        self.mon_action = 'Bloque'
        self.mes_actions = ""
        self.etat_ad = [3, 1]
        self.actions_ad = ""
        self.bloquetime = mktime(localtime())
        self.monbloquetime = mktime(localtime())

    def __str__(self) -> str:
        return f'Anonyme'

    
    def action(self):
        #self.mon_action = 'Bloque'
        if self.etat_ad[0] < 0 or self.etat_ad[1] < 0:
            self.faute()
            #print(f"tu triche, ta vie or munition est moins que 0")
            
        elif mktime(localtime()) - self.monbloquetime >= 44:
            self.recharge()
            #print(f"Tu ne fais que blocage pendant 45s, tes dernières actions sont {self.actions_ad}")
            #print(f"Puis, je fait un 'recharege' ")
            # sleep(1)
        else:
            self.stategie()
        #print(self.mon_action, self.mes_actions)
        return self.mon_action

    def adversaire(self, action):
        if action == 'Tir':
            self.actions_ad = ""
            self.etat_ad[1] -= 1
            if self.mon_action != 'Bloque':
                self.vie -= 1
            if self.mon_action == 'Tir':
                self.etat_ad[0] -= 1
            self.bloquetime = mktime(localtime())
        elif action == 'Recharge':
            self.actions_ad = ""
            if self.etat_ad[1] < 3:
                self.etat_ad[1] += 1
            if self.mon_action == 'Tir':
                self.etat_ad[0] -= 1
            self.bloquetime = mktime(localtime())
        elif action == 'Bloque':
            self.actions_ad  += "b"
            #sleep(1)

        elif action == 'Faute':
            self.actions_ad = ""
            #print("On n'a pas triché==================================")
            #sleep(5)
            self.bloquetime = mktime(localtime())
        # else:
        #     #print('Action inconnue!!====================================')
        #     sleep(5)
        # if self.vie == 0:
        #     #print("Je coule!=========================================== ")
        #     sleep(5)
    
    def stategie(self):
        if self.etat_ad[1] == 0:    # pas dangeureur
            if self.munition == 0:
                self.recharge()     # sure
            elif self.munition == 3:
                self.tir()          # sure
            elif self.munition == 2:
                if self.etat_ad[0] == 1:
                    self.tir()       # sure
                elif self.etat_ad[0] == 3:
                    self.recharge()   # conservatif
                else:
                    if self.vie > 2 :
                        self.tir()   # agressive
                    else:
                        self.recharge()   # conservatif
            else:                          # ma munition = 1
                if self.etat_ad[0] == 1:
                    self.recharge()              # sure
                elif self.etat_ad[0] == 3:
                    self.recharge()         # conservatif
                else:                       # sa vie = 2
                     self.recharge()           
                   
        elif self.etat_ad[1] == 3: # tres dangeureur
            if self.etat_ad[0] == 1:
                if self.munition >= 2 :
                    if self.vie == 1:
                        self.bloque()
                    else:
                        self.tir()    # agressif
                elif self.munition == 1:
                    if self.vie == 1:
                        self.bloque()
                    else:
                        self.recharge()
                elif self.munition == 0:
                     self.bloque()
               
            elif self.etat_ad[0] == 2:
                if self.vie == 1:
                    self.bloque()
                elif self.vie == 3:
                    if self.munition ==3:
                        self.tir()
                    elif self.munition == 0:
                        self.bloque()
                    else:
                        self.recharge()
                else:
                    self.bloque()

            elif self.etat_ad[0] == 3:
                if self.munition == 3:
                    if self.vie <= 3:
                        self.bloque()
                    else:
                        self.tir()
                elif self.munition == 2:
                    self.bloque()
                    
                elif self.munition == 1:
                    if self.vie <= 2:
                        self.bloque()
                    else:
                        self.bloque()
                else:
                    self.bloque()
         
        elif self.etat_ad[1] == 2:
            if self.etat_ad[0] == 3:
                self.bloque()
            elif self.etat_ad[0] == 1:
                if self.vie == 1 :
                    self.bloque()
                else:
                    if self.munition == 1:
                        self.recharge()
                    elif self.munition == 0:
                        self.bloque()
                    else:
                        self.tir()
            elif self.etat_ad[0] == 2:
                if self.vie == 3:
                    if self.munition >= 2:
                        self.tir()
                    elif self.munition == 0:
                        self.bloque()
                    else:
                        self.recharge()
                elif self.vie == 2:
                    if self.munition == 3:
                        self.tir()
                    elif self.munition == 2:
                        self.bloque()
                    elif self.munition == 1:
                        self.bloque()
                    else:
                        self.bloque()
                elif self.vie == 1:
                    self.bloque()



        elif self.etat_ad[1] == 1:
            if self.etat_ad[0] == 1:
                if self.munition >= 2:
                    if self.vie >= 2:
                        self.tir()
                    else:
                        self.bloque()
                elif self.munition == 0:
                    if self.vie >= 2:
                        self.recharge()
                    else:
                        self.bloque()
                elif self.munition == 1:
                    if self.vie == 1:
                        self.bloque()
                    elif self.vie ==2:
                        self.recharge()
                    else:
                        self.recharge()           
            elif self.etat_ad[0] == 2:
                if self.vie == 3:
                    if self.munition >= 2:
                        self.tir()
                    elif self.munition == 0:
                        self.bloque()
                    else:
                        self.recharge()
                elif self.vie == 2:
                    if self.munition == 3:
                        self.tir()
                    elif self.munition == 1:
                        self.recharge()
                    elif self.munition == 0:
                        self.bloque()
                    else:
                        self.tir()
                elif self.vie == 1:
                    self.bloque()
                    
            elif self.etat_ad[0] == 3:
                if self.vie ==3:
                    if self.munition >= 2:
                        self.tir()
                    elif self.munition == 0:
                        self.bloque()
                    else:
                        self.recharge()
                elif self.vie <= 2:
                    self.bloque()


    def tir(self):
        self.mon_action = "Tir"
        self.munition -= 1
        self.mes_actions = ""
        self.monbloquetime = mktime(localtime())

    def recharge(self):
        self.mon_action = "Recharge"
        if self.munition < 3:
            self.munition += 1
        self.mes_actions = ""
        self.monbloquetime = mktime(localtime())

    def bloque(self):
        self.mon_action = "Bloque"
        self.mes_actions += "b"

    def faute(self):
        self.mon_action = "Faute"
        self.mes_actions = ""
        self.monbloquetime = mktime(localtime())

    def etat(self):
        return f'Anonyme {self.vie} vies {self.munition} balls'


# def test():

#     p = Anonyme()

#     vie = [1,2,3]
#     ball = [0,1,2,3]
#     print(f"no av  am  mv  mm  action")
#     a=1
#     for i in vie:
#         for j in ball:
#             for k in vie:
#                 for l in ball:
#                     p.etat_ad = [i, j]
#                     p.vie, p.munition = k, l

#                     ac = p.action()
#                     #if i+j == k+l:
#                     print(f"{a}  {i}  {j}  {k}  {l}  {ac}")
#                     a+=1
#                     if ac not in Anonyme.type_action:
#                         return

# test()