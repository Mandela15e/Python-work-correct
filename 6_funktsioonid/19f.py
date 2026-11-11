import tkinter as tk


def joonista_ring(canvas, x, y, raadius, varv):
    canvas.create_oval(x - raadius, y - raadius, x + raadius, y + raadius,
                       fill=varv, outline="black")


aken = tk.Tk()
aken.title("Värvilised ringid")
canvas = tk.Canvas(aken, width=600, height=300, bg="white")
canvas.pack()

varvid = ["red", "orange", "gold", "green", "cyan",
          "blue", "purple", "magenta", "brown", "gray"]

for i in range(10):
    joonista_ring(canvas, 40 + i * 55, 150, 15 + i * 2, varvid[i])

aken.mainloop()