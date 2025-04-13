import pgzrun
import time
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
question_file_name = r"D:\OneDrive\Desktop\Python_gamedev\Quiz_master\questions.txt"
questions = []
question_count = 0
question_index = 0
answer_boxes = [answer_box_1,answer_box_2,answer_box_3,answer_box_4]


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
    screen.draw.textbox(question[0].strip(),question_box,color="black" , angle = 0)
    index = 1
    for answer_box in answer_boxes:
        screen.draw.textbox(question[index].strip(),answer_box,color="blue")
        index +=1
    screen.draw.textbox(str(time_left),timer_box,color="black")
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
   


def read_next_question():
    global question_index
    question_index +=1
    return questions.pop(0).split(",")
 
def game_over():
    global question,time_left,score 
    message = f"Game Over! \n You got {score} questions correct"
    question=[message, "-","-","-","-",5]
    time_left=0

def correct_ans():
    global score,question,questions,time_left
    if questions:
        question=read_next_question()
        score += 1 
        time_left = 10
    else:
        game_over()
   

def timer():
    global time_left
    if time_left:
        time_left -=1 
    else:
        game_over()


def skip_question():
    global questions,question,time_left
    if questions:
        question = read_next_question()
        time_left = 10
    else:
        game_over()




def on_mouse_down(pos):
    index=1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index is int(question[5]):
                correct_ans()
            else:
                game_over()
        index +=1
    if skip_box.collidepoint(pos):
        skip_question()
        








read_q_file()
question=read_next_question()
clock.schedule_interval(timer,1)
pgzrun.go()