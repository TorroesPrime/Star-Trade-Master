import os
from filemedia import top_level_delimiter,second_level_delim,room_states_marker,rooms_marker,exits_marker
filename = "ply the stars.adv"
print(os.getcwd())
os.chdir("G:\\Documents\\projects\\Programming Projects\\Python Projects\\Rogue Trader Game\\python src\\adventures")
print(os.getcwd())

def dungeon_scanner(fileName):
    adventure_Data = []
    room_data =[]
    exit_data =[]
    dungeon_data = []
    with open(fileName,"r") as a:
        for line in a.readlines():
            adventure_Data.append(line.strip())
    dungeon_data.append(adventure_Data[0])
    dungeon_data.append(adventure_Data[1])
    dungeon_data.append(adventure_Data[2])

    for line in adventure_Data:
        print(line)
        a = line
        if line == rooms_marker:
            while line != second_level_delim:
                room_data.append(line)
                print(line)
        
            

    



dungeon_scanner(filename)