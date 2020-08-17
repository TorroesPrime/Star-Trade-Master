from room import Room
from game_state import game_state_instance as gsi
from class_exit import Exit
from dungeon import Dungeon
from command_factory import CommandFactory
from command import Command
import adventure_loader

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

def prompt_user():
    command_prompt = input("> ")
    return command_prompt

def interpreter():
    adventure_loader.load_modules("adventures/")
    testDungeon = test_dungeon_build()
    gsi.initialize(testDungeon)
    print(f"\nWelcome to {gsi.dungeon.title}")
    print(gsi.adventurers_current_room.describe())
    command = input("> ")
    action = CommandFactory(command)
    while action.commandString != "q":
        action.execute_command()
        command = input("> ")
        action = CommandFactory(command)
    print("Logging off...")




interpreter()


