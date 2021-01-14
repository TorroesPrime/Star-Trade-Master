"""builds a simple dungeon for testing an development."""
from room import Room
from game_state_instance import game_state_instance as gsi
from class_exit import Exit
from dungeon import Dungeon
#from command_factory import CommandFactory
#from command import Command
from character import Character as char
from character import characteristic_gen as cgen
from filemedia import dice
from class_item import item

d10_01 = dice(10)
d10_02 = dice(10)
d10_03 = dice(10)
d10_04 = dice(10)
d6_01 = dice(4)
d6_02 = dice(4)
d6_03 = dice(4)
d6_04 = dice(4)


def test_dungeon_build():
    """method to build a dungeon for testing and dev."""
    dungeon_name = "Test Dungeon"
    room_one_date =["Entry Room", "The first room in the test dungeon"]
    room_one = Room(room_one_date)
    roomtwo_data = ["second Room", "The second room of the test dungeon"]
    room_two = Room(roomtwo_data)
    exit1 = Exit("n", room_one, room_two)
    exit2 = Exit("s", room_two, room_one)
    room_one.add_exit(exit1)
    room_two.add_exit(exit2)
    test_dungeon = Dungeon(dungeon_name, room_one)
    test_dungeon.add_room(room_two)
    item_one_stats = ["Apple", "A red Fuji Apple", .2]
    item_one_actions = {"eat": "consume-You eat the apple", "examine": "It's a\
         red apple. It looks really tasty.", "throw": "destroy-You hurl the \
             apple agaisnt the wall. It smashes agaisnt it with a splat."}
    item_one_date = ["Apple", "A red Fuji Apple", 0.2,item_one_actions]
    item_one = item(item_one_date)
    item_two_stats = ["Spoon", "a metal spoon", .01]
    item_two_actions = {"examine": "examine-The spoon is made of some form of lite metal, perhaps tin.", "throw": "remove-You hurl the \
             spoon agaisnt the wall. It clashes against the wall with a clatter."}
    item_two_data = ["Spoon", "a metal spoon", 0.01,item_two_actions]
    item_two = item(item_two_data)
    room_one.add_item(item_one)
    room_one.add_item(item_two)
    return test_dungeon

def test_char_build():
    """builds a test character to be used for testing and development."""
    name = "Test Character"
    weapon_skill = cgen()
    ballistic_skill = cgen()
    strength = cgen()
    tough = cgen()
    agility = cgen()
    intelligence = cgen()
    perception = cgen()
    will_power = cgen()
    fellowship = cgen()
    homeworld = "Terra"
    motivation = "Money!!!"
    gender = "male"
    character_stats = [name, weapon_skill, ballistic_skill, strength, tough, agility\
        , intelligence, perception, will_power, fellowship, homeworld, motivation, \
        gender, 29]
    return char(character_stats)


test_character = test_char_build()
gsi.set_player_character(test_character)
