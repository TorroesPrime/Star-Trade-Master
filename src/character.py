import filemedia as fm
import random
#import class_item
from filemedia import inv_header
from tools import spacer
import xlrd
workbook = xlrd.open_workbook("G:\\Documents\\projects\\Programming Projects\\Python Projects\\Rogue Trader Game\\python src\\names.xlsx")
male_names_sheet = "human male names"
female_names_sheet = "human female names"
last_names = "human last names"
name_source =[male_names_sheet,female_names_sheet,last_names]
dw= "Death World"
nb="Noble Born World"
iw="Imperial World"
hw="Hive World"
w="Forge World"
vb="Void Born"
world_type_names = ["Death World","Noble Born World","Imperial World","Hive World","Forge World","Void Born"]

class Character():
    def __init__(self,stats):
        """defines a character object"""
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
        self.age = 25
        self.skills = []
        self.traits = []
        self.wounds = stats[13]
        self.expierence = 0
        self.primary_weapon = None
        self.inventory = []
        self.max_weight = int(self.char_stats.get("strength"))*3

    def add_item(self, item):
        """adds supplied item to character inventory."""
        total_weight = 0
        for item in self.inventory:
            total_weight = total_weight + item.weight
        if (item.weight + total_weight) >= self.max_weight:
            print("You are not strong enough to carry all of that.")
        else:
            self.inventory.append(item)

    def list_inventory(self):
        """displays character inventory"""
        print(inv_header)
        for item in self.inventory:
            print(spacer(item.name,25)+"|"+spacer(str(item.weight),12)+"|\n")

    def arm(self, weapon):
        """sets supplied weapon as characters weapon."""
        self.primary_weapon=weapon
    
    def addxp(self,value):
        """adds xp to the character's earned_xp field."""
        self.expierence = self.expierence + value

    def character_sheet(self):
        """displays character sheet including stats, traits, talents and identification information."""
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
        return None

    def print_char(self,char):
        """modifies supplied characteristics to fill up 2 spaces. Used in character__sheet()"""
        if len(str(char)) == 2:
            char = str(char)
        else:
            char = " "+str(char)
        return char
    
    def add_skill(self,skill):
        """adds a skill to the character's skills"""
        self.skills.append(skill)

    def attack_melee(self,target):
        """method used to execute a melee attack against a supplied target"""
        if self.primary_weapon == None:
            attack_str = self.char_stats["strength"]
        else:
            attack_str = self.primary_weapon.strength

def select_name(gender = None):
    """randomly selects a name. Can be predetermined as a male or female name"""
    first_name_source = None
    if gender == "male":
        first_name_source = name_source[0]
    elif gender == "female":
        first_name_source = name_source[1]
    else:
        choice_value = random.randint(0,1)
        first_name_source = name_source[choice_value]
    first_name_sheet = workbook.sheet_by_name(first_name_source)
    row = 0
    col = 0
    total_rows = first_name_sheet.nrows
    names = []
    while row <= total_rows-1:
       names.append(first_name_sheet.cell_value(row,col).strip())
       row = row +1
    return random.choice(names)

def generate_characteristics(bonus=None, char_class = None):  
    """randomly generates values for character stats"""
    stats = []
    for stat in range(10):
        stats.append(random.randint(2,20)+25) 
    return stats
    
def generate_gender():
    """randomly selects a gender for a character"""
    gender = ["male","female"]
    return random.choice(gender)

def select_homeworld(world_type = None):    
    """randomly selects a homeworld name. Can select a particular type of home world"""
    home_world_names_source = workbook.sheet_by_name(random.choice(world_type_names))
    home_worlds = []
    row = 0
    col = 0
    total_rows = home_world_names_source.nrows
    names = []
    while row <= total_rows-1:
        names.append(home_world_names_source.cell_value(row,col))
        row = row +1
    return random.choice(names)

def generate_wounds(bonus=None):
    """Generates a random integer between 10 and 25"""
    return random.randint(10,25)

def generate_random_char():
    """generates one random character"""
    gender = generate_gender()
    name = select_name(gender)
    stats = generate_characteristics()
    home_world = select_homeworld()
    motive = "Generic motivation"
    wounds = generate_wounds()
    #generate wounds
    character_stats = [name]
    for stat in stats:
        character_stats.append(stat)
    character_stats.append(home_world)
    character_stats.append(motive)
    character_stats.append(gender)
    character_stats.append(wounds)
    created_character = Character(character_stats)
    return created_character
 

#character_gen_f()