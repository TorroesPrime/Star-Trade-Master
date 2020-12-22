from filemedia import default_save_file,save_file_version,save_file_ext
from game_state_instance import game_state_instance as gsi
import room


class TakeCommand(): 
    def __init__(self,commandString):
        command_string_list = commandString.split()
        self.commandName = "take Command"
        self.description = "Takes the specified item and adds it to the player inventory."
        self.usage = "> take hammer"
        self.usageDetails = "if an item matching the name supplied is not found in the room, displays a message saying no such item found in current room."
        self.item = command_string_list[1]

    def execute(self):
        room_inventory = []
        for item in gsi.adventurers_current_room.iventory:
            item_name = item.name
             
        if self.item in gsi.adventurers_current_room.iventory:
            gsi.player_character.add_item(self.item)
            return self.item+" added to your inventory.\n"
    def details(self,details):
        """ Method docstring"""
        if(details != True):
            return self.description
        else:
            return " - "+self.commandName+": "+self.description+"\nUsage Example: "+self.usageDetails