from room import Room
from game_state import game_state_instance as gsi
from class_exit import Exit
from dungeon import Dungeon
from command_factory import CommandFactory
from command import Command
from character import Character as char
from character import characteristic_gen as cgen


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