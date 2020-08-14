import Dungeon

class GameState:
    __instance = None
    SAVE_FILE_VERSION="RT001"
    CURRENT_ROOM_LEADER = "Current room: "    
    DEFAULT_SAVE_FILE = "zorkSave"
    SAVE_FILE_EXT= ".sav"
    CURRENT_ROOM_LEADER = "Current room: " 
    test = True
    
    @staticmethod
    def getInstance(self):
        """ Static access method. """
        if GameState.__instance == None:
            GameState()
        return GameState.__instance
    #SAVE_FILE_VERSION="RT001"
       
    def __init__(self):
        """ virtually private constructor """
        if GameState.__instance != None:
            raise Exception("There can be only one... GameState.")
        else:
            GameState.__instance = self

    #def restore(self, filename):
    #    self.store(DEFAULT_SAVE_FILE)
    
    def store(self,saveName):
        fileName = saveName+GameState.SAVE_FILE_EXT
        saveFile = open(fileName,"a")
        saveFile.write(GameState.SAVE_FILE_VERSION)
        Dungeon.StoreState(saveFile)
        saveFile.write(GameState.CURRENT_ROOM_LEADER+getAdventurersCurrent().getName())
        saveFile.close()

    def initialize(self, dungeon):
        self.dungeon = dungeon
        self.test = True
        adventurersCurretRoom = Dungeon.getEntry()

    def getAdventurersCurrentRoom(self):
        return 
