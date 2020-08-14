from filemedia import save_file_ext
from abc import ABC, abstractmethod
from filemedia import default_save_file,save_file_version,save_file_ext

class SaveCommand(): 
    def __init__(self):
        self.default_save_file = default_save_file+save_file_ext

    def execute(self):
        save_file_name = input("Enter file save name, or leave blank and press enter to accept default save name: ")
        if save_file_name == "":
            print("Data saved to "+self.default_save_file)            
        else:
            print("Data saved to "+save_file_name+save_file_ext)