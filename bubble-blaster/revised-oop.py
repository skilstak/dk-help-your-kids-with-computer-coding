'''
This object-oriented revision of the Bubble Blaster program tries to keep
the general feel of the one in the book but taking a traditional
object-oriented approach.
'''

import tkinter
import math
import time
import random

class CanvasObject(object):
    '''
    A generic parent class for all objects created for the tk canvas,
    which often include several tk canvas shape, polygon, and text
    objects combined into a single logic object with one root object. This
    approach allows complex collections of sprite images and more to be
    treated as one object in terms of movement and collision detection.
    '''

    def __init__(self,canvas):
        self.canvas = canvas
        self.root = None
        self.x = 0
        self.y = 0

    def update_coords(self):
        '''Usually just call this from move()'''
        pos = self.canvas.coords(self.root)
        self.x = (pos[0] + pos[2]) / 2
        self.y = (pos[1] + pos[3]) / 2

    def move(self,x,y):
        '''Override to move all the components of the CanvasObject'''
        self.canvas.move(self.root,x,y)
        self.update_coords()

    def step(self):
        '''Override to give CanvasObject behavior for each step'''
        pass

    def destroy(self):
        '''Override to remove and cleanup all the canvas items for self'''
        pass

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
        self.root = canvas.create_oval(x-r, y-r, x+r, y+r, outline='white')
        self.speed = random.randint(1,self.max_speed)

    def destroy(self):
        self.canvas.delete(self.root)

class Ship(CanvasObject):
    def __init__(self,canvas):
        self.canvas = canvas
        self.radius = 15
        self.speed = 10
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        self.poly = canvas.create_polygon(5,5,5,25,30,15,fill='red')
        self.oval = canvas.create_oval(0,0,30,30,outline='red')
        self.root = self.oval
        canvas.bind_all('<KeyPress>',self._handle_keypress)
        canvas.bind_all('<KeyRelease>',self._handle_keyrelease)

    def move(self,x,y):
        self.canvas.move(self.poly,x,y)
        self.canvas.move(self.oval,x,y)
        self.update_coords()

    def step(self):
        if self.moving_up:
            self.move(0,-self.speed)
        if self.moving_down:
            self.move(0,self.speed)
        if self.moving_left:
            self.move(-self.speed,0)
        if self.moving_right:
            self.move(self.speed,0)

    def _update_moving(self,event,state):
        if event.keysym == 'Up':
            self.moving_up = state
        elif event.keysym == 'Down':
            self.moving_down = state
        elif event.keysym == 'Left':
            self.moving_left = state
        elif event.keysym == 'Right':
            self.moving_right = state

    def _handle_keypress(self,event):
        self._update_moving(event,True)

    def _handle_keyrelease(self,event):
        self._update_moving(event,False)

class Text(CanvasObject):
    def_color = 'white'
    def_text = ''
    def __init__(self,canvas,x=0,y=0,text=None,fill=None,font=None):
        if not fill: fill = self.def_color
        if not text: text = self.def_text
        self.canvas = canvas
        self.text = text
        self.fill = fill
        self.root = canvas.create_text(x,y,text=text,fill=fill,font=font)

    def update(self,text):
        self.text = text
        self.canvas.itemconfig(self.root,text=text)

class Game():
    height = 500
    width = 800
    mid_x = width / 2
    mid_y = height / 2
    bonus_score = 1000
    bubble_chance = 10
    gap = 100
    time_limit = 30
    speed = 0.01

    def __init__(self):
        self.score = 0
        self.bonus = 0
        self.window = tkinter.Tk()
        self.window.title('Bubble Blaster')
        self.canvas = tkinter.Canvas(self.window, width=self.width,
                height=self.height, bg='darkblue')
        self.end = time.time() + self.time_limit
        Text(self.canvas,50,30,'TIME')
        Text(self.canvas,150,30,'SCORE')
        self.gui_score = Text(self.canvas,150,50)
        self.gui_time = Text(self.canvas,50,50)
        self.canvas.pack()
        self.bubbles = list()
        self.ship = Ship(self.canvas)
        self.ship.move(self.mid_x, self.mid_y)

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

    def destroy_bubble(self,bubble):
        self.bubbles.remove(bubble)
        bubble.destroy()

    def clean_up_bubbles(self):
        for bubble in self.bubbles:
            if bubble.x < -self.gap:
                self.destroy_bubble(bubble)

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
            self.ship.step()
            time.sleep(self.speed)
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
                self.destroy_bubble(bubble)
        return points

    def update_gui(self):
        self.gui_score.update(str(self.score))
        self.gui_time.update(str(self.time_left))

if __name__ == '__main__':
    Game().run()
