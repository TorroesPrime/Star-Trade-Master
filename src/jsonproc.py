import json
import os
import class_exit
import class_item
import dungeon
import character
import room as room
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
rooms = []
exits = []
dungeon_rooms =[module["name"]]
if gsi.test_value:
    print("Dungeon Rooms created")
    print(dungeon_rooms)
dungeon_exits = []
dungeon_npcs = []
dungeon_items = []
for value in module['npcs']:
    print("npcs:")
    print(value)
    characters.append(char_builder(value))
for value in module["items"]:
    print("items:")
    print(value)
    items.append(item_builder(value))
for value in module["rooms"]:
    print(value)
    room_value = room_builder(value)
    room_a=room.Room(room_value)
    if gsi.test_value:
        print("Value 1: "+room_value[0])
        print("Value 2: "+room_value[1])
        print("Room Name: "+room_a.name)
        print("Room desc: "+room_a.desc)
        print(room_a.name)
    rooms.append(room_a)
for value in module["exits"]:
    exits.append(exit_builder(value))
for entry in characters:
    char(entry)
for entry in rooms:
    dungeon_rooms.append(entry)
    if gsi.test_value:
        print("dungeon_rooms:")
        print(dungeon_rooms)
        print("entry")
        print(entry)
if gsi.test_value:
    print("Module[\"name\"]:"+str(module["name"])+" of type "+str(type(module["name"])))
    print("dungeon_rooms:"+str(type(dungeon_rooms[1])))
    print("dungeon_rooms[1]:"+str(dungeon_rooms[1]))
    print(dungeon_rooms)
    for room in dungeon_rooms:
        print(type(room))


dungeon_map = dungeon(module["name"],dungeon_rooms[1])
if gsi.test_value:
    print("Dungeon map created")
for entry in dungeon_rooms[1:]:
    if gsi.test_value:
        print(str(type(entry)))
    dungeon_map.add_room(entry)
    if gsi.test_value:
        print(room.name+"Room added")