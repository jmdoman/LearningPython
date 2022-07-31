import msvcrt as m
import random
import turtle as t
def wait():
    m.getch()
def  get_line_length():
    choice = input('Enter line length (long, medium or short): ')
    if choice == 'long':
        line_length = 250
    elif choice == 'medium':
        line_length = 200
    else:
        line_length = 100
    return line_length
def get_line_width():
    choice = input('Enter line width (superthick, thick or thin: ')
    if choice == 'superthick':
        line_width = 40
    elif choice == 'thick':
        line_width = 20
    else: 
        line_width = 10
    return line_width
def inside_window():   
    left_limit = (-t.window_width() / 2) + 100
    right_limit = (t.window_width() / 2) - 100
    top_limit = (t.window_height() / 2) - 100
    bottom_limit = (-t.window_height() / 2) + 300
    (x, y) = t.pos()
    inside = left_limit < x < right_limit and bottom_limit < y < top_limit
    print('inside: ' + str(inside))
    return inside
def move_turtle(line_length):
    print('turn = ' + str((maxtime - times) + 1))
    pen_colors = ['red', 'orange', 'yellow', 'blue', 'green', 'purple']
    this_color = random.choice(pen_colors)
    t.pencolor(this_color)
    print('color: ' + this_color)
    if inside_window():
        angle = random.randint(0, 180)
        t.right(angle)
        t.forward(line_length)
    else:
        t.backward(line_length)

line_length = get_line_length()
line_width = get_line_width()
timesAsked = input('how many times? enter number: ')
times = int(timesAsked)
t.shape('turtle')
t.fillcolor('green')
t.bgcolor('black')
t.speed('fastest')
t.pensize(line_width)

maxtime = times
while times > 0:
    move_turtle(line_length)
    times = times - 1

wait()
