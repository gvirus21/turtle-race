from turtle import Turtle,Screen
import random

turtle_green=Turtle("turtle")
turtle_red=Turtle("turtle")
turtle_yellow=Turtle("turtle")
turtle_orange=Turtle("turtle")
turtle_purple=Turtle("turtle")

turtles=   {
        turtle_green:"green",
        turtle_red:"red",
        turtle_yellow:"yellow",
        turtle_orange:"orange",
        turtle_purple:"purple"
        }

is_race_on=False
screen=Screen()
screen.setup(width=400,height=500)

user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter your color :")
if user_bet:
        is_race_on=True

x=-180
y=100

for index in turtles:
        index.penup()
        index.color(turtles[index])
        index.goto(x,y)
        y-=50

while is_race_on :
        for turtle in turtles:
                rand_distance=random.randint(0,10)
                turtle.forward(rand_distance)
                if turtle.xcor() > 170:
                        is_race_on=False
                        winning_color=turtles[turtle]
                        if winning_color==user_bet:
                                print(f"You have won! winning color is {winning_color}")
                        else: print(f"You lost! winning color is {winning_color}")
                        
screen.exitonclick()