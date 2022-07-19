import turtle as t
from itertools import cycle

colors = cycle(['red','orange','yellow','green','blue','purple'])

def drawcircle(size, angle, shift):
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    drawcircle(size + 5, angle + 1, shift + 1)
    


t.bgcolor('black')
t.speed('fast')
t.pensize(4)

t.pencolor('red')
drawcircle(30, 0, 1)
