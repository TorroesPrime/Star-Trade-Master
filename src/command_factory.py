from re import search
from game_state import game_state_instance as gsi
import movement_command as move
from save_command import SaveCommand
MOVEMENT_COMMANDS = "nsweud"

class CommandFactory:
    def __init__(self,command):
        a = str(command).casefold()
        self.commandString = a

    def execute_command(self):
        if self.commandString =="save":
           # store(defaultSaveFile)
           if gsi.test_value:
               print("save command")
           return SaveCommand().execute()
        if self.commandString == "look":
            print(gsi.adventurers_current_room.describe())
        elif search(self.commandString, MOVEMENT_COMMANDS):
            if gsi.test_value:
                print("movement command")
            command = move.MovementCommand(self.commandString)
            return command.execute()

            