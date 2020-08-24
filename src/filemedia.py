import xlrd
import json
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

male_names = list_builder("names.xlsx","human male names","male_names")
female_names = list_builder("names.xlsx","human female names","female_names")
human_last_names = list_builder("names.xlsx","human last names","human_last_names")
char_names = [male_names,female_names,human_last_names]
library_file_maker("library.json",char_names)