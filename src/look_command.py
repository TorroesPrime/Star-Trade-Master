from filemedia import default_save_file,save_file_version,save_file_ext
from game_state_instance import game_state_instance as gsi

class LookCommand(): 
    def __init__(self):
        self.default_save_file = default_save_file+save_file_ext
        self.commandName = "Look Command"
        self.description = "Allows the user to view the full description of the room they currently occupy."
        self.usage = "> look\n [full description of the room]"
        self.usageDetails = ""

    def execute(self):
        return gsi.adventurers_current_room.full_describe()
        
    def details(self,details):
        """ Method docstring"""
        if(details != True):
            return " - "+self.commandName+": "+self.description
        else:
            return " - "+self.commandName+": "+self.description+"\nUsage Example: "+self.usageDetails