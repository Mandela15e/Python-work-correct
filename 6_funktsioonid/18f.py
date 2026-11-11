import tkinter as tk


def joonista_ruut(canvas, x, y, suurus, varv):
    canvas.create_rectangle(x, y, x + suurus, y + suurus, fill=varv, outline="black")


aken = tk.Tk()
aken.title("Värvilised ruudud")
canvas = tk.Canvas(aken, width=500, height=300, bg="white")
canvas.pack()

joonista_ruut(canvas, 20, 20, 60, "red")
joonista_ruut(canvas, 110, 40, 90, "orange")
joonista_ruut(canvas, 230, 20, 40, "green")
joonista_ruut(canvas, 300, 80, 120, "blue")
joonista_ruut(canvas, 60, 150, 100, "purple")
joonista_ruut(canvas, 200, 200, 50, "gold")

aken.mainloop()