# Project overview
This project is an outgrowth of a Zork clone I helped build for class. Using a CLI system similar to Zork, this game will permit a player to take on the role of a "Star Trader", an intersteller free trader in the midst of the 30th mellenium, who is seeking their fortune and glory. 

### technologies used:
* Primary Programming language: Python 3.8

# Current status
**2020-8-29:**
I don't have a lot to talk about this week in regards to updates for the project, because I have started the new semester and I'm taking 17 credits this semester. So getting started in that has chewed into my free time quit a bit this week, limiting how much work I can do on the project. Another thing that is limiting how much I've been able to do on the project: reading up and studying about different storage approached. See, here is the thing. The more I've worked on planning out the system, and the more I've thought about what I ultimately want to be able to do in the system, the more I've been thinking about what the system needs to be able to do. And one of the thing is storing things like character data in a formate that can be readily accessed and recalled. 

As an example, let's say you start up a new adventure and you want to load up the character you played from another adventure but you also want to load a supporting characting. The information about all characters needs to be stored in a way that can be read and loaded. In order to cut down on over head, it's a good idea to limit what you need to load. Like say you have a record of 200 characters, 10 adventures, and 25 save games. Why build the system so that it loads all 200 characters, 10 adventure modules and the 25 saves just to select a character? 
So I've been reading up on pickle and json. At some point in the future I may switch to a database system... but for the moment something like json seems to be a good option.

So the only thing I've really been able to work on this week is part of the character system. Basically I want to have a "Character Generator" system. Partly for testing so I can work with loading, working with, storing and retriving characters, but with time I may expand it to enable a sort of "auto populate" kind of function. Just off the top of my head, one example of this could be say you're looking for a particular character in a room full of people. Rather then having to write up 30 or 40 characters in the adventure module, you could have a "population(40, mixed)" call in the adventure module and the game engine itself will generate 40 random characters and put them in the room.

And I make it sound like I've actually done so much of that. All I've managed to do so far is setup a system to import lists of names from an excel file.


**2020-8-23:**
working on the character class today. For the moment I'm using a 9 stat character class model based on the Warhammer 40,000 role play games. Very basic all told right now, but I've got the fundimental characteristics setup and I have a start on displaying the player characters' stats view a "view stats" command.
![character sheet](https://github.com/TorroesPrime/Star-Trade-Master/blob/master/files/screen-8-23-2020.png)


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
