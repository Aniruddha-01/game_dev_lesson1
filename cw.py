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
game_complete = False
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


def get_options_to_create(number_of_extra_items):
    items_to_create = ["paper"]
    for i in range (0,number_of_extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.appemd(random_option)
    return items_to_create


def create_items(items_to_create):
    new_items=[]
    for options in items_to_create:
        item = Actors(option + "img")
        new_items.append(item)
    return new_items


def layout_items(items_to_layout):
    number_of_gaps = len(items_to_layout) + 1
    gap_size = WIDTH/number_of_gaps
    random.shuffle(items_to_layout)
    for index, item in enumerate(items_to_layout):
        new_x_pos = (index+1)*gap_size
        item.x = new_x_pos

def animate_items(items_to_animate):
    global animations
    for item in items_to_animate:
        duration = START_SPEED - current_level
        item.anchor = ("center","bottom")
        animation = animate(item ,duration=duration ,on_finished = handle_game_over() y = HEIGHT)
        animations.append(animation)


def update():


def make_items(number_of_extra_items):



def handle_game_over():


def handle_game_complete():


def on_mouse_down():


def stop_animations():





def display_message(heading_text , sub_heading_text):
    screen.draw.text(heading_text , fontsize = 60 , center = CENTER, color="white")
    screen.draw.text(sub_heading_text, fontsize = 30, center = (CENTER_X, CENTER_Y+30), color="white")

pgzrun.go()