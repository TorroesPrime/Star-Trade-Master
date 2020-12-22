from filemedia import default_save_file,save_file_version,save_file_ext
from game_state_instance import game_state_instance as gsi

class SaveCommand(): 
    def __init__(self):
        self.default_save_file = default_save_file+save_file_ext
        self.commandName = "Save Command"
        self.description = "Saves the current gamestate to a .sav file."
        self.usage = "> save save1  -or- save  -or- save save1.sav"
        self.usageDetails = "if no save file name is supplied, the default save file name is used."

    def execute(self):
        save_file_name = input("Enter file save name, or leave blank and press enter to accept default save name: ")
        if save_file_name == "":
            save_file= self.default_save_file           
        else:
            save_file = save_file_name+save_file_ext 
        gsi.store(save_file)
        return "Data saved to "+save_file
    def details(self,details):
        """ Method docstring"""
        if(details != True):
            return self.description
        else:
            return " - "+self.commandName+": "+self.description+"\nUsage Example: "+self.usageDetails