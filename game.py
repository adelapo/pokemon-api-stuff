# PokeAPI Game

from tkinter import *
from urllib.request import Request, urlopen
import json
from pprint import pprint
from random import *
from math import ceil
import os.path

class Move:
    def __init__(self, name, move_type, power, accuracy, priority):
        self.name = name
        self.type = move_type
        self.power = power
        self.accuracy = accuracy
        self.priority = priority

class Pokemon:
    def __init__(self, name, types, stats, moves):
        self.name = name
        self.types = types
        self.stats = stats
        self.moves = moves          
        
        self.level = randint(1, 100)

        self.health = (2 * self.stats["hp"] + 100) * self.level / 100 + 10

    def attack(self, opponent, move) :
        print(self.name + " used " + move.name + " on " + opponent.name + "!")

        if move.power == None:
            damage = 0
        else:
            damage = (((((2 * self.level) / 5) + 2) * move.power * self.stats["attack"]) / (50 * opponent.stats["defense"]) + 2)
        if randint(1, 100) <= 5:
            damage = damage * 2
            print("Critical hit!")
        if False and self.type == move.type:
            damage = damage * 1.5
        damage = damage * randint(85, 100) / 100

        print(move.name + " did " + str(ceil(damage)) + " damage.")
        opponent.health = opponent.health - damage
        if opponent.health < 0:
            print(opponent.name + " fainted!")

BASE_URL = "http://pokeapi.co/api/v2/"

def is_cached(folder, name):
    file_name = "cache/" + folder + "/" + str(name) + ".txt"
    return os.path.isfile(file_name)

def cache_json(folder, name, string):
    file_name = "cache/" + folder + "/" + str(name) + ".txt"
    with open(file_name, "w") as file:
        file.write(string)

def get_data(resource, thing_id):
    if is_cached(resource, thing_id):
        # print("Getting resource " + resource + "/" + str(thing_id) + " from cache...")
        file_name = "cache/" + resource + "/" + str(thing_id) + ".txt"
        with open(file_name) as file:
            json_string = file.read()
    else:
        # print("Getting resource " + resource + "/" + str(thing_id) + " from API...")
        url = BASE_URL + resource + "/" + str(thing_id)
        req = Request(url, headers={"User-Agent" : "Chrome/60.0"})
        json_string = urlopen(req).read()
        json_string = json_string.decode("utf-8")
        cache_json(resource, thing_id, json_string)

    json_data = json.loads(json_string)

    return json_data
        
def get_pokemon(pokedex_id):
    pokemon_data = get_data("pokemon", pokedex_id)

    name = pokemon_data["name"].title()

    stats_dict = {}

    for stat in pokemon_data["stats"]:
        stat_name = stat["stat"]["name"]
        stat_number = stat["base_stat"]
        stats_dict[stat_name] = stat_number        

    moves = []

    # Get URLs of ALL its moves
    move_urls = [move["move"]["url"] for move in pokemon_data["moves"]]

    for move_url in move_urls:
        stl_slash = move_url[:-1].rfind("/")
        move_id = int(move_url[stl_slash+1:-1])
        move_data = get_data("move", move_id)

        new_move = Move(move_data["name"], move_data["type"], move_data["power"], move_data["accuracy"], move_data["priority"])
        moves.append(new_move)

    return Pokemon(name, "", stats_dict, moves)

def fight(player_pokemon, player_move, cpu_pokemon, cpu_move):
    if player_move.priority > cpu_move.priority:
        first = player_pokemon
        second = cpu_pokemon
        first_move = player_move
        second_move = cpu_move
    elif player_move.priority < cpu_move.priority:
        first = cpu_pokemon
        second = player_pokemon
        first_move = cpu_move
        second_move = player_move
    elif player_pokemon.stats["speed"] > cpu_pokemon.stats["speed"]:
        first = player_pokemon
        second = cpu_pokemon
        first_move = player_move
        second_move = cpu_move
    elif player_pokemon.stats["speed"] < cpu_pokemon.stats["speed"]:
        first = cpu_pokemon
        second = player_pokemon
        first_move = cpu_move
        second_move = player_move
    else:
        first = player_pokemon
        second = cpu_pokemon
        first_move = player_move
        second_move = cpu_move

    first.attack(second, first_move)
    if second.health > 0:
        second.attack(first, second_move)
    print("\n")


def encounter(player_pokemon, cpu_pokemon):
    print("\nA wild Lv. " + str(cpu_pokemon.level) + " " + cpu_pokemon.name + " appeared!")
    while player_pokemon.health > 0 and cpu_pokemon.health > 0:
        print("Your Lv. " + str(player_pokemon.level) + " " + player_pokemon.name + " has " + str(ceil(player_pokemon.health)) + " health.")
        print("Lv. " + str(cpu_pokemon.level) + " " + cpu_pokemon.name + " has " + str(ceil(cpu_pokemon.health)) + " health.")
        move_chosen = False
        while not move_chosen:
            attack_name = input("What will " + player_pokemon.name + " do?\n")
            for move in player_pokemon.moves:
                if move.name == attack_name:
                    player_move = move
                    move_chosen = True
        cpu_move = choice(cpu_pokemon.moves)
        fight(player_pokemon, player_move, cpu_pokemon, cpu_move)
        
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
    encounter(player_pokemon, get_pokemon(randint(1, 801)))
