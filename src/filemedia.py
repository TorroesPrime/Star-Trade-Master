import os
import xlrd
import json
import random
from game_state_instance import game_state_instance as gsi
screen_width = 90
save_file_version="RT001"
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