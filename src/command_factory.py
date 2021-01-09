"""takes string input and constructs command output based on it"""
from re import search
from game_state_instance import game_state_instance as gsi
import movement_command as move
from save_command import SaveCommand
from unknown_command import UnknownCommand
from help_command import HelpCommand
from look_command import LookCommand
from test_command import TestCommand
from take_command import TakeCommand
from inventory_command import InventoryCommand
MOVEMENT_COMMANDS = "nsweud"

class CommandFactory:
    """defines a command"""
    def __init__(self, command):
        a___ = str(command).casefold().split()
        if gsi.test_value:
            print(a___)
        if len(a___) > 1:
            self.command_string = a___[0]
            self.noun_string = a___[1]
        elif len(a___) == 1:
            self.command_string = a___[0]
            self.noun_string = ""
        else:
            self.command_string = a___[0]

    def execute_command(self):
        """command action"""
        command = "No Command"
        if self.command_string == "save":
          # store(defaultSaveFile)
            if gsi.test_value:
                print("save command")
            command = SaveCommand().execute()
           #return SaveCommand().execute()
        elif self.command_string == "look":
            if gsi.test_value:
                print("look command")
            command = LookCommand().execute()
           # print(gsi.adventurers_current_room.describe())
        elif search(self.command_string, MOVEMENT_COMMANDS):
            if gsi.test_value:
                print("movement command")
            command = move.MovementCommand(self.command_string)
            return command.execute()
        elif self.command_string == "drop":
            if self.noun_string == "all":
                if gsi.test_value:
                    print("Drop all command")
            else:
                if gsi.test_value:
                    print("drop command")
        elif self.command_string == "i" or self.command_string == "inventory" \
            or self.command_string == "inven":
            if gsi.test_value:
                print("inventory command")
            command = InventoryCommand().execute()
        elif self.command_string == "score":
            if gsi.test_value:
                print("score command")
        elif self.command_string == "wound":
            if gsi.test_value:
                print("wound command")
                wound_amount = input("How many wounds should be inflicted?")
                print(wound_amount)
            else:
                command = UnknownCommand("wound").execute()
        elif self.command_string == "talk":
            if gsi.test_value:
                print("talk command")
        elif self.command_string == "carry":
            if gsi.test_value:
                print("carry command")
        elif self.command_string == "view":
            if self.noun_string == "stats":
                command = gsi.player_character.character_sheet()
                print(command)
        elif self.command_string == "test":
            command = TestCommand().execute()
        elif self.command_string == "help":
            if gsi.test_value:
                print("help command")
            command = HelpCommand().execute()
        elif self.command_string == "take":
            if gsi.test_value:
                print("take command")
            command = TakeCommand(self.noun_string).execute()
        else:
            if gsi.test_value:
                print("unknown command")
            string_value = self.command_string+" "+self.noun_string
            command = UnknownCommand(string_value).execute()
        print(command)
        return command
            