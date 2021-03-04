import character
gen_npc = 20
non_player_characters = []
for entry in range(gen_npc):
    non_player_characters.append(character.generate_random_char())
for char in non_player_characters:
    char.character_sheet()