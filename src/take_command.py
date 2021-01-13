from game_state_instance import game_state_instance as gsi
#import room
#import class_item


class TakeCommand(): 
    def __init__(self,item):
        self.commandName = "take Command"
        self.description = "Takes the specified item and adds it to the player inventory."
        self.usage = "> take hammer"
        self.usageDetails = "if an item matching the name supplied is not found in the room, displays a message saying no such item found in current room."
        self.item = item.lower()

    def execute(self):
       # room_inventory = gsi.get_adventurers_current_room().inventory
       # for item in gsi.adventurers_current_room.inventory:
       #     print("Item name:"+item.name)
        #    item_name = item.name
        #    room_inventory.append(item_name)
        #print("Room Contents:")
        #for item in room_inventory:
        #    print(item)
        #room_inventory = []
        #for item in gsi.get_adventurers_current_room().inventory:
        #    name = item.name.lower()
        #    room_inventory.append(name)
        #    if gsi.test_value:
        #        print(item.name)
        response = ""
        if self.item == "all":
            response = ""
            for item in gsi.get_adventurers_current_room().inventory:
                gsi.player_character.add_item(item)
                gsi.get_adventurers_current_room().remove_item(item)
                response = response+item.name + " added to your inventory. \n"
        else:
            for item in gsi.get_adventurers_current_room().inventory:
                if gsi.test_value:
                    print("item name:"+item.name.lower())
                    print("search name:"+self.item.lower())
                if self.item == item.name.lower():
                    gsi.player_character.add_item(item)
                    gsi.adventurers_current_room.inventory.remove(item)
                    response = self.item + " added to your inventory."
                    break
                else:
                    response = "No "+self.item+" found in the room."
        return response

    def details(self,details):
        """ Method docstring"""
        if(details != True):
            return " - "+self.commandName+": "+self.description
        else:
            return " - "+self.commandName+": "+self.description+"\nUsage Example: "+self.usageDetails