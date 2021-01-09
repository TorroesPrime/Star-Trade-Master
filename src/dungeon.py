from filemedia import top_level_delimiter,second_level_delim,room_states_marker,rooms_marker,supported_file_versions,file_name_leader
#from room import roomInstance
import room
from game_state_instance import game_state_instance as gsi
#from room import Room
class Dungeon:
    def __init__(self,title,entry):
        self.filename = None
        self.title = title
        self.entry = entry
        self.rooms = {}

    def manual_Dungeon(self,title,entry):
        """manual dungeon instantiation method"""
        self.filename = None
        self.title = title
        self.entry = entry
        self.rooms = {}
        return self

    def dungeon(self,filename,entry):
        """Read from the .zork filename passed, and instantiate a Dungeon object based on it."""
        self.filename = filename
        with open(filename) as f:
        #fileReader = open(filename)
            self.title = f.readline()
         #   if test==True:
         #       print(f"title:{self.title}")
            if f.readline()!=top_level_delimiter:
                raise Exception(f"No {top_level_delimiter} after version indicator")
            if f.readline()!=rooms_marker:
                raise Exception(F"No {rooms_marker} line were expected")
            try:
                self.add_room(self.entry)
                self.entry = self.get_room(entry)
            except:
                raise Exception("No room found")
            #try:
                #self.addRoom(RoomInstance.RoomMaker(f))
            #except:
            #    raise Exception(f"no more rooms")
            #if f.readline()!=self.EXITS_MARKER:
            #    raise Exception(f"Illegal dungeon file format")
    @staticmethod
    def scanner(filename):
        with open(filename) as a:
            adv_data = []
            for line in a.readlines():
                adv_data.append(line.strip("\n"))
            

            dungeon_title = a.readline()
            dungeon_desc = ""
            test_line = a.readline()
            if gsi.test_value:
                print(f"test_line:{test_line}")
            if test_line.startswith("Description: ")== False:
                dungeon_desc = ""
            else:
                dungeon_desc = test_line
            if gsi.test_value:
                print(f"dungeon_desc:{dungeon_desc}")
            check_version = a.readline().replace("Version:","")
            if gsi.test_value:
                print(f"check_version:{check_version}")
            if check_version not in supported_file_versions:
                raise Exception("This adventure module is not supported by this version of the game.")
            else:
                check_line = a.readline()
                if gsi.test_value:
                    print(f"check_line:{check_line}")
                if check_line != top_level_delimiter:
                    raise Exception("Invalid adventure format")




                



    def store_state(self,saveFile):
        saveFile.write(file_name_leader +str(self.filename)+"\n")
        saveFile.write(room_states_marker+"\n")
        for entry in self.rooms.values():
            if gsi.test_value:
                print(entry)
            entry.store_state(saveFile)
        saveFile.write(top_level_delimiter+"\n")

    def restore_state(self, readFile):
        if(readFile.readLine()!=room_states_marker):
            raise Exception(F"no {room_states_marker} after dungeon filename in file")
        roomName = readFile.nextLine()
        while(roomName!=top_level_delimiter):
            print("need to check this")
    
    def add_room(self, room):
        roomName = room.name
        self.rooms.update({roomName:room}) 
    
    def get_room(self, roomName):
        return self.rooms.get(roomName)

#dungeonInstance = Dungeon("dungeon instance",roomInstance)    