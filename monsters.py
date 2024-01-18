from monster_structure import Monster

Dragon = Monster("Dragon", "GOD", "Fire", 1500,2000)
Slime = Monster("Slime", "Wild Monster", "Water", 20, 30)
Zombie = Monster("Zombie", "Human", "NONE", 40,60)


def boss (self):
    if self.MANA>= 1000:
        return "Boss"
    else:
        return "Regular Monster"
    
print (boss (Slime))