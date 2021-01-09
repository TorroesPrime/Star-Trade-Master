import os
import xlrd
import json
import random
from game_state_instance import game_state_instance as gsi
from class_item import item
screen_width = 90
save_file_version="RT001"
inv_header = "  Item Description        Item Weight "
supported_file_versions= ["RT001"]
current_room_leader = "Current room: "    
default_save_file = "zorkSave"
save_file_ext= ".sav"
current_room_leader = "Current room: " 
top_level_delimiter = "==="
second_level_delim = "---"
rooms_marker = "Rooms:"
exits_marker = "Exits:"
file_name_leader = "Dungeon file: "
room_states_marker = "Room states:"
char_name = "Character Name:"
total_xp = "Total Expierence Earned: "
core_chars = "                              core Characteristics                              "
char_table_bar = "+-----"
char_table_top = " "*17+"|  WS |  BS | Str | Tgh |  Ag | Int | Per |  WP | Chr |"

item_apple_stats = ["Apple", "A red Fuji Apple", .2]
item_apple_Actions = {"eat": "consume-You eat the apple", "examine": "It's a red apple. It looks really tasty.", "throw": "destroy-You hurl the apple agaisnt the wall. It smashes agaisnt it with a splat."}
item_apple = item(item_apple_stats,item_apple_Actions)
item_rusty_spoon_stats = ["Spoon", "a rusty metal spoon", .1]
item_rusty_spoon_Actions ={"examine":"It's a rusty metal spoon. Looks like it may have been made out of iron.", "throw": "discard-You hurl the spoon agaisnt the wall. It clatters to the floor."}
item_rusty_spoon = item(item_rusty_spoon_stats,item_rusty_spoon_Actions)
item_birthday_cake_stats = ["Cake", "A birthday Cake", 2.5]
item_birthday_cake_Actions = {"examine": "It's a brightly decorrated birthday cake. Why is there a birthday cake in here?", "throw": "destroy-You hurl the cake against the wall. It splatters against it and remains slide down in a gooey heep. What a waste."}
item_birthday_cake = item(item_birthday_cake_stats,item_birthday_cake_Actions)
item_examples = []
item_examples.append(item_apple)
item_examples.append(item_birthday_cake)
item_examples.append(item_rusty_spoon)

class dice():
    def __init__(self,sides):
        self.sides = sides
    
    def roll(self):
        #result = random.randint(1,self.sides)
        return random.randint(1,self.sides)

def memory_block_check():
    data_directory = "data\\library\\names\\"
    files = ["data\\library\\names\\humanMale.json","data\\library\\names\\humanFemale.json","data\\library\\names\\humanLastNames.json"]
    for entry in files:
        if os.path.isfile(entry) == False:
            if gsi.test_value:
                print("False")
        else:
            if gsi.test_value:
                print("True")
            #os.makedirs(entry)


def list_builder(fileName,sheetName,listName):
    workbook = xlrd.open_workbook(fileName)
    worksheet = workbook.sheet_by_name(sheetName)
    total_rows = worksheet.nrows
    current_row = 1
    listName = []
    while current_row < total_rows:
        data = worksheet.cell(current_row,0).value.replace("\n","")
        listName.append(data)
        current_row += 1
    return listName
def library_file_maker(dest_file,source):
    with open(dest_file,"w") as write_file:
        json.dump(source,write_file)

def library_list_maker(source):
    encoded_file = open(source,'r')
    decoded_file = json.load(encoded_file)
    return decoded_file
    


if gsi.test_value:
    print(f"current Working directory:{os.getcwd()}")
memory_block_check()
male_names = list_builder("names.xlsx","human male names","male_names")
female_names = list_builder("names.xlsx","human female names","female_names")
human_last_names = list_builder("names.xlsx","human last names","human_last_names")
char_names = [male_names,female_names,human_last_names]
#library_file_maker("data\\library\\names\\humanMale.json",male_names)
#library_file_maker("data\\library\\names\\humanFemale.json",female_names)
#library_file_maker("data\\library\\names\\humanLastNames.json",human_last_names)
#print(library_list_maker("data/library/names/humanMale.json"))