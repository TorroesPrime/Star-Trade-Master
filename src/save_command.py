from filemedia import default_save_file,save_file_version,save_file_ext
from game_state import game_state_instance as gsi

class SaveCommand(): 
    def __init__(self):
        self.default_save_file = default_save_file+save_file_ext

    def execute(self):
        save_file_name = input("Enter file save name, or leave blank and press enter to accept default save name: ")
        if save_file_name == "":
            save_file= self.default_save_file           
        else:
            save_file = save_file_name+save_file_ext 
        gsi.store(save_file)
        print("Data saved to "+save_file)