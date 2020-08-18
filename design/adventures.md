## Adventures:
The system will support loading of "Adventure modules", which are single file archives that layout of a dungeon, and the contents of the dungeon including the rooms, exits, NPCs, items, exit statuses, and events that are actionable in that dungeon.

### Notes about adventure module format:
1. an adventure module file must have the .adv extension.
2. a .adv filt is a text file with the proper structure to be read by the program.

### example structure of a .adv file:
> items that are part of the file will be rendered **like this** while explinations of the part will be rendered *like this*.

**Adventure name** *title of the adventure*

**Description: a multiline description of the adventure.** *the description of the adventure*

**Version:RT001** *the supported version of the Star Trader engine this adventure requires.*

**===** *top level delemiter. Denotes a change in material type is coming up.*

**Items:** *item notation marker. Signifies that until another top level delimeter is encoutner, the system is reading materials for item type objects.*

**cake** *item name*

**2** *weight of the item*

**craftable:true** *craftable notation to signify if the item can be crafted by the player*

**recipe:flour-milk-eggs-vanilla** *the recipe of ingredients needed to craft this item*

**examine: it's a cake.** *verb action:response that this item can have performed on it.*

**kick: The cake explodes across your boot.** *verb action:response that this item can have performed on it.*

**eat[Wound(-2)]:Hmm that was a good cake** *verb action:response that this item can have performed on it. In this case, the action 'eat' will call the 'wound' event, and pass it a -2, effectivily healing the player for 2 hit points.*

**---** *second level delimeter. Signifies that this is the end of this item's entry.*

**dragonglass,glass** *name of the item. In this case, the item can be referred to by both "dragonglass" and "glass".*

**4** *weight of the dragonglass*

**break[Wound(1)]:Ouch!** *verb action:response that this item can have performed on it. In this case, the action 'break' will call the 'wound' event, and pass it a 1, wounding the player and subtracting 1 hit point from them.*

**wield:There is no one where to weild it against.** *verb action:response that this item can have performed on it.*

**---** *second level delimeter signifying that this is the end of the entry for this item.*

**Imperial Warrent of Trade** *name of the item*

**100** *weight of the item*

**examine:This warrent of trade is what gives your family the foundation for its power. By possessing this warrent you, as an authorized agent of your father's enterprises, are granted the authority to operate under your own discretion, in the name of the Empire beyond and with in it's borders. With out, you would be at best considered a rogue captain and at worst would be seen  as a pirate.** *verb action:response that this item can have performed on it.*

**read:[this would be the full text of the warrent of trade]**  *verb action:response that this item can have performed on it.*

**---** *second level delimeter signifying that this is the end of the entry for this item.*

**===** *top level delimeter signifying that we have reached the end of the current section and the next section will be a new type of object.*

**Non-player characters:** *NPC notation marker. Signifies that until another top level delimeter is encountered, the system is reading materials for Non-player character objects.*

**Old-man** *NPC Name*

**default:Yes, I am the old man. I've been around and seen a thing or two you young wipper snapper. I've been across the [crystal-mountains], and seen the[burning-sands]. Even made some good trade deals.** *the default, or initial response for the NPC.*

**crystal-mountains:Beutiful those mountains are. Legends say the Soul gem, the largest diamond ever seen by human eyes is hidden on those snow capped mountains. I went looking for it as a kid myself. Nearly died due to the cold. Also the Ursa Polars almost got me.** *a topic:response entry for the character*

**burning-sands:The burning sands... horrible horrible place. Blinding sun, burning heat, practically no water to speak of, massive hoards of Fire Scorpions, detestable vulture wasps... bagh. If it weren't for the chances of recovering treasures from lost convoys I would never have ventured into those cursed lands. Never!** *a topic:response entry for the character*

**soul-gem:The Soul Gem? Oh my word, the legends on that. A Crystal diamond the size of a Vorrik helm and crystal clear. Hmmm, if the legends are true, it's worth a score of King's Ransoms!** 

**fire-scorpions: Horrible devil spawn those things. Individually they are a dangerous annoyance, but you'll never encounter a single fire scorpion. They always congregate in hoards of hundreds. Their stingers can pierce thin armor and their venom make you feel like you're on fire and while you're screaming and flailing in response to feeling your skin burn off, the gods cursed critters are crawling all over you cutting into your body, taking out hunks! If we could eliminate all of those creepy bars it would be godly work to do so!** *a topic:response entry for the character*

**notknown:Huh? What? I don't know anything about that.** *a topic:response entry for the character. In this case, this is a "nonknown" entry. This is used for anytime the player askes the character about something the character doesn't know about.*

**---** *second level delimeter. Signifies that this is the end of this item's entry.*

**David** *NPC Name*

**default: greetings young traveler, I am David, I'm just an old Druid. Went out for a walk after breakfast and never came back. I've been out and about for most of my life. Been over the misty mountains a few times. Would love to get back to KalemZhad again. Such a trek would require crossing the ice creeks. That seems to be too dangerous a task for these days.** *the default, or initial response for the NPC.*

**druids:Druids are people of the Dwarf lands who do not live in caves but rather feel at home in the woods and grass lands.** *a topic:response entry for the character*

**ice-creeks: Far to the north are rivers that never run, solid as ice they are.** *a topic:response entry for the character*

**kalemzhad:Oh my word... KalenZhad is an impressive sight. Cave ceilings a thousand hefts tall with walls that runs for a hundred fields. Lights as bright as day. It's a fortress the likes of which are not known otherwise.** *a topic:response entry for the character*

**notknown:hmm.. yes... yes... that... is something I do not know.** *a topic:response entry for the character. In this case, this is a "nonknown" entry. This is used for anytime the player askes the character about something the character doesn't know about.*

**---** *second level delimeter signifying that this is the end of the entry for this item.*

**===** *top level delimeter signifying that we have reached the end of the current section and the next section will be a new type of object.*

**Rooms:** *Room notation marker. Signifies that until another top level delimeter is encountered, the system is reading materials for room objects.*

**Main bridge fore** *room name*

**The main bridge of the vessal** *Description of the room. Idealy should be a couple lines long.*

**NPCs:David,Old-man** *a list of the NPCs names contained in this room*

**Contents:dragonglass,Imperial Warrent of Trade** *list of items contained in this room*

**---** *second level delimeter signifying that this is the end of the entry for this item.*

**Main bridge aft** *room name*

**---** *second level delimeter signifying that this is the end of the entry for this item.*

**===** *top level delimeter signifying that we have reached the end of the current section and the next section will be a new type of object.*

**Exits:** *Exit notation marker. Signifies that until another top level delimeter is encountered, the system is reading materials for exit objects.*

**Main bridge for** *the source room for this exit.*

**s** *the direction of travel for this exit*

**Main bridge aft** *the destination room for this exit.*

**---** *second level delimeter signifying that this is the end of the entry for this item.*

**Main bridge aft** *the source room for this exit.*

**n** *the direction of travel for this exit*

**Main bridge fore** *the destination room for this exit.*

**---** *second level delimeter signifying that this is the end of the entry for this item.*

**===** *top level delimeter signifying that we have reached the end of the current section and the next section will be a new type of object.*

**EOF** *end of file delimeter, signifying the end of the module.*

