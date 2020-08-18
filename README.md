# Project overview
This project is an outgrowth of a Zork clone I helped build for class. Using a CLI system similar to Zork, this game will permit a player to take on the role of a "Star Trader", an intersteller free trader in the midst of the 30th mellenium, who is seeking their fortune and glory. 

### technologies used:
* Primary Programming language: Python 3.8

# Current status
**2020-8-17:**
Working on the module loading system. The intention is when you start a new game, the program will automatically present you a list of availible (and valid) adventure modules and the player only needs to select which one they wish to play.

Got the system working to a point that it will build a list of availible adventure modules and display the name and description of those adventures. Next step: 
passing the name of the selected adventure module to the load function of dungeon.

**2020-8-13:**
Fundimental interface system is functional. If you download the file, run interpeter.py. This fill will create a very simple 2 room dungeon. The interface will accept any string command while 'N' 'S' 'E' 'W' 'U' 'D' will create a movement command and 'SAVE' will create a save command. None of these commands actually do anything at this time.

**Prelimary write up**
At this point the project is in conceptualization. While I have ideas in my head of what I want, I need to get those ideas written down so I can work with them and start actually designing the engine and systems to power this game.


# Quick information Access 
1-[General Description](https://github.com/TorroesPrime/Star-Trade-Master/blob/master/design/generalDescription.md)

A general overview of what the game is intended to be and future plans for it.

2- [Command Line Interface](https://github.com/TorroesPrime/Star-Trade-Master/blob/master/design/interfaceDescription.md)

A combination of notes and design throughts about how the interface will look, be laid out, and function.

3- [Character class](https://github.com/TorroesPrime/Star-Trade-Master/blob/master/design/characterDescription.md)

Information about the character, and the class derived from it.

4- [Mission Notes](https://github.com/TorroesPrime/Star-Trade-Master/blob/master/design/missionsDescription.md)

Notes about the different types of missions that the player can under take in the game.

5- [Screens](https://github.com/TorroesPrime/Star-Trade-Master/blob/master/design/screenDescription.md)

Information and notes regarding the screens.

6- [Actions](https://github.com/TorroesPrime/Star-Trade-Master/blob/master/design/actions.md)

Information and notes about actions a character can perform.

7- [Adventure Modules](https://github.com/TorroesPrime/Star-Trade-Master/blob/master/design/adventures.md)

Information and note about adventure module files.