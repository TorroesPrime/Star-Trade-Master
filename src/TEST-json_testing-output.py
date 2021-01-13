import json
import os
import class_exit
import class_item
import dungeon
import character
import room
import adventure_loader
from character import Character as char
from dungeon import Dungeon
from class_exit import Exit 
from class_item import item as item
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
print(module["description"])
print(module["version"])
adv_data ={"file name":"test_file.adv", "name":module["name"], "desc":module["description"]}
adventur_builder(adv_data)

characters = []
items = []
rooms = [module["name"]]
exits = []
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
dungeon_map = dungeon_builder(rooms)