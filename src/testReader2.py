import os
from filemedia import top_level_delimiter, second_level_delim, room_states_marker, rooms_marker, exits_marker
filename = "ply the stars.adv"
print(os.getcwd())
os.chdir("G:\\Documents\\projects\\Programming Projects\\Python Projects\\Rogue Trader Game\\python src\\adventures")
print(os.getcwd())
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
def dungeon_scanner(fileName):
    with open(fileName,"r") as a:
        delimiterfound = False
        adventure_info = []
        for line_num,line in enumerate(a.readlines()):
            if delimiterfound == True:
                if line[0:4] == "NPCs:":
                    delimiterfound = False
                if line[0:2] == "===":
                    delimiterfound = True

            print("line "+str(line_num+1)+": "+line)
            adventure_info.append(line)

dungeon_scanner(filename)