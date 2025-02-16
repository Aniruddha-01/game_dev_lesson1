import pgzrun
import random


WIDTH=800
HEIGHT=600
TITLE="Recycle game"
FONT_option = (9255,255,255)
CENTER_X = WIDTH/2
CENTER_Y = HEIGHT/2
CENTER=(CENTER_X,CENTER_Y)
FINAL_LEVEL = 6
START_SPEED = 10
ITEMS = ["bag","battery","bottle","chips"]

game_over = False
game_complete = True
current_level = 1
items = []
animations = []

def draw():
    global items,current_level,game_over,game_complete
    screen.clear()
    screen.blit("bground", (0,0))
    if game_over:
        display_message("GAME OVER","try again")
    elif game_complete:
        display_message("YOU WIN!","Well done")
    else:
        for item in ITEMS:
            item.draw()











def display_message(heading_text , sub_heading_text):
    screen.draw.text(heading_text , fontsize = 60 , center = CENTER, color="white")
    screen.draw.text(sub_heading_text, fontsize = 30, center = (CENTER_X, CENTER_Y+30), color="white")

pgzrun.go()