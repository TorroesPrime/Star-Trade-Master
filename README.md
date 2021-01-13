# Project overview
This project is an outgrowth of a Zork clone I helped build for class. Using a CLI system similar to Zork, this game will permit a player to take on the role of a "Star Trader", an intersteller free trader in the midst of the 30th mellenium, who is seeking their fortune and glory. 

### technologies used:
* Primary Programming language: Python 3.8

# Current status
**2021-1-08:**
Hey, believe it or not, I haven’t abandoned this project! I know it’s been a few months since I was able to update. This last semester of class was particularly demanding and really left me in a bad place when it came to creative energy and motivation. There were days where I looked at my collection of Role play game rule books and felt pangs of guilt for not working on this project, only to be reminded I still had assignments for class I hadn’t finished. Oh and Covid has been a thing. But I’ve been on winter break between semesters, and that means I’ve been able to get some more work in on it. There are three things I’ve worked on most recently.
The first thing is the <help> command. 
![commands](https://raw.githubusercontent.com/TorroesPrime/Star-Trade-Master/master/files/screensnip-01-08-2021.png)
 
You can see from the display snippet above that the `help` command shows information for the move, save, take, look, and inventory commands. These are the basic commands I intend to get working for version .01 of the system. 

Future plans for the `help` command include allowing the player to use the `help` command in conjunction with a specific command. So you could do `help take` and get a more detailed explanation of the `take` and `take all` commands.

The second thing I’ve been working on is the `inventory` command. It’s not finished yet, but it matches the example output of the help command which means it’s functional.

Finally I’ve gotten the `take` command working. As of right now you can only take single items, but the next thing is getting the `take all` command to work. 

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
