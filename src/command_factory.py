from re import search
from game_state import test_value
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
           if test_value:
               print("save command")
           return SaveCommand().execute()
        elif search(self.commandString, MOVEMENT_COMMANDS):
            if test_value:
                print("movement command")
            command = move.MovementCommand(self.commandString)
            return command.execute()

            
            
