import pgzrun

TITLE = 'Quiz_Master'
WIDTH = 870
HEIGHT = 650

marquee_box = Rect(0,0 , 870,80)
answer_box_1 = Rect(0,0 , 300,150)
answer_box_2 = Rect(0,0 , 300,150)
answer_box_3 = Rect(0,0 , 300,150)
answer_box_4 = Rect(0,0 , 300,150)
question_box = Rect(0,0 , 630,70)
timer_box = Rect(0,0 , 120,70)
skip_box = Rect(0,0 , 120,300)

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
answer_box_1.move_ip(20,190)
answer_box_2.move_ip(350,190)
answer_box_3.move_ip(20,360)
answer_box_4.move_ip(350,360)
timer_box.move_ip(700,100)
skip_box.move_ip(700,190)

def draw():
    screen.clear()
    screen.fill(color = "black")
    screen.draw.filled_rect(marquee_box,"green")
    screen.draw.filled_rect(question_box,"red")
    screen.draw.filled_rect(answer_box_1,"orange")
    screen.draw.filled_rect(answer_box_2,"orange")
    screen.draw.filled_rect(answer_box_3,"orange")
    screen.draw.filled_rect(answer_box_4,"orange")
    screen.draw.filled_rect(timer_box,"blue")
    screen.draw.filled_rect(skip_box,"blue")

    











pgzrun.go()