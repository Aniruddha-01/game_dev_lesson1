import pgzrun

TITLE = 'Quiz_Master'
WIDTH = 870
HEIGHT = 650

marquee_box = Rect(0,0 , 880,80)
answer_box_1 = Rect(0,0 , 300,150)
answer_box_2 = Rect(0,0 , 300,150)
answer_box_3 = Rect(0,0 , 300,150)
answer_box_4 = Rect(0,0 , 300,150)
question_box = Rect(0,0 , 750,70)
timer_box = Rect(0,0 , 70,70)
skip_box = Rect(0,0 , 70,300)

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
answer_box_1.move_ip(20,190)
answer_box_2.move_ip(350,190)
answer_box_3.move_ip(20,360)
answer_box_4.move_ip(350,360)
timer_box.move_ip(800,100)
skip_box.move_ip(800,200)

def draw():
    screen.clear()
    screen.fill(color = "black")
    screen.draw.filled_rect(marquee_box,"green")












pgzrun.go()