import tkinter as tk

def bouge_boule():
    global l
    x1 = (canvas.coords(boule)[0]+canvas.coords(boule)[2])/2
    y1 = (canvas.coords(boule)[1]+canvas.coords(boule)[3])/2
    if x1 + 20 == 1150 or ((x1 + 21) in l) :
        x = -1
    else: x = 1
    if x1 - 20 == 478:
        return
    canvas.move(boule, x * 2, 0)
    l.append(x1 + 21)
    canvas.after(10, bouge_boule)

l=[]
HEIGHT = 700
WIDTH = 1200
racine = tk.Tk()
canvas = tk.Canvas(racine, bg= "gray70", height=HEIGHT, width= WIDTH)
canvas.grid()
canvas.create_rectangle((1150,0), (1200,700), fill="black")
canvas.create_rectangle((900,0), (1200,20), fill="black")
canvas.create_rectangle((900,680), (1200,700), fill="black")
boule = canvas.create_oval((480,330),(520,370), fill="turquoise1")
canvas.create_rectangle((464,310), (479,390), fill="black")
bouge_boule()
racine.mainloop()