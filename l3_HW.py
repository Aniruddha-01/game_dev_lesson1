import pgzrun
from random import randint  
WIDTH = 500
HEIGHT = 500

def draw():
    width = 100
    height = 200
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    r2 = randint(0,255)
    g2 = randint(0,255)
    b2 = randint(0,255)
    my_rect1 = Rect((0,0) , (width,height))
    screen.draw.rect(my_rect1 , (r, g, b))

    my_rect2 = Rect((100,100) , (width,height))
    screen.draw.rect(my_rect2, (r2, g2, b2))
    

pgzrun.go()