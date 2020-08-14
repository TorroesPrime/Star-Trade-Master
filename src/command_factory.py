from re import search

import movement_command as move
from save_command import SaveCommand
#import movement_command as move
MOVEMENT_COMMANDS = "nsweud"

class CommandFactory:
    def __init__(self,command):
        a = str(command).casefold()
        self.commandString = a

    def execute_command(self):
        if self.commandString =="save":
           # store(defaultSaveFile)
           print("save command")
           return SaveCommand().execute()
        elif search(self.commandString, MOVEMENT_COMMANDS):
            print("movement command")
            return move.MovementCommand(self.commandString)

            