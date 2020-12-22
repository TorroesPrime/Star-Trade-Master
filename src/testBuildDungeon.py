from room import Room
from game_state_instance import game_state_instance as gsi
from class_exit import Exit
from dungeon import Dungeon
from command_factory import CommandFactory
from command import Command
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
    dungeonName = "Test Dungeon"
    roomOne = Room("Entry Room","The first room in the test dungeon")
    roomTwo = Room("second Room","The second room of the test dungeon")
    exit1 = Exit("n",roomOne,roomTwo)
    exit2 = Exit("s",roomTwo,roomOne)
    roomOne.add_exit(exit1)
    roomTwo.add_exit(exit2)
    testDungeon = Dungeon(dungeonName,roomOne)
    testDungeon.add_room(roomTwo)
    item_one_stats = ["Apple", "A red Fuji Apple", .2]
    ItemOneActions = {"eat": "consume-You eat the apple", "examine": "It's a red apple. It looks really tasty.", "throw": "destroy-You hurl the apple agaisnt the wall. It smashes agaisnt it with a splat."}
    itemOne = item(item_one_stats,ItemOneActions)
    roomOne.add_item(itemOne)
    return testDungeon

def test_char_build():
    name = "Test Character"
    ws = cgen()
    bs = cgen()
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
    character_stats = [name,ws,bs,strength,tough,agility,intelligence,perception,will_power,fellowship,homeworld,motivation,gender,29]
    return char(character_stats)


test_character = test_char_build()
gsi.set_player_character(test_character)