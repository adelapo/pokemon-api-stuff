# Text-Based Pokemon

from pokeapi import *

bulbasaur = get_pokemon(1)
charmander = get_pokemon(4)
squirtle = get_pokemon(7)

starters = [bulbasaur, charmander, squirtle]
print("Welcome Trainer! Choose your starter Pokemon!")
for i in range(len(starters)):
    print(str(i) + ": Lv. " + str(starters[i].level) + " " + starters[i].name)

starter_num = int(input("\nYour choice: "))

player_pokemon = starters[starter_num]
print("Good choice. Here are all of " + player_pokemon.name + "'s moves:")
for move in player_pokemon.moves:
    print(move.name)

while player_pokemon.health > 0:
    encounter(player_pokemon, get_pokemon(randint(1, 802)))
