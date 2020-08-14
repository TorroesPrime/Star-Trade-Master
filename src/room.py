from dungeon import top_level_delimiter, second_level_delim
class Room:
    name = ""
    desc = ""
    been_here =""
    exits = []
    def __init__(self,name,desc,exits):
       self.been_here = False
       self.name = name
       self.desc = desc
       self.add_exit(exits)

    def manuel_room(self,name,desc,exits):
        """manual instanstiator for room objects. Requires a string for the name of the room, a string that is a description of the room, and a list of one or more exits"""
        self.name = name
        self.desc = desc
        self.add_exit(exits)
        return self
    
    def add_exts(self, exits):
        """takes a list of exits and adds each one to the room's exits list"""
        for exit in exits:
            self.add_exit(exit)
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
        if(self.been_here):
            description = self.name
        else:
            description = self.name+"\n"+self.desc+"\n"
        for exit in self.exits:
            description = description + "\n"+exit.describe()
        self.been_here = True
        return description

    def leave_by(self, direction):
        for exit in self.exits:
            if exit.getdirection() == direction:
                return exit.getDest()
        return None

    def add_exit(self, exit):
        self.exits.append(exit)




    



