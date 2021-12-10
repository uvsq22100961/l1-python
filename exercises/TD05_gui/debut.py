import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400


root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# Début de votre code
x0 = CANVAS_WIDTH / 2 - 50
x1 = CANVAS_WIDTH / 2 + 50
y = CANVAS_HEIGHT / 2
canvas.create_line(x0 + 50, y - 150, x0 + 50, y +150)
canvas.create_oval(x0, y - 200, x1, y - 100)
canvas.create_oval(x0, y - 50, x1, y + 50)
canvas.create_oval(x0, y + 100, x1, y + 200)
    
# Fin de votre code

canvas.grid()
root.mainloop()
