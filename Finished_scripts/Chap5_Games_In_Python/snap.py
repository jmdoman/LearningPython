import random
import time

from tkinter import Tk, Canvas, HIDDEN, NORMAL

def next_shape():
    global shape
    global previous_color
    global current_color
    previous_color = current_color #note current_color is currently set to the previous shapes's color! 
    c.delete(shape) #deletes the previous shape (which is now text)
    if len(shapes) > 0: #if there are any shapes left in shapes...
        shape = shapes.pop() #get the next shape in shapes
        c.itemconfigure(shape, state=NORMAL) #make the new shape visible
        current_color = c.itemcget(shape, 'fill') #assign current_color to the color of the current shape.
        root.after(1000, next_shape) #wait 1 second then show the next shape
    else: #if we're out of shapes...
        c.unbind('q')
        c.unbind('p') #game will no longer respond to p and q press
        #display the game result
        if p1_score > p2_score:
            c.create_text(200,200,text='Winner: Player 1')
        elif p2_score > p1_score:
            c.create_text(200,200,text='Winner: Player 2')
        else:
            c.create_text(200,200,text='Draw')
        c.pack()

def snap(event):
    global shape
    global p1_score
    global p2_score
    valid = False
    c.delete(shape) #deletes current shape
    # check if snap is valid
    if previous_color == current_color:
        valid = True
    if valid:
        if event.char == 'q':
            p1_score = p1_score + 1
        else:
            p2_score = p2_score + 1
        shape = c.create_text(200,200, text='SNAP! You score 1 point!')
    else:
        if event.char == 'q':
            p1_score = p1_score - 1
        else:
            p2_score = p2_score - 1
        shape = c.create_text(200,200, text='WRONG! You lose 1 point!')
    c.pack()
    root.update_idletasks() #this line forces the GUI to update immediately
    time.sleep(1) #wait 1 second to let player read message

root = Tk()
root.title('Snap')
c = Canvas(root, width=400,height=400)

# create shapes
shapes = []
circle = c.create_oval(35, 20, 365, 350, outline='black', fill='black', state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline='red', fill='red', state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline='green', fill='green', state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline='blue', fill='blue', state=HIDDEN)
shapes.append(circle)
rectangle = c.create_rectangle(35,100,365,270, outline='black', fill='black', state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35,100,365,270, outline='red', fill='red', state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35,100,365,270, outline='green', fill='green', state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35,100,365,270, outline='blue', fill='blue', state=HIDDEN)
shapes.append(rectangle)
square = c.create_rectangle(35,30,365,350, outline='black', fill='black', state=HIDDEN)
shapes.append(square)
square = c.create_rectangle(35,30,365,350, outline='red', fill='red', state=HIDDEN)
shapes.append(square)
square = c.create_rectangle(35,30,365,350, outline='green', fill='green', state=HIDDEN)
shapes.append(square)
square = c.create_rectangle(35,30,365,350, outline='blue', fill='blue', state=HIDDEN)
shapes.append(square)
c.pack()
random.shuffle(shapes)
# set starting variables
shape = None
previous_color = ''
current_color = ''
p1_score = 0
p2_score = 0
# set up UI
root.after(3000, next_shape) #3 second delay before first shape appears 
c.bind('q', snap)
c.bind('p', snap)
c.focus_set() #sends keystrokes to c
#start the game
root.mainloop()




