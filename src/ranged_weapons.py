class Ranged_Weapon():
    def __init__(self,stats):
        self.name = stats[0]
        self.weaponClass = stats[1]
        self.range = stats[2]
        self.rate_of_fire = stats[3]
        self.damage_mod = stats[4]
        self.penetration = stats[5]
        self.clip_size = stats[6]
        self.special_rule = stats[7]
        self.weight = stats[8]

    
