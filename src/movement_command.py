from command import Command

class MovementCommand(Command):
    commandString = ""
    MOVEMENT_COMMANDS = "nsweud"

    def __init__(self,s):
        self.dir = s

    def execute(self):
        print("You moved")