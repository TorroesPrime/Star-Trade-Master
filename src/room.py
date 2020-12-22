from dungeon import top_level_delimiter, second_level_delim
from game_state_instance import game_state_instance as gsi
import class_exit
class Room:
    def __init__(self,name,desc):
       self.been_here = False
       self.name = name
       self.desc = desc
       self.exits = []
       self.inventory = []
       self.been_here = False
#       self.add_exits(exits)
    
    def add_exit(self, exit):
        self.exits.append(exit)
    
    def add_exits(self, exits):
        """takes a list of exits and adds each one to the room's exits list"""
        for entry in exits:
            self.add_exit(entry)
   
    def scanner_room(self,f):
        """Read from the .zork filename passed, and instantiate a Room object based on it."""
        self.name = f.readline()
        if(self.name == top_level_delimiter):
            raise Exception("Invalid dungeon format")
        lines_Of_desc = f.readline()
        while lines_Of_desc != second_level_delim & lines_Of_desc != top_level_delimiter:
            self.desc = self.desc+lines_Of_desc+"\n"
            lines_of_desc = f.readline()
        if lines_of_desc != second_level_delim:
            raise Exception(f"Invalid dungeon format: No {second_level_delim} after room")
        return self

    #def RoomMaker(self, f):
    #    return self.RoomScan(f)
    def store_state(self,save_file):
        """Stores the current state of this room to the filename passed to it."""
        if self.been_here:
            save_file.write(self.name+":")
            save_file.write("been_here:true")
            save_file.write(second_level_delim)

    
    def restore_state(self, f):
        line = f.readline().split(":")
        if line[0]!="been_here":
            raise Exception("No been_here value")
        if line[1]=="true":
            self.been_here = True
        else:
            self.been_here = False
    
    def describe(self):
        description = ""
        if(self.been_here == True):
            description = self.name
        else:
            description = self.name+"\n"+self.desc+"\n"
        for entry in self.exits:
            description = description + "\n"+entry.describe()
        self.been_here = True
        return description
    def full_describe(self):
        description = self.name+"\n"+self.desc+"\n"
        items = "the room contains: "
        for entry in self.exits:
            description = description + "\n"+entry.describe()
        for item in self.inventory:
            items = items + item.name
        description = description+"\n"+items+"."

        return description

    def leave_by(self, direction):
        for e in self.exits:
            if gsi.test_value:
                print(f"source room:{e.source_room.name}")
                print(f"destination room:{e.destination_room.name}")
            if e.get_direction() == direction:
                return e.get_destination()
            else:
                return None
    
    def list_exits(self):
        for e in self.exits:
            print(f"Source room: {e.get_source().name}")
            print(f"Direction: {e.get_direction()}")
            print(f"Destination room: {e.get_destination().name}")
    
    def add_item(self,item):
        self.inventory.append(item)




roomInstance = Room("blankroom","method acces")
    



