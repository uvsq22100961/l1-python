import tkinter as tk
import random

def bouge_boule():
    global l
    global Y
    x1 = (canvas.coords(boule)[0]+canvas.coords(boule)[2])/2
    y1 = (canvas.coords(boule)[1]+canvas.coords(boule)[3])/2
    P1 = canvas.coords(rectangle1)[1]
    P2 = canvas.coords(rectangle1)[3]
    if x1 == 440:
        print("GAME OVER!")
        return
    if y1 + 20 >= 680 or y1 - 20 <= 20:
        Y = -Y
    if x1 - 20 == 478 and (((y1 - P1) >= 0 and (y1 - P1) <= 40) or ((P2 - y1) <= 40 and (P2 - y1) >= 0)):
        l = []
    if x1 + 20 == 1150 or ((x1 + 21) in l) :
        x = -1
    else: x = 1
    canvas.move(boule, x * 2, Y)
    l.append(x1 + 21)
    canvas.after(10, bouge_boule)

def rectangle(event):
    if event.char == "s":
        canvas.move(rectangle1, 0, 5)
    elif event.char == "z":
        canvas.move(rectangle1, 0, -5)

print("Appuyer sur 's' pour descendre et sur 'z' pour monter")
l = []
HEIGHT = 700
WIDTH = 1200
racine = tk.Tk()
canvas = tk.Canvas(racine, bg= "gray70", height=HEIGHT, width= WIDTH)
canvas.grid()
canvas.create_rectangle((1150,0), (1200,700), fill="black")
canvas.create_rectangle((0,0), (1200,20), fill="black")
canvas.create_rectangle((0,680), (1200,700), fill="black")
boule = canvas.create_oval((480,330),(520,370), fill="turquoise1")
rectangle1 = canvas.create_rectangle((464,310), (479,390), fill="black")
racine.bind("<KeyPress>", rectangle)
x2 = 315
y = random.randint(20, 680)
dy = y - 350
Y = dy / x2
bouge_boule()
racine.mainloop()