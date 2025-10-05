import pgzrun, random
WIDTH = 800
HEIGHT = 460
TITLE = "DA QUIZ"

title_box = Rect((0, 0), (800, 75))
text = Rect((20, 100), (600, 100))
timer = Rect((650, 100), (130, 100))
ans1 = Rect((20, 220), (300, 100))
ans2 = Rect((20, 340), (300, 100))
ans3 = Rect((340, 220), (300, 100))
ans4 = Rect((340, 340), (300, 100))
skip = Rect((670, 220), (100, 220))

answers = [ans1, ans2, ans3, ans4]
question = []
questions = []
total_questions = 0
question_number = 0
score = 0
countdown = 15
game_over = False

def draw():
    screen.fill("Black")
    screen.draw.filled_rect(title_box, "black")
    screen.draw.filled_rect(text, "blue")
    screen.draw.filled_rect(timer, "blue")
    screen.draw.filled_rect(ans1, "orange")
    screen.draw.filled_rect(ans2, "orange")
    screen.draw.filled_rect(ans3, "orange")
    screen.draw.filled_rect(ans4, "orange")
    screen.draw.filled_rect(skip, "green")
    screen.draw.textbox("Welcome to Da Quiz! Try your best to answer all questions accurately!", title_box, color =  "light blue")
    screen.draw.textbox("SKIP", skip, color =  "black")
    screen.draw.textbox(question[0], text, color = "black")
    screen.draw.textbox(str(countdown), timer, color = "black")
    screen.draw.textbox(question[1], ans1, color = "black")
    screen.draw.textbox(question[2], ans2, color = "black")
    screen.draw.textbox(question[3], ans3, color = "black")
    screen.draw.textbox(question[4], ans4, color = "black")

def end_game():
    global score, question, countdown
    question = ["Game Over! Score = " + str(score), "-", "-", "-", "-", 5]
    countdown = 0

def read_questions():
    global questions, total_questions
    file = open("questions.txt", "r")
    questions = file.readlines()
    total_questions = len(questions)
    file.close()

def next_question():
    global questions, question_number, question, countdown
    question_number = question_number + 1
    countdown = 15
    if question_number >= total_questions:
        end_game()
    else:
        question = questions[question_number].split(",")

def update_time():
    global countdown
    if countdown <= 0:
        end_game()
    else:
        countdown = countdown - 1

def on_mouse_down(pos):
    global countdown, question_number, score
    for option in answers:
        if option.collidepoint(pos):
            option_number = answers.index(option) + 1
            if option_number == int(question[5]):
                next_question()
                score = score + 1
            else:
                end_game()
        elif  skip.collidepoint(pos):
            next_question()
def update():
    pass
clock.schedule_interval(update_time, 1)
read_questions()
next_question()
pgzrun.go()