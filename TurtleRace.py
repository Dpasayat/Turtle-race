from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color from rainbow:")

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_position = [-70, -40, -10, 20, 50, 80, 110]

all_turtles = []
for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

message = ''

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            referee = Turtle(shape="turtle")
            referee.penup()
            referee.hideturtle()
            if winning_color == user_bet:
                message = f"{winning_color} turtle is the winner!! You won"
                referee.color("green")
            else:
                message = f"{winning_color} turtle is the winner!! You lost"
                referee.color("red")

            referee.write(message, align="center", font=("Courier", 11, "normal"))
            is_race_on = False
            break
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
