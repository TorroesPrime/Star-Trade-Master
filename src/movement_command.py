from game_state import game_state_instance as gsi

class MovementCommand():
    commandString = ""
    MOVEMENT_COMMANDS = "nsweud"

    def __init__(self,direction):
        self.dir = direction

    def execute(self):
        currentRoom = gsi.get_adventurers_current_room()
        if gsi.test_value:
            print(f"current room:{currentRoom.name}")
        nextRoom = currentRoom.leave_by(self.dir)
        if gsi.test_value:
            print(f"next room:{nextRoom.name}")
        if nextRoom != None:
            gsi.adventurers_current_room=nextRoom
            print(gsi.adventurers_current_room.describe())
            gsi.adventurers_current_room.been_here = True
        else:
            print(f"Sorry, you can't go {self.dir} from {currentRoom.name}.")