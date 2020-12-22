from game_state_instance import game_state_instance as gsi
import movement_command as move
from save_command import SaveCommand
from unknown_command import UnknownCommand
from take_command import TakeCommand
from look_command import LookCommand
class HelpCommand():
    def __init__(self):
        self.name = "Help Command"
        move_command = move.MovementCommand("n")
        save = SaveCommand()
        take = TakeCommand("Take test")
        look = LookCommand()
        self.commandList = [move_command,save,take,look]
    def execute(self):
        for command in self.commandList:
            print(command.details(True))
        return "Help Command Complete"