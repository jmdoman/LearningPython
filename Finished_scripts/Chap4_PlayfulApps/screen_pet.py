from tkinter import HIDDEN, NORMAL, Tk, Canvas

def toggle_eyes():
    current_color = c.itemcget(eye_l, 'fill')
    new_color = c.body_color if current_color == 'white' else 'white'
    current_state = c.itemcget(pupil_l, 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_l, state = new_state)
    c.itemconfigure(pupil_r, state = new_state)
    c.itemconfigure(eye_l, fill=new_color)
    c.itemconfigure(eye_r, fill=new_color)

def blink():
    toggle_eyes()
    root.after(250, toggle_eyes)
    root.after(3000, blink)

def show_happy(event):
    if (20 <= event.x <= 350) and (20 <= event.y <= 350):
        c.itemconfigure(cheek_l, state=NORMAL)
        c.itemconfigure(cheek_r, state=NORMAL)
        c.itemconfigure(mouth_happy, state=NORMAL)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad, state=HIDDEN)
    return

def hide_happy(event):
    c.itemconfigure(cheek_l, state=HIDDEN)
    c.itemconfigure(cheek_r, state=HIDDEN)
    c.itemconfigure(mouth_happy, state=HIDDEN)
    c.itemconfigure(mouth_normal, state=NORMAL)
    c.itemconfigure(mouth_sad, state=HIDDEN)

def toggle_tongue():
    if not c.tongue_out:
        c.itemconfigure(tongue_1, state=NORMAL)
        c.itemconfigure(tongue_2, state=NORMAL)
        c.tongue_out = True
    else:
        c.itemconfigure(tongue_1, state=HIDDEN)
        c.itemconfigure(tongue_2, state=HIDDEN)
        c.tongue_out = False

def toggle_pupils():
    if not c.eyes_crossed:
        c.move(pupil_l, 10, -5)
        c.move(pupil_r, -10, -5)
        c.eyes_crossed = True
    else:
        c.move(pupil_l, -10, 5)
        c.move(pupil_r, 10, 5)
        c.eyes_crossed = False

def cheeky(event):
    toggle_tongue()
    toggle_pupils()
    hide_happy(event)
    root.after(1000, toggle_tongue)
    root.after(1000, toggle_pupils)
    return

root = Tk()
c = Canvas(root, width=400, height=400)
c.configure(bg='dark blue', highlightthickness=0)
c.body_color = 'SkyBlue1'
body = c.create_oval(35, 20, 365, 350, outline=c.body_color, fill=c.body_color)
ear_l = c.create_polygon(75, 80, 75, 10, 165, 70, outline=c.body_color, fill=c.body_color)
ear_r = c.create_polygon(255, 45, 325, 10, 320, 70, outline=c.body_color, fill=c.body_color)
foot_l = c.create_oval(65, 320, 145, 360, outline=c.body_color, fill=c.body_color)
foot_r = c.create_oval(250, 320, 330, 360, outline=c.body_color, fill=c.body_color)
eye_l = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
eye_r = c.create_oval(230, 110, 260, 170, outline='black', fill='white')
pupil_l = c.create_oval(140, 145, 150, 155, outline='black', fill='black')
pupil_r = c.create_oval(240, 145, 250, 155, outline='black', fill='black')
mouth_normal = c.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL)
mouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN)
mouth_sad = c.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2, state=HIDDEN)
cheek_l = c.create_oval(70, 180, 120, 230, outline='pink', fill='pink', state=HIDDEN)
cheek_r = c.create_oval(280, 180, 330, 230, outline='pink', fill='pink', state=HIDDEN)
tongue_1 = c.create_rectangle(170, 250, 230, 290, outline='red', fill='red', state=HIDDEN)
tongue_2 = c.create_oval(170, 285, 230, 300, outline='red', fill='red', state=HIDDEN)
c.pack()
c.bind('<Motion>', show_happy)
c.bind('<Leave>', hide_happy)
c.bind('<Double-1>', cheeky)
c.eyes_crossed = False
c.tongue_out = False
root.after(5000, blink)


root.mainloop()
