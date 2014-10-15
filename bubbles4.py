# despite what the book says it's actually bad practice to use either:
#from tkinter import *
#from tkinter import Tk

import tkinter

HEIGHT = 500
WIDTH = 800
window =  tkinter.Tk()
window.title('Bubble Blaster')
c = tkinter.Canvas(window, width=WIDTH, height=HEIGHT, bg='darkblue')
c.pack()

ship_id = c.create_polygon(5,5,5,25,30,15,fill='red')
ship_id2 = c.create_oval(0,0,30,30,outline='red')
SHIP_RADIUS = 15
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2
c.move(ship_id,MID_X,MID_Y)
c.move(ship_id2,MID_X,MID_Y)

# don't abbreviate, it's bad style and not 'pythonic'
SHIP_SPEED = 10
def move_ship(event):
    if event.keysym == 'Up':
        c.move(ship_id,0,-SHIP_SPEED)
        c.move(ship_id2,0,-SHIP_SPD)
    elif event.keysym == 'Down':
        c.move(ship_id,0,SHIP_SPD)
        c.move(ship_id2,0,SHIP_SPD)
    elif event.keysym == 'Left':
        c.move(ship_id,-SHIP_SPD,0)
        c.move(ship_id2,-SHIP_SPD,0)
    elif event.keysym == 'Right':
        c.move(ship_id,SHIP_SPD,0)
        c.move(ship_id2,SHIP_SPD,0)
c.bind_all('<Key>',move_ship)

import random

bubble_id = list()
bubble_radius = list()
bubble_speed = list()
MIN_BUBBLE_RADIUS = 10
MAX_BUBBLE_RADIUS = 30
MAX_BUBBLE_SPEED = 10
GAP = 100

def create_bubble():
    x = WIDTH + GAP
    y = random.randint(0, HEIGHT)
    r = random.randint(MIN_BUBBLE_RADIUS, MAX_BUBBLE_RADIUS)
    id1 = c.create.oval(x-r, y-r, x+r, y+r, outline='white')
    bubble_id.append(id1)
    bubble_radius.append(r)
    bubble_speed.append(random.randint(1,MAX_BUBBLE_SPEED))

# easy way to keep the window open
input()
