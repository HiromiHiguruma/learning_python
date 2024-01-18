import random

class pokemon :
    def __init__(self, name, attack1, attack2, attack3, attack4, hp):
        self.name = name
        self.attack1 = attack1
        self.attack2 = attack2
        self.attack3 = attack3
        self.attack4 = attack4
        self.hp = hp













pikachu = pokemon("Pikachu","Trueno", "Rayo", "Placaje", "Doble bofeton", 150)

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








def players_choice ():
    Pokemon_selected = 0
    while Pokemon_selected == 0:
        choose = "\n1) " + pikachu.name + "              2) " + mewtwo.name + "\n"
        pokemon_selection = input ("Choose your pokemon" + choose)
        try:
            if int(pokemon_selection) == 1:
                Pokemon_selected = 1
                if Pokemon_selected == 1:
                    Pokemon_selected = pikachu
                    return Pokemon_selected
            elif int(pokemon_selection) == 2:
                Pokemon_selected = 2
                if Pokemon_selected == 2:
                    Pokemon_selected = mewtwo
                    return Pokemon_selected
            else:
                print ("Invalid option. Please choose (1) or (2)")
                Pokemon_selected = 0
        except ValueError:
            print ("\nPlease enter a numeric value")
            Pokemon_selected = 0
            players_choice



your_pokemon = players_choice()





def cpus_choice ():
    if your_pokemon == pikachu:
        cpu_pokemon = mewtwo
        return cpu_pokemon
    else:
        cpu_pokemon = pikachu
        return cpu_pokemon
    
cpus_pokemon = cpus_choice ()


print ("\nA wild " + cpus_pokemon.name + " appeared!!")
print ("Go " + your_pokemon.name + "!!")


def battle ():
    try:

        your_current_HP = your_pokemon.hp
        cpus_current_HP = cpus_pokemon.hp
        cpus_attack_pool = [cpus_pokemon.attack1, cpus_pokemon.attack2, cpus_pokemon.attack3, cpus_pokemon.attack4]

        while your_current_HP > 0 and cpus_current_HP > 0:
            print ("\n" + your_pokemon.name + "                 HP:" + str(your_current_HP))
            print (cpus_pokemon.name + "                 HP:" + str (cpus_current_HP))
            print ("\n Choose your attack")
            print ("1 ) " + your_pokemon.attack1 + "            2 )" + your_pokemon.attack2 )
            print ("\n")
            print ("3 ) " + your_pokemon.attack3 + "            4 )" + your_pokemon.attack4 )
            your_attack_choice = int (input ())
            if your_attack_choice == 1:
                print ("You used " + your_pokemon.attack1 + ".")
                cpus_current_HP = cpus_current_HP - valor_de_ataques.get(your_pokemon.attack1)
                
                cpus_attack_choice = random.choice(cpus_attack_pool)
                print ("\nWild " + cpus_pokemon.name + "used " + cpus_attack_choice + "." )
                your_current_HP = your_current_HP - valor_de_ataques.get(cpus_attack_choice)


            elif your_attack_choice == 2:
                print ("You used " + your_pokemon.attack2 + ".")
                cpus_current_HP = cpus_current_HP - valor_de_ataques.get(your_pokemon.attack2)

                cpus_attack_choice = random.choice(cpus_attack_pool)
                print ("\nWild " + cpus_pokemon.name + "used " + cpus_attack_choice + "." )
                your_current_HP = your_current_HP - valor_de_ataques.get(cpus_attack_choice)


            elif your_attack_choice == 3:
                print ("You used " + your_pokemon.attack3 + ".")
                cpus_current_HP = cpus_current_HP - valor_de_ataques.get(your_pokemon.attack3)

                cpus_attack_choice = random.choice(cpus_attack_pool)
                print ("\nWild " + cpus_pokemon.name + "used " + cpus_attack_choice + ".")
                your_current_HP = your_current_HP - valor_de_ataques.get(cpus_attack_choice)


            elif your_attack_choice == 4:
                print ("You used " + your_pokemon.attack4 + ".")
                cpus_current_HP = cpus_current_HP - valor_de_ataques.get(your_pokemon.attack4)

                cpus_attack_choice = random.choice(cpus_attack_pool)
                print ("\nWild " + cpus_pokemon.name + "used " + cpus_attack_choice + "." )
                your_current_HP = your_current_HP - valor_de_ataques.get(cpus_attack_choice)


            else:
                print ("Invalid option")
            
    except ValueError:
        print ("\nPlease enter a numeric value. The battle will restart.")

        battle ()

    if your_current_HP <= 0 and cpus_current_HP > 0:
        print ( "\n" + your_pokemon.name + " has no more HP!!")
        print ("You lose")
    elif your_current_HP >= 0 and cpus_current_HP < 0:
        print ( "\n" + cpus_pokemon.name + " has no more HP!!")
        print ("You win!!!!")




battle ()