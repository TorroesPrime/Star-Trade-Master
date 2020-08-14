from room import Room
#from room import manuel_room
import game_state
from class_exit import Exit
from dungeon import Dungeon
from command_factory import CommandFactory
#import command_factory
from command import Command

def test_dungeon_build():
    dungeonName = "Test Dungeon"
    roomOneExits = ()
    roomTwoExits = ()
    roomOne = Room("Entry Room","The first room in the test dungeon",roomOneExits)
    roomTwo = Room("second Room","The second room of the test dungeon",roomTwoExits)
    exit1 = Exit("n",roomOne,roomTwo)
    exit2 = Exit("s",roomTwo,roomOne)
    roomOne.add_exit(exit1)
    roomTwo.add_exit(exit2)
    testDungeon = Dungeon(dungeonName,roomOne)
    testDungeon.add_room(roomTwo)

    return testDungeon

def prompt_user():
    command_prompt = input("> ")
    return command_prompt

def interpreter():
    testDungeon = test_dungeon_build()
    print(f"\nWelcome to {testDungeon.title}")
    command = input("> ")
    action = CommandFactory(command)
    while action.commandString != "q":
        action.execute_command()
        command = input("> ")
        action = CommandFactory(command)
    print("Logging off...")




interpreter()


