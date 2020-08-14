from filemedia import second_level_delim,top_level_delimiter


class Exit:
    direction = ""
    source_room = ""
    destination_room = ""

    def manuel_exit(self,direction,source_room,destination_room):
        self.dir = direction
        self.source_room = source_room
        self.destination_room = destination_room
        self.source_room.addExit(self)
        return self

    def __init__(self, direction,source_room,destination_room):
        self.dir = direction
        self.source_room = source_room
        self.destination_room = destination_room
        self.source_room.add_exit(self)

    def scanner_exit(self,f,d):
        pass

    def describe(self):
        return f"You can go {self.direction} to the {self.destination_room.getName()}."
    
    def get_direction(self):
        return self.direction
    
    def get_source(self):
        return self.source_room
    
    def get_destination_roomination(self):
        return self.destination_room



