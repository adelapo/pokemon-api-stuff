# PokeAPI GUI

from tkinter import *
from pokeapi import *

# GUI Prep

def custom_font(font_size):
    return ("Courier New", font_size, "bold")

root = Tk()

canvas = Canvas(root, width = 800, height = 500)
#bg_image = PhotoImage(file = "background.gif")
#canvas.create_image((0, 0), image=bg_image, anchor="nw")
canvas.pack()

message_box = Label(root, text="What will Ekans do?", font=custom_font(16), anchor="w", height=2, width=50, relief=SOLID, justify=LEFT, wraplength=400, borderwidth=3)
canvas.create_window((0, 400), window=message_box, width=400, height=100, anchor="nw")

action_box = Frame(root, borderwidth=3, relief=SOLID)
canvas.create_window((400, 400), window=action_box, width=400, height=100, anchor="nw")

button1 = Button(action_box, text="FIGHT", width=10, height=1, font=custom_font(16), padx=0, pady=0)
button1.grid(row=1, column=1)

button2 = Button(action_box, text="HELP", width=10, height=1, font=custom_font(16), padx=0, pady=0)
button2.grid(row=1, column=2)

button3 = Button(action_box, text="Pokemon", width=10, height=1, font=custom_font(16), padx=0, pady=0)
button3.grid(row=2, column=1)

button4 = Button(action_box, text="prdgu", width=10, height=1, font=custom_font(16), padx=0, pady=0)
button4.grid(row=2, column=2)

def show_message(msg):
    message_box.config(text=msg)

# Game Begins

bulbasaur = get_pokemon(1)
charmander = get_pokemon(4)
squirtle = get_pokemon(7)

# Starter Select

show_message("Welcome Trainer! Please select a starter Pokemon.")

starter1 = PhotoImage(file = get_sprite(1, "front"))
starter2 = PhotoImage(file = get_sprite(4, "front"))
starter3 = PhotoImage(file = get_sprite(7, "front"))

canvas.create_image((200, 250), image=starter1)
canvas.create_image((400, 250), image=starter2)
canvas.create_image((600, 250), image=starter3)



"""

player_id = 23
cpu_id = 623

player_pokemon = get_pokemon(player_id)
player_sprite = PhotoImage(file = get_sprite(23, "back"))  

# player_img = canvas.create_image((50, 150), image=player_sprite, anchor="nw")

cpu_pokemon = get_pokemon(cpu_id)
cpu_sprite = PhotoImage(file = get_sprite(cpu_id, "front"))

# cpu_img = canvas.create_image((500, 50), image=cpu_sprite, anchor="nw")

player_text = Label(root, text="You 100/100", font=custom_font(24), height=2, width=20, anchor="nw", relief=SOLID, borderwidth=3, justify=RIGHT)
canvas.create_window((775, 250), window=player_text, anchor="ne")

cpu_text = Label(root, text="CPU 100/100", font=custom_font(24), height=2, width=20, anchor="nw", relief=SOLID, borderwidth=3)
canvas.create_window((25, 50), window=cpu_text, anchor="nw")

"""

