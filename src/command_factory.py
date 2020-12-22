from re import search
from game_state_instance import game_state_instance as gsi
import movement_command as move
from save_command import SaveCommand
from unknown_command import UnknownCommand
from help_command import HelpCommand
from look_command import LookCommand
from test_command import TestCommand
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
        elif len(a)==1:
            self.commandString=a[0]
            self.nounString=""
        else:
            self.commandString = a[0]

    def execute_command(self):
        command = "No Command"
        if self.commandString =="save":
          # store(defaultSaveFile)
            if gsi.test_value:
              print("save command")
            command = SaveCommand().execute()
           #return SaveCommand().execute()
        elif self.commandString == "look":
            if gsi.test_value:
                print("look command")
            command = LookCommand().execute()
           # print(gsi.adventurers_current_room.describe())
           
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
                command = UnknownCommand("wound").execute()    
        elif self.commandString == "talk":
            if gsi.test_value:
                print("talk command")
        elif self.commandString == "carry":
            if gsi.test_value:
                print("carry command")
        elif self.commandString == "view":
            if self.nounString == "stats":
                command = gsi.player_character.character_sheet()
                print(command)
        elif self.commandString =="test":
            command = TestCommand().execute()
        elif self.commandString == "help":
            if gsi.test_value:
                print("help command")
            command = HelpCommand().execute()
        else:
            if gsi.test_value:
               print("unknown command")
            string_value = self.commandString+" "+self.nounString
            command = UnknownCommand(string_value).execute()
        print(command)
        return command.execute()

            