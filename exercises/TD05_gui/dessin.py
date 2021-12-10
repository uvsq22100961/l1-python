import tkinter as tk
from tkinter.constants import RAISED
import random

couleur1 = "blue"
CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500

def disque(couleur):
    """affiche un disque de diamètre 100 en bleu à un endroit choisi au hasard dans le canevas"""
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    canvas.create_oval((x, y), (x + 100, y + 100), fill = couleur)

def carre(couleur):
    """ affiche un carré rouge de côté 100"""
    x1 = random.randint(0, 400)
    y1 = random.randint(0, 400)
    canvas.create_rectangle((x1, y1), (x1 + 100, y1 + 100), fill = couleur)

def croix(couleur):
    """affiche une croix jaune inscrite dans un carré de côté 100"""
    x2 = random.randint(0, 400)
    y2 = random.randint(0, 400)
    canvas.create_line((x2, y2), (x2 + 100, y2 + 100), fill = couleur)
    canvas.create_line((x2 + 100, y2), (x2, y2 + 100), fill = couleur)

def couleur_objets():
    """Demande une couleur à l'utilisateur dans le terminal. Ensuite, les objets qui s'affichent doivent être de cette couleur, qui peut être modifiée par l'utilisateur autant de fois qu'il le souhaite. Tant que l'utilisateur n'a pas choisi de couleur, la couleur est bleue"""
    global couleur1
    couleur1 = input("Choisissez une couleur")

racine = tk.Tk()
racine.title("Mon dessin")
canvas = tk.Canvas(racine, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "black", borderwidth = 5, relief = RAISED)
bouton1 = tk.Button(racine, text = "Choisir une couleur", font = ("helvetica","10"), fg = "blue", command = couleur_objets)
bouton2 = tk.Button(racine, text = "Cercle", font = ("helvetica","10"), bg = "blue", command = lambda : disque(couleur1))
bouton3 = tk.Button(racine, text = "Carré", font = ("helvetica","10"), bg = "red", command = lambda : carre(couleur1))
bouton4 = tk.Button(racine, text = "Croix", font = ("helvetica","10"), bg = "yellow", command = lambda : croix(couleur1))

canvas.grid(column = 1, row = 1, rowspan = 3)
bouton1.grid(column = 1, row = 0, pady = 10)
bouton2.grid(column = 0, row = 1, padx = 10)
bouton3.grid(column = 0, row = 2)
bouton4.grid(column = 0, row = 3)

racine.mainloop()