# Pokéapi Python API Code

This is a simple Pokémon-themed game in Python which uses the [Pokéapi](https://pokeapi.co/).

There will soon be two versions of this code. There is currently `game.py`, which is a text-based version of the game. Eventually there will be a GUI version with sprites and buttons using Tkinter; you can see the progress in `pokegui.py`.

The other file, `pokeapi.py`, contains all the classes/functions used to grab data from Pokéapi. Both versions of the game rely on this code.

## Gotta Cache 'Em All!

As the [Pokéapi documentation](https://pokeapi.co/docsv2/) says, please try to cache the resources and images if they are requested in the code. My code makes this very easy to do.

### How To Cache

If you do not have the proper file structure for the cache when running the game, Python will yell at you. So, in the same directory as `pokeapi.py`, you should have a `cache` folder with three sub-folders:

* `move`
* `pokemon`
* `sprites`
* `type`

If you have errors, make sure you've typed everything correctly.

