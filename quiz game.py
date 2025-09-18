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
    screen.draw.textbox("_____", text, color = "black")
    screen.draw.textbox("0", timer, color = "black")
    screen.draw.textbox("-", ans1, color = "black")
    screen.draw.textbox("-", ans2, color = "black")
    screen.draw.textbox("-", ans3, color = "black")
    screen.draw.textbox("-", ans4, color = "black")

def read_questions():
    file = open("questions.txt", "r")
    print(file.readlines())
    file.close()
    
def update():
    pass
read_questions()
pgzrun.go()