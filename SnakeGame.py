import turtle
import time
import random

delay = 0.1
body_segments = []
score = 0
high_score = 0

window = turtle.Screen()
window.title("Jueguito serpientita")
window.setup(width=600, height=600)
window.bgcolor("dark grey")

# lapitoncabezuda
head = turtle.Turtle()
head.speed(6)
head.shape("square")
head.penup()
head.color("dark green")
head.goto(0, 0)
head.direction = "stop"

# Sucomiditarica
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 80)
food.direction = "stop"

# 100puntosparagriffindor
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0, 250)
text.write(f'Score: 0      High Score: 0', align="center" , font=("Impact", 24))


def mov() :
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    
def dirUp():
    head.direction = "up"
def dirDown():
    head.direction = "down"
def dirRight():
    head.direction = "right"
def dirLeft():
    head.direction = "left"

window.listen()
window.onkeypress(dirUp, "w")
window.onkeypress(dirDown, "s")
window.onkeypress(dirLeft, "a")
window.onkeypress(dirRight, "d")


while True:
    window.update()

    # Chocaste pa
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in body_segments:
            segment.goto(1000, 1000)

        body_segments.clear()
        score = 0
        text.clear()
        text.write(f"Score: {score}      High Score: {high_score}", align="center" , font=("Impact", 24))

    #Lecrecelatula
    if head.distance(food) <= 20:
        x = random.randint(-275, 275)
        y = random.randint(-275, 275)
        food.goto(x, y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("light green")
        new_segment.penup()
        new_segment.goto(0, 0)
        body_segments.append(new_segment)
        score += 10

        if score > high_score:
            high_score = score

        text.clear()
        text.write(f'Score: {score}      High Score: {high_score}', align="center" , font=("Impact", 24))

    totalSeg = len(body_segments)

    for i in range(totalSeg - 1, 0, -1):
        x = body_segments[i-1].xcor()
        y = body_segments[i-1].ycor()
        body_segments[i].goto(x, y)

    if totalSeg > 0:
        x = head.xcor()
        y = head.ycor()
        body_segments[0].goto(x, y)

    mov()
    # te comiste la cola
    for segment in body_segments:
        if segment.distance(head) < 10:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in body_segments:
                segment.goto(1000, 1000)

            body_segments.clear()
            score = 0
            text.clear()
            text.write(f"Score: {score}      High Score: {high_score}", align="center" , font=("Impact", 24))

    time.sleep(delay)


turtle.done()
