test_value = False
class GameState:    
#    @staticmethod
# #   def get_instance():
#        """ Static access method. """
#        if GameState.__instance is None:
#            return GameState.__init__()
#        return GameState.__instance
#    #save_file_version="RT001"
#   @staticmethod  
# #   def __init__():
#        """ virtually private constructor """
#        if __instance != None:
# #           raise Exception("There can be only one... GameState.")
#        else:
#            __instance = True
    #def restore(self, filename):
    #    self.store(default_save_file)
    def __init__(self):
        self.__instance = True 
        self.save_file_version="RT001"
        self.current_room_leader = "Current room: "    
        self.default_save_file = "zorkSave"
        self.save_file_ext= ".sav"
        self.current_room_leader = "Current room: " 
        self.adventurers_curret_room = None
    def manual_state(self):
        self.__instance = True 
        self.save_file_version="RT001"
        self.current_room_leader = "Current room: "    
        self.default_save_file = "zorkSave"
        self.save_file_ext= ".sav"
        self.current_room_leader = "Current room: " 
        self.adventurers_curret_room = None
        return self
    def store(self,saveName,dungeon):
        fileName = saveName+self.save_file_ext
        saveFile = open(fileName,"a")
        saveFile.write(self.save_file_version)
        dungeon.StoreState(saveFile)
        saveFile.write(self.current_room_leader+self.adventurers_curret_room.getName())
        saveFile.close()

    def initialize(self, dungeon):
        self.dungeon = dungeon
        self.test = True
        self.adventurers_curret_room = self.dungeon.entry
    
    def get_adventurers_current_room(self):
        return self.adventurers_curret_room
    
    def set_adventurers_current_room(self, room):
        self.adventurers_curret_room = room
