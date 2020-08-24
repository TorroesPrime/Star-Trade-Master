from room import Room
from game_state import game_state_instance as gsi
from class_exit import Exit
from dungeon import Dungeon
from command_factory import CommandFactory
from command import Command
import adventure_loader
from testBuildDungeon import test_dungeon_build as tester
from testBuildDungeon import test_char_build as char_test
import character as char

adventures_dir = "adventures/"


def prompt_user():
    command_prompt = input("> ")
    return command_prompt

def interpreter():

    #adventure = Dungeon.scanner(adventure_loader.select_modules(adventure_loader.load_modules(adventures_dir)))
    gsi.initialize(tester())
    test_char = char_test()
    gsi.add_character(test_char)
    gsi.player_character=test_char
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


