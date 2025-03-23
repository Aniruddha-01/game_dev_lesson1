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
skip_box = Rect(0,0 , 120,320)

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
answer_box_1.move_ip(20,190)
answer_box_2.move_ip(350,190)
answer_box_3.move_ip(20,360)
answer_box_4.move_ip(350,360)
timer_box.move_ip(700,100)
skip_box.move_ip(700,190)


score = 0
time_left = 10
question_file_name = "questions.txt"
questions = []
question_count = 0
question_index = 1

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
    screen.draw.textbox("Skip",skip_box,color="black",angle=-90)
    marquee_text = "Welcome to QuizMaster..."
    marquee_text = marquee_text + f"Q:{question_index} of {question_count}"
    screen.draw.textbox(marquee_text,marquee_box,color="black")

def update():
    move_marquee()

def move_marquee():
    marquee_box.x=marquee_box.x-2
    if marquee_box.right<0:
        marquee_box.left=WIDTH


def read_q_file():
    global question_count,questions
    q_file = open(question_file_name, "r")
    for question in q_file:
        questions.append(question)
        question_count = question_count+1
    q_file.close()
   












read_q_file()
pgzrun.go()