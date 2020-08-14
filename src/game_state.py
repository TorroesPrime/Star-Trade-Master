__instance = True 
save_file_version="RT001"
current_room_leader = "Current room: "    
default_save_file = "zorkSave"
save_file_ext= ".sav"
current_room_leader = "Current room: " 
adventurers_current_room = None
test_value = False
def store(saveName,dungeon):
    fileName = saveName+save_file_ext
    saveFile = open(fileName,"a")
    saveFile.write(save_file_version)
    dungeon.StoreState(saveFile)
    saveFile.write(current_room_leader+adventurers_current_room.getName())
    saveFile.close()
def initialize(dungeon):
    dungeon = dungeon
    adventurers_current_room = dungeon.entry
    
def get_adventurers_current_room():
    current_room = adventurers_current_room
    return current_room
    
def set_adventurers_current_room(room):
    adventurers_curret_room = room
