'''
This object-oriented revision of the Bubble Blaster program tries to keep
the general feel of the one in the book that uses global variables and
such. For a version that takes a more direct tk approach see
bubbles-revised-oop-tk.py
'''

import tkinter
import math
import time
import random

class CanvasObject():

    # mostly to document since always subclassed
    def __init__(self,canvas):
        self.canvas = canvas
        self.cid = None
        self.x = 0
        self.y = 0

    def update_coords(self):
        pos = self.canvas.coords(self.cid)
        self.x = (pos[0] + pos[2]) / 2
        self.y = (pos[1] + pos[3]) / 2

class Bubble(CanvasObject):
    min_radius = 10
    max_radius = 30
    max_speed = 10

    def __init__(self,canvas,x=0,y=0):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.radius = random.randint(self.min_radius, self.max_radius)
        r = self.radius
        self.cid = canvas.create_oval(x-r, y-r, x+r, y+r, outline='white')
        self.speed = random.randint(1,self.max_speed)

    def move(self,x,y):
        self.canvas.move(self.cid,x,y)
        self.update_coords()

    def remove(self):
        self.canvas.delete(self.cid)

class Ship(CanvasObject):
    def __init__(self,canvas):
        self.canvas = canvas
        self.radius = 15
        self.speed = 10
        self.poly = canvas.create_polygon(5,5,5,25,30,15,fill='red')
        self.oval = canvas.create_oval(0,0,30,30,outline='red')
        self.cid = self.oval
        canvas.bind_all('<Key>',self.handle_keyboard_move)

    def move(self,x,y):
        self.canvas.move(self.poly,x,y)
        self.canvas.move(self.oval,x,y)
        self.update_coords()

    def handle_keyboard_move(self,event):
        if event.keysym == 'Up':
            self.move(0,-self.speed)
        elif event.keysym == 'Down':
            self.move(0,self.speed)
        elif event.keysym == 'Left':
            self.move(-self.speed,0)
        elif event.keysym == 'Right':
            self.move(self.speed,0)

class Text(CanvasObject):
    def_color = 'white'
    def_text = ''
    def __init__(self,canvas,x=0,y=0,text=None,fill=None,font=None):
        if not fill: fill = self.def_color
        if not text: text = self.def_text
        self.canvas = canvas
        self.text = text
        self.fill = fill
        self.cid = canvas.create_text(x,y,text=text,fill=fill,font=font)

    def update(self,text):
        self.text = text
        self.canvas.itemconfig(self.cid,text=text)

class Game():
    def __init__(self):
        self.height = 500
        self.width = 800
        self.mid_x = self.width / 2
        self.mid_y = self.height / 2
        self.bonus_score = 1000
        self.bubble_chance = 10
        self.gap = 100
        self.time_limit = 30
        self.score = 0
        self.bonus = 0
        self.end = time.time() + self.time_limit
        self.window = tkinter.Tk()
        self.window.title('Bubble Blaster')
        self.canvas = tkinter.Canvas(self.window, \
                width=self.width, height=self.height, bg='darkblue')
        self.canvas.pack()
        self.ship = Ship(self.canvas)
        self.bubbles = list()
        self.ship.move(self.mid_x, self.mid_y)
        self.gui_time_title = Text(self.canvas,50,30,'TIME')
        self.gui_score_title = Text(self.canvas,150,30,'SCORE')
        self.gui_score = Text(self.canvas,150,50)
        self.gui_time = Text(self.canvas,50,50)

    def coords_of(cid):
        pos = c.coords(cid)
        x = (pos[0] + pos[2]) / 2
        y = (pos[1] + pos[3]) / 2
        return x, y

    def create_bubble(self):
        x = self.width + self.gap
        y = random.randint(0,self.height)
        self.bubbles.append(Bubble(self.canvas,x,y))

    def move_bubbles(self):
        for bubble in self.bubbles:
            bubble.move(-bubble.speed,0)

    def remove_bubble(self,bubble):
        self.bubbles.remove(bubble)
        bubble.remove()

    def clean_up_bubbles(self):
        for bubble in self.bubbles:
            if bubble.x < -self.gap:
                self.remove_bubble(bubble)

    def run(self):
        while time.time() < self.end:
            if random.randint(1, self.bubble_chance) == 1:
                self.create_bubble()
            self.move_bubbles()
            self.clean_up_bubbles()
            self.score += self.ship_bubble_collision()
            if (int(self.score / self.bonus_score)) > self.bonus:
                self.bonus += 1
                self.end += self.time_limit
            self.time_left = int(self.end - time.time())
            self.update_gui()
            self.window.update()
            time.sleep(0.01)
        Text(self.canvas,self.mid_x, self.mid_y,'GAME OVER',
                font=('Helvetica',30))
        Text(self.canvas,self.mid_x, self.mid_y + 30,
                'Score ' + str(self.score))
        Text(self.canvas,self.mid_x, self.mid_y + 45,'Bonus Time ' + 
                str(self.bonus * self.time_limit))
        input()

    def distance(self,x1,y1,x2,y2):
        return math.sqrt((x2-x1)**2+(y2-y1)**2)

    def ship_bubble_collision(self):
        points = 0
        for bubble in self.bubbles:
            distance = self.distance(self.ship.x,self.ship.y,\
                    bubble.x,bubble.y)
            boundary = self.ship.radius + bubble.radius
            if distance < boundary:
                points += bubble.radius + bubble.speed
                self.remove_bubble(bubble)
        return points

    def update_gui(self):
        self.gui_score.update(str(self.score))
        self.gui_time.update(str(self.time_left))

if __name__ == '__main__':
    Game().run()
