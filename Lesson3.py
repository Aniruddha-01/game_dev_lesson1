import pgzrun
from random import randint

TITLE = "Good Shot"
WIDTH = 500
HEIGHT = 500

message = ""

alien = Actor('alien')
alien.pos = 50,50

def draw():
    screen.clear()
    alien.draw()
    screen.draw.text(message , (10,10) , fontsize = 30)

def place_alien():
    alien.x = randint(50,WIDTH-50)
    alien.y = randint(50,HEIGHT-50)

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = "Good shot"
        place_alien()
    else : 
        message = "Missed it"

place_alien()



pgzrun.go()