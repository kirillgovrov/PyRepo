# window(field)
from tkinter import *
HEIGHT = 500
WIDTH = 800
window = Tk()
window.title('Bubble bluster')
c = Canvas(window, width=WIDTH, height=HEIGHT, bg = 'darkblue')
c.pack


# The submarine
ship_id = c.create_polygon(5,5,5,25,30,15,fill='red')
ship_id2 = c.creat_oval(0,0,30,30,outline='red')
SHIP_R = 15
MID_X = WIDTH/2
MID_Y = HEIGHT/2
c.move(ship_id,MID_X,MID_Y)
c.move(ship_id2, MID_X, MID_Y)


# the submarine move
SHIP_SPD = 10
def move_ship(event):
    if event.keysym == 'Up':
        c.move(ship_id,0, -SHIP_SPD)
        c.move(ship_id2,0, -SHIP_SPD)
    elif event.keysym == 'Down':
        c.move(ship_id,0, SHIP_SPD)
        c.move(ship_id2,0, SHIP_SPD)
    elif event.keysym == 'Left':
     c.move(ship_id,0, SHIP_SPD)
     c.move(ship_id2,0, SHIP_SPD)