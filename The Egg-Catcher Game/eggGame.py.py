#upload packages
from itertools import cycle
from random import randrange
from tkinter import Canvas, Tk, messagebox, font

#import modules for the backgroud music
from pygame.locals import*
from pygame import mixer

import winsound #import module for button click and end of the game sound

#Import modules for backgroud image
from tkinter import*
from PIL import ImageTk,Image

#Adding the background sound
mixer.init()
mixer.music.load("Power - AShamaluevBackground.mp3")
mixer.music.play()

#Set up a screen size
screen_width = 800
screen_height = 400

#creating a screen
root = Tk()
root.title("Egg Catcher")
screen = Canvas(root, width=screen_width, height=screen_height)
image=ImageTk.PhotoImage(Image.open("BgFarm.jpg"))

screen.create_image(0,0,anchor=NW,image=image)
screen.pack()

#Create eggs
color_cycle = cycle(["brown", "blue","pink", "orange","lime"])
egg_width = 45
egg_height = 55
egg_score = 10
egg_speed = 500
egg_interval = 4000
difficulty = 0.95

#create an egg catcher
catcher_color = "red"
catcher_width = 100
catcher_height = 100
catcher_startx = screen_width / 2 - catcher_width / 2
catcher_starty = screen_height - catcher_height - 20
catcher_startx2 = catcher_startx + catcher_width
catcher_starty2 = catcher_starty + catcher_height

catcher = screen.create_arc(catcher_startx, catcher_starty, catcher_startx2, catcher_starty2, start=200, extent=140, style="arc", outline=catcher_color, width=3)
game_font = font.nametofont("TkFixedFont")
game_font.config(size=18)

#Create scores
score = 0
score_text = screen.create_text(650, 35, anchor="nw", font=game_font, fill="gold", text="Score: "+ str(score))

#remaining lives
lives_remaining = 3
lives_text = screen.create_text(screen_width-38, 10, anchor="ne", font=game_font, fill="red", text="Lives: "+ str(lives_remaining))

eggs = []

def create_egg():
    x = randrange(10, 740)
    y = 40
    new_egg = screen.create_oval(x, y, x+egg_width, y+egg_height, fill=next(color_cycle), width=0)
    eggs.append(new_egg)
    root.after(egg_interval, create_egg)

def move_eggs():
    for egg in eggs:
        (eggx, eggy, eggx2, eggy2) = screen.coords(egg)
        screen.move(egg, 0, 10)
        if eggy2 > screen_height:
            egg_dropped(egg)
    root.after(egg_speed, move_eggs)

def egg_dropped(egg):
    eggs.remove(egg)
    screen.delete(egg)
    lose_a_life()
    if lives_remaining == 0:
        mixer.music.stop()
        winsound.PlaySound("Sound for game over.wav", winsound.SND_FILENAME) #play sound for the end of the game
        messagebox.showinfo("The End :(", "Total Obtained : "+ str(score))
        root.destroy()

def lose_a_life():
    global lives_remaining
    lives_remaining -= 1
    screen.itemconfigure(lives_text, text="Lives: "+ str(lives_remaining))

def check_catch():
    (catcherx, catchery, catcherx2, catchery2) = screen.coords(catcher)
    for egg in eggs:
        (eggx, eggy, eggx2, eggy2) = screen.coords(egg)
        if catcherx < eggx and eggx2 < catcherx2 and catchery2 - eggy2 < 40:
            eggs.remove(egg)
            screen.delete(egg)
            increase_score(egg_score)
    root.after(100, check_catch)

def increase_score(points):
    global score, egg_speed, egg_interval
    score += points
    egg_speed = int(egg_speed * difficulty)
    egg_interval = int(egg_interval * difficulty)
    screen.itemconfigure(score_text, text="Score: "+ str(score))

def go_left(event):
    (x1, y1, x2, y2) = screen.coords(catcher)
    if x1 > 0:
        screen.move(catcher, -20, 0)

def go_right(event):
    (x1, y1, x2, y2) = screen.coords(catcher)
    if x2 < screen_width:
        screen.move(catcher, 20, 0)

#Keyboard keys for moving the catcher
screen.bind("<Left>", go_left)
screen.bind("<Right>", go_right)
screen.focus_set()
root.after(1000, create_egg)
root.after(1000, move_eggs)
root.after(1000, check_catch)
root.mainloop()
