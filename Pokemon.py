import random

class pokemon :
    def __init__(self, name, attack1, attack2, attack3, attack4, hp):
        self.name = name
        self.attack1 = attack1
        self.attack2 = attack2
        self.attack3 = attack3
        self.attack4 = attack4
        self.hp = hp













pikachu = pokemon("Pikachu","Trueno", "Rayo", "Placaje", "Doble bofetón", 150)

mewtwo = pokemon("Mewtwo", "Confusión", "Paranormal", "Psico-corte","Psiquico", 200)



valor_de_ataques = {
    "Rayo":50,
    "Trueno":120,
    "Placaje":30,
    "Doble bofeton":40,
    "Confusión":40,
    "Paranormal":60,
    "Psico-corte":70,
    "Psiquico":90
    }


print (valor_de_ataques.get("Rayo"))






def payers_choice ():
    choose = "\n1) " + pikachu.name + "              2) " + mewtwo.name
    pokemon_selection = input ("Choose your pokemon" + choose)
    if pokemon_selection == 1:
        return pikachu
    elif pokemon_selection == 2:
        return mewtwo