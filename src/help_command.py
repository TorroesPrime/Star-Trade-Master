from game_state_instance import game_state_instance as gsi
import movement_command as move
from save_command import SaveCommand
from unknown_command import UnknownCommand
from take_command import TakeCommand
from look_command import LookCommand
from inventory_command import InventoryCommand
class HelpCommand():
    def __init__(self):
        self.name = "Help Command"
        move_command = move.MovementCommand("n")
        save = SaveCommand()
        take = TakeCommand("Take test")
        look = LookCommand()
        print("test before")
        inv = InventoryCommand()
        print("test after")
        self.commandList = [move_command,save,take,look,inv]
    def execute(self):
        for command in self.commandList:
            print(command.details(True))
        return "Help Command Complete"