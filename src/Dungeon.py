import GameState
class Dungeon:
    TOP_LEVEL_DELIM = "==="
    SECOND_LEVEL_DELIM = "---"
    ROOMS_MARKER = "Rooms:"
    EXITS_MARKER = "Exits:"
    FILE_NAME_LEADER = "Dungeon file: "
    ROOM_STATES_MARKER = "Room states:"
    
    def manDungeon(self,title, entry):
        """manual dungeon instantiation method"""
        __init__()
        self.filename = null
        self.title = title
        self.entry = entry
        self.Rooms = {}

    def Dungeon(self,filename):
        """Read from the .zork filename passed, and instantiate a Dungeon object based on it."""
        __init__()
        self.filename = filename
        fileReader = open(filename)
        self.title = fileReader.readline()
        if GameState.test==True:
            print(f"title:{self.title}")
        if fileReader.readline()!=TOP_LEVEL_DELIM:
            raise Exception(f"No {TOP_LEVEL_DELIM} after version indicator")
        if fileReader.readline()!=ROOMS_MARKER:
            raise Exception(F"No {ROOMS_MARKER} line were expected")
        try:
            self.entry = Room(s)
            add(entry)
        try:
            add(Room(s))
        except expression as identifier:
            raise Exception(f"no more rooms")
        





        

