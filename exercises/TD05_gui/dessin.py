import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

racine = tk.Tk()
racine.title("Mon dessin")
canvas = tk.Canvas(racine, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "black")
bouton1 = tk.Button(racine, text = "Choisir une couleur", font = ("helvetica","15"))
bouton2 = tk.Button(racine, text = "Cercle", font = ("helvetica","15"))
bouton3 = tk.Button(racine, text = "Carré", font = ("helvetica","15"))
bouton4 = tk.Button(racine, text = "Croix", font = ("helvetica","15"))

canvas.grid(column = 1, row = 1)
bouton1.grid(column = 1, row = 0)
bouton2.grid(column = 0, row = 1)
bouton3.grid(column = 0, row = 2)
bouton3.grid(column = 0, row = 3)

racine.mainloop()