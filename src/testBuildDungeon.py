import Dungeon 
#import GameState
import Room
import Exit 


def testDungeonBuild():
    RoomInstance = Room.Room()
    DungeonInstance = Dungeon.Dungeon()
    ExitInstance = Exit.Exit()
    dungeonName = "Test Dungeon"
    roomOneExits = ()
    roomTwoExits = ()
    roomOne = RoomInstance.Room("Entry Room","The first room in the test dungeon",roomOneExits)
    roomTwo = RoomInstance.Room("second Room","The second room of the test dungeon",roomTwoExits)
    exit1 = ExitInstance.Exit("n",roomOne,roomTwo)
    exit2 = ExitInstance.Exit("s",roomTwo,roomOne)
    roomOne.addExit(exit1)
    roomTwo.addExit(exit2)
    return DungeonInstance.manDungeon(dungeonName,roomOne)
