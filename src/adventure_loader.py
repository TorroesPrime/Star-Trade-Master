import os
from os.path import isfile, join
from filemedia import save_file_ext, save_file_version
import dungeon as d
import room as r
import class_exit as e

testFiles = os.listdir("adventures")
def readAdvFiles(supplied_file):
    adventure_object = []
    with open(supplied_file) as f:
        for line in f.readlines():
            adventure_object.append(line.strip("\n"))
    for line in adventure_object:
        print(line)
    if adventure_object[1] != "Version:"+save_file_version:
        print("This file is not valid for this verison of Star Trader: Destiny")
    else:
        pass

        
for files in testFiles:
    print(files)

readAdvFiles("adventures\\testFile.adv")
