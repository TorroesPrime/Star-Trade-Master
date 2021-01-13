"""game state - records present state of the game including dungeon, player, players current room,\
 and NPCs."""
#import character
class GameState():
    """defines game state"""
    def __init__(self):
        self.save_file_version = "RT001"
        self.current_room_leader = "Current room: "
        self.default_save_file = "zorkSave"
        self.save_file_ext = ".sav"
        self.current_room_leader = "Current room: "
        self.adventurers_current_room = None
        self.test_value = True
        self.player_character = None
        self.characters = []
        self.actions = []
    def store(self, save_name):
        """method to write present gamestate to .sav file"""
        #fileName = saveName+self.save_file_ext
        save_file = open(save_name, "w")
        save_file.write(self.save_file_version+"\n")
        self.dungeon.store_state(save_file)
        current_room_record = self.current_room_leader+self.adventurers_current_room.name
        save_file.write(current_room_record+"\n")
        save_file.close()
    def initialize(self, dungeon):
        """initialize dungeon and sets adventuers current room to entry room."""
        self.dungeon = dungeon
        self.adventurers_current_room = dungeon.entry
    def get_adventurers_current_room(self):
        """returns adventurers current room"""
        current_room = self.adventurers_current_room
        return current_room
    def set_adventurers_current_room(self, room):
        """set's adventurer's current room"""
        self.adventurers_curret_room = room
    def set_player_character(self, character):
        """sets the selected character to be the player character"""
        self.player_character = character
    def add_character(self, character):
        """adds a supplied character to dungeon's characters list."""
        self.characters.append(character)
    def set_test(self):
        """set's test status"""
        if self.test_value:
            self.test_value = False
        else:
            self.test_value = True
