import json
import os
import class_exit
import class_item
import dungeon
import character
import room
import adventure_loader
from character import Character as char
from dungeon import Dungeon as dungeon
from class_exit import Exit 
from class_item import item as item
from room import Room
from game_state_instance import game_state_instance as gsi
os.chdir("..\\")
def char_builder(char):
    char_stats = [char["name"],char["weapon skill"],char["ballistic skill"],char["strength"],char["Toughness"],char["Agility"],char["Intelligence"],char["Perception"],char["Will Power"],char["Fellowship"],char["Home world"],char["motivation"],char["Gender"],char["Wounds"]]
    return char_stats
def exit_builder(exit):
    direction = exit["direction"]
    source_room = exit["source room"]
    destination_room = exit["destination room"]
    return class_exit.Exit(direction,source_room,destination_room)
def item_builder(item):
    item_stats = [item["name"],item["description"],item["weight"],item["actions"],]
    return item_stats
def room_builder(room):
    name = room["name"]
    desc = room["desc"]
    inventory = room["inventory"]
    if gsi.test_value:
        print("Room "+name+" created")
        print("description: "+desc)
    room_data = [name,desc,inventory]
    return room_data
def dungeon_builder(dungeon):
    pass
def adventur_builder(adv_info):
    fileName = adv_info["file name"]
    name = adv_info["name"]
    desc = adv_info["desc"]
with open("test_file.adv",'r') as adv:
    module = json.load(adv)
print(module["name"])
#print(module["description"])
#print(module["version"])
adv_data ={"file name":"test_file.adv", "name":module["name"], "desc":module["description"]}
#adventur_builder(adv_data)

characters = []
items = []
rooms = [module["name"]]
exits = []
dungeon_rooms =[module["name"]]
dungeon_exits = []
dungeon_npcs = []
dungeon_items = []
for value in module['npcs']:
    characters.append(char_builder(value))
for value in module["items"]:
    items.append(item_builder(value))
for value in module["rooms"]:
    rooms.append(room_builder(value))
for value in module["exits"]:
    exits.append(exit_builder(value))
for entry in characters:
    char(entry)

for entry in rooms:
    dungeon_rooms.append(Room(entry))
test_room = Room(rooms[1])
#print(type(test_room))
if gsi.test_value:
    print("Module[\"name\"]:"+str(module["name"])+" of type "+str(type(module["name"])))
    print("dungeon_rooms:"+str(type(dungeon_rooms[1])))
    print("dungeon_rooms[1]:"+str(dungeon_rooms[1]))


dungeon_map = dungeon(module["name"],dungeon_rooms[1])
if gsi.test_value:
    print("Dungeon map created")
for room in dungeon_rooms[1:]:
    dungeon_map.add_room(room)
    if gsi.test_value:
        print(room.name+"Room added")