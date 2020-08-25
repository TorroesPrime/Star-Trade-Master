import filemedia as fm
import random
class Character():
    def __init__(self,stats):
        self.name = stats[0]
        self.char_stats = {
            "weapon skill" : stats[1],
            "ballistic skill":stats[2],
            "strength":stats[3],
            "toughness":stats[4],
            "agility":stats[5],
            "intelligence":stats[6],
            "perception":stats[7],
            "will power":stats[8],
            "fellowship":stats[9],
            }
        self.home_world = stats[10]
        self.motivation = stats[11]
        self.gender = stats[12]
        self.age = stats[13]
        self.skills = []
        self.traits = []
        self.expierence = 0
        
    
    def addxp(self,value):
        self.expierence = self.expierence + value

    def character_sheet(self):
        print(f"                              {fm.char_name} {self.name}                              ")
        print(f"                              {fm.total_xp} {self.expierence}                              ")
        print(f"{fm.core_chars}")
        print((" "*17)+(fm.char_table_bar*9)+"+")
        print(fm.char_table_top)
        print((" "*17)+(fm.char_table_bar*9)+"+")
        ws =self.print_char(self.char_stats["weapon skill"])
        bs = self.print_char(self.char_stats["ballistic skill"])
        s = self.print_char(self.char_stats["strength"])
        t = self.print_char(self.char_stats["toughness"])
        ag = self.print_char(self.char_stats["agility"])
        Int = self.print_char(self.char_stats["intelligence"])
        per = self.print_char(self.char_stats["perception"])
        fell = self.print_char(self.char_stats["fellowship"])
        will = self.print_char(self.char_stats["will power"])
        print(" "*17+"|  "+ws+" |  "+bs+" |  "+s+" |  "+t+" |  "+ag+" |  "+Int+" |  "+per+" |  "+will+" |  "+fell+" |")
        print((" "*17)+(fm.char_table_bar*9)+"+")

    def print_char(self,char):
        if len(str(char)) == 2:
            char = str(char)
        else:
            char = " "+str(char)
        return char
    
    def add_skill(self,skill):
        self.skills.append(skill)

def characteristic_gen():
    dice_1 = random.randint(1,9)
    dice_2 = random.randint(1,9)
    class_bonus = 25
    value = dice_1+dice_2+class_bonus
    return value
