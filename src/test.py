class room:
    def __init__(self,name,desc):
        self.name = name
        self.desc = desc
    def get_name(self):
        return self.name
testDict = {}
room1 = room("room one","this one room")
room2 = room("room two","this two room")
room3 = room("room three","this three room")
room4 = room("room 4","this four room")
room5 = room("room 5","this five room")
testDict.update({room1.name:room1})
testDict.update({room2.name:room2})
testDict.update({room3.name:room3})
testDict.update({room4.name:room4})
testDict.update({room5.name:room5})
for room in testDict.values():
    print(room.get_name())
