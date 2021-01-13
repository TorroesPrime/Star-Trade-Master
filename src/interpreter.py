"""main input functions when run in a terminal. """
import json
from command_factory import CommandFactory
from game_state_instance import game_state_instance as gsi
from jsonproc import dungeon_map
#from test_build__dungeon import test_dungeon_build as tester
from test_build__dungeon import test_char_build as char_test




def prompt_user():
    '''provides the '>' character for the interpreter'''
    command_prompt = input("> ")
    return command_prompt

def interpreter():
    '''Primary interaction method. Initialized Game state, sets player character.'''
    gsi.initialize(dungeon_map)
    test_char = char_test()
    gsi.add_character(test_char)
    gsi.player_character = test_char
    print(f"\nWelcome to {gsi.dungeon.title}")
    print(gsi.adventurers_current_room.describe())
    command = prompt_user()
    action = CommandFactory(command)
    while action.command_string != "q":
        action.execute_command()
        command = prompt_user()
        action = CommandFactory(command)
    print("Logging off...")

interpreter()
