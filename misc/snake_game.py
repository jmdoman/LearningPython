# https://geekflare.com/snake-game-in-python/

import turtle
import random
import time

# Assigning directions
def moveleft():
    if snake.direction != "right":
        snake.direction = "left"

def moveright():
    if snake.direction != "left":
        snake.direction = "right"

def moveup():
    if snake.direction != "down":
        snake.direction = "up"

def movedown():
    if snake.direction != "up":
        snake.direction = "down"

def move():
    if snake.direction == "up":
        coord_y = snake.ycor()
        snake.sety(coord_y+20)

    if snake.direction == "down":
        coord_y = snake.ycor()
        snake.sety(coord_y-20)

    if snake.direction == "right":
        coord_x = snake.xcor()
        snake.setx(coord_x+20)

    if snake.direction == "left":
        coord_x = snake.xcor()
        snake.setx(coord_x-20)



player_score = 0
highest_score = 0
delay_time = 0.1

# window screen created
wind = turtle.Screen()
wind.title("Snake Maze🐍")
wind.bgcolor("red")

#screen size
wind.setup(width=600, height=600)

#creating the snake
snake = turtle.Turtle()
snake.shape("square")
snake.color("black")
snake.penup()
snake.goto(0, 0)
snake.direction = "Stop"

# creating the food
snake_food = turtle.Turtle()
shapes = ['triangle', 'circle']
this_shape = random.choice(shapes)
snake_food.shape(this_shape)
snake_food.color("blue")
snake_food.speed(0)
snake_food.penup()
snake_food.goto(0, 100)

#writing the score
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Your_score: 0 Highest_Score : 0", align="center",font=("Arial", 24, "normal"))

wind.listen()
wind.onkeypress(moveleft, 'L')
wind.onkeypress(moveright, 'R')
wind.onkeypress(moveup, 'U')
wind.onkeypress(movedown, 'D')



turtle.mainloop()
