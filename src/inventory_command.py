"""command to allow player to view their inventory"""
from filemedia import inv_header, item_examples
from tools import spacer
from game_state_instance import game_state_instance as gsi

class InventoryCommand():
    """inventory command deifnition"""
    def __init__(self):
        #command_string_list = commandString.split()
        self.command_name = "Inventory Command"
        self.description = "Displays player current inventory."
        list_of_items = ""
        for item in item_examples:
            item_name = item.name
            item_weight = item.weight
            list_of_items = list_of_items+spacer(item_name, 25)+"|"+\
                spacer(str(item_weight), 12)+"|\n"
        self.usage = "> i =or= >inventory =or= >inven"
        self.usage_details = "> i =or= >inventory =or= >inven \n"+\
            inv_header+"\n"+list_of_items
    def execute(self):
        """executiong for an inventory command: Shows the player inventory"""
        inventory = "inventory Command"
        if len(gsi.player_character.inventory) == 0:
            inventory = "You are not currently carrying anything."
        else:
            if gsi.test_value:
                print("Inventory size:"+str(len(gsi.player_character.inventory)))
            print(inv_header)
            current_inventory_weight = 0
            for item in gsi.player_character.inventory:
                print("|"+spacer(item.name, 25)+"|"+\
                    spacer(str(item.weight), 12)+"|\n")
                current_inventory_weight = current_inventory_weight+item.weight
            print("Total present weight: "+str(current_inventory_weight)+"/"+str(gsi.\
                player_character.max_weight)+" pounds")
                #inventory = inv_header+"\n"+"|"+spacer(item.name, 25)+"|"+\
                #    spacer(str(item.weight), 12)+"|\n"
            #print(inventory)
            inventory = ""
        return inventory
    def details(self, details):
        """ Method docstring"""
        if details is not True:
            return " - "+self.command_name+": "+self.description+"\n"
        else:
            return " - "+self.command_name+": "+self.description+\
                "\nUsage Example: "+self.usage_details
