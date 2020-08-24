from re import search
from game_state import game_state_instance as gsi
import movement_command as move
from save_command import SaveCommand
from unknown_command import UnknownCommand
import character
MOVEMENT_COMMANDS = "nsweud"

class CommandFactory:
    def __init__(self,command):
        a = str(command).casefold().split()
        if gsi.test_value:
            print(a)
        if len(a)>1:
            self.commandString = a[0]
            self.nounString = a[1]
        else:
            self.commandString = a[0]

    def execute_command(self):
        if self.commandString =="save":
           # store(defaultSaveFile)
           if gsi.test_value:
               print("save command")
           return SaveCommand().execute()
        elif self.commandString == "look":
            if gsi.test_value:
                print("look command")
            print(gsi.adventurers_current_room.describe())
        elif search(self.commandString, MOVEMENT_COMMANDS):
            if gsi.test_value:
                print("movement command")
            command = move.MovementCommand(self.commandString)
            return command.execute()
        elif self.commandString == "drop":
            if self.nounString == "all":
                if gsi.test_value:
                    print("Drop all command")
            else:
                if gsi.test_value:
                    print("drop command")
        elif self.commandString == "i" or self.commandString == "inventory":
            if gsi.test_value:
                print("inventory")
        elif self.commandString == "score":
            if gsi.test_value:
                    print("score command")
        elif self.commandString == "wound":
            if gsi.test_value:
                print("wound command")
                wound_amount = input("How many wounds should be inflicted?")
            else:
                return UnknownCommand("wound").execute()    
        elif self.commandString == "talk":
            if gsi.test_value:
                print("talk command")
        elif self.commandString == "carry":
            if gsi.test_value:
                print("carry command")
        elif self.commandString == "view":
            if self.nounString == "stats":
                gsi.player_character.character_sheet()
        else:
            if gsi.test_value:
               print("unknown command")
            string_value = self.commandString+" "+self.nounString
            return UnknownCommand(string_value).execute()

            