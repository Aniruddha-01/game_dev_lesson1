import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500

score = 0
game_over = False


ash = Actor('ash2')
ash.pos = 100,100

pikachu = Actor('pikachu')
pikachu.pos = 200,200

def draw():
    pikachu.draw()
    ash.draw()
    screen.draw.text('Score:' + str(score) , color='black', topleft = (10,10))

    if game_over:
        screen.fill('red')
        screen.draw.text("Time's up! Your final score:" + str(score), midtop=(WIDTH/2,10), fontsize = 40, color = 'black')

def place_pikachu():
    pikachu.x = randint(70,(WIDTH-70))
    pikachu.y = randint(70,(HEIGHT-70))

def time_up():
    global game_over
    game_over = True

def update():
    global score
    if keyboard.left:
        ash.x = ash.x - 2
    if keyboard.right:
        ash.x = ash.x + 2
    if keyboard.up:
        ash.y = ash.y - 2
    if keyboard.down:
        ash.y = ash.y + 2
    pikachu_collected = ash.colliderect(pikachu)
    
    if pikachu_collected:
        score +=10
        place_pikachu()

clock.schedule(time_up, 60.0)


pgzrun.go()