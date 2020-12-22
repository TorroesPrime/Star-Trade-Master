#import character
class GameState():
    def __init__(self):
        self.save_file_version="RT001"
        self.current_room_leader = "Current room: "    
        self.default_save_file = "zorkSave"
        self.save_file_ext= ".sav"
        self.current_room_leader = "Current room: " 
        self.adventurers_current_room = None
        self.test_value = False
        self.player_character = None
        self.characters = []
        self.actions = []
    def store(self,saveName):
        #fileName = saveName+self.save_file_ext
        saveFile = open(saveName,"w")
        saveFile.write(self.save_file_version+"\n")
        self.dungeon.store_state(saveFile)
        current_room_record = self.current_room_leader+self.adventurers_current_room.name
        saveFile.write(current_room_record+"\n")
        saveFile.close()
    def initialize(self,dungeon):
        self.dungeon = dungeon
        self.adventurers_current_room = dungeon.entry
    
    def get_adventurers_current_room(self):
        current_room = self.adventurers_current_room
        return current_room
    
    def set_adventurers_current_room(self,room):
        self.adventurers_curret_room = room
    
    def set_player_character(self,character):
        self.player_character = character
    
    def add_character(self,character):
        self.characters.append(character)

    def set_test(self):
        if self.test_value:
            self.test_value = False
        else:
            self.test_value = True
