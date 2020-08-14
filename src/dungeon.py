from filemedia import save_file_ext,save_file_version,default_save_file,top_level_delimiter,second_level_delim,rooms_marker,exits_marker,file_name_leader,room_states_marker

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

    def store_state(self,saveFile):
        saveFile.write(file_name_leader +self.filename)
        saveFile.write(room_states_marker)
        for room in self.rooms:
            room.storeState(saveFile)
        saveFile.print(top_level_delimiter)

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