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

# easy way to keep the window open
input()
