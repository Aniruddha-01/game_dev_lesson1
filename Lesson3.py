import pgzrun
from random import randint

TITLE = "Good Shot"
WIDTH = 900
HEIGHT = 900

message = ""

ghost = Actor('ghost')
ghost.pos = 50,50

def draw():
    screen.clear()
    ghost.draw()
    screen.draw.text(message , (10,10) , fontsize = 30)

def place_ghost():
    ghost.x = randint(50,WIDTH-50)
    ghost.y = randint(50,HEIGHT-50)

def on_mouse_down(pos):
    global message
    if ghost.collidepoint(pos):
        message = "Good shot"
        place_ghost()
    else : 
        message = "Missed it"

place_ghost()



pgzrun.go()