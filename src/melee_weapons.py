class Melee_Weapon():
    def __init__(self,stats):
        self.name = stats[0]
        self.weaponClass = stats[1]
        self.damage_mod = stats[2]
        self.penetration = stats[3]
        self.special_rule = stats[4]
        self.weight = stats[5]

        
