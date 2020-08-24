import os
from os.path import isfile, join
from filemedia import save_file_ext, save_file_version,supported_file_versions
import dungeon as d
import room as r
import class_exit as e
#from interpreter import gsi
test_value = False


class adventure_object():
    def __init__(self,fileName,name,desc):
        self.fileName = fileName
        self.name = name
        self.desc = desc
        self.supported = False

testFiles = os.listdir("adventures")
def adventure_file_loader(fileName):
    """ takes a supplied adventure file and reads it into an adventure object"""
    file_contents_list = []
    if fileName.endswith("adv") != True:
        raise Exception("Invalid file format")
    with open(fileName,"r") as a:
        for line in a.readlines():
            file_contents_list.append(line.strip("\n"))
        if file_contents_list[2].startswith("Version:"):
            file_contents_list[2] = file_contents_list[2].replace("Version:","") 
            if file_contents_list[2] in supported_file_versions:
                if test_value:
                    print("supported adventure module")
                name = file_contents_list[0]
                desc = file_contents_list[1]
                adventure_mod =adventure_object(fileName,name,desc)
                return adventure_mod
        else:
            raise Exception("Invalid adventure format")

def load_modules(directory):
    valid_modules = []
    if test_value:
        print("directory:"+directory)
    for file in os.listdir(directory):
        if file.endswith("adv"):
            filename = directory+file
            if test_value:
                print(filename)
            valid_modules.append(adventure_file_loader(filename))
            if test_value:
                print("Check value of 'file':"+file)
    return valid_modules

def select_modules(valid_modules):
    """returns the file name of an adventure module"""
    print("Availible Adventure modules:")
    value_selector = 1
    for entry in valid_modules:
        print(f"[{value_selector}]: {entry.name}")
        print(f"   {entry.desc}")
        value_selector = value_selector+1
    print("Type the number of the adventure module you want to load")
    a = int(input())-1
    return valid_modules[a].fileName


#a = adventure_file_loader("adventures/testFile.adv")
#load_modules("adventures/")
#select_modules(load_modules("adventures/"))