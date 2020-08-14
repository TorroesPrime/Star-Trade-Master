from game_state import game_state_instance

class MovementCommand():
    commandString = ""
    MOVEMENT_COMMANDS = "nsweud"

    def __init__(self,direction):
        self.dir = direction

    def execute(self):
        currentRoom = game_state_instance.get_adventurers_current_room()
        nextRoom = currentRoom.leave_by(dir)
        if nextRoom != None:
            game_state_instance.set_adventurers_current_room(nextRoom)
        else:
            print(f"Sorry, you can't go {self.dir} from {currentRoom.name}.")