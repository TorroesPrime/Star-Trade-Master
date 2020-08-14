
from abc import ABC, abstractmethod


class Command(): 
    def __init__(self,dir):
        self.commandString = dir
    
    def getStr(self):
        return self.commandString

    def execute(self):
        pass            