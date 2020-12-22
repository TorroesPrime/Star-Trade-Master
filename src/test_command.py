
from abc import ABC, abstractmethod
from game_state_instance import game_state_instance as gsi

class TestCommand(): 
    def __init__(self):
        self.commandName = "Test Command"
        self.description = "Used for setting the 'test' value of the game state used for development and function testing."
        self.usage = "> test"
        self.usageDetails = "sets the test flag"
    
    def getStr(self):
        return "Test Command"

    def execute(self):
        gsi.set_test()
        return "Test value set to: "+str(gsi.test_value)