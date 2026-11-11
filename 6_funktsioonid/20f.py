import tkinter as tk


def joonista_sein(canvas, x, y, laius, korgus, varv):
    canvas.create_rectangle(x, y, x + laius, y + korgus, fill=varv, outline="black")


def joonista_katus(canvas, x, y, laius, korgus, varv):
    canvas.create_polygon(x, y, x + laius, y, x + laius / 2, y - korgus,
                          fill=varv, outline="black")


def joonista_aken(canvas, x, y, suurus):
    canvas.create_rectangle(x, y, x + suurus, y + suurus,
                            fill="lightblue", outline="black")
    canvas.create_line(x + suurus / 2, y, x + suurus / 2, y + suurus)
    canvas.create_line(x, y + suurus / 2, x + suurus, y + suurus / 2)


def joonista_maja(canvas, x, y, laius, korgus, seinavarv, katusevarv):
    joonista_sein(canvas, x, y, laius, korgus, seinavarv)
    joonista_katus(canvas, x, y, laius, korgus / 2, katusevarv)
    aken_suurus = laius / 3
    joonista_aken(canvas, x + laius / 3, y + korgus / 4, aken_suurus)


aken = tk.Tk()
aken.title("Majad")
canvas = tk.Canvas(aken, width=600, height=300, bg="white")
canvas.pack()

joonista_maja(canvas, 30, 130, 120, 100, "khaki", "brown")
joonista_maja(canvas, 200, 90, 160, 150, "lightgreen", "darkred")
joonista_maja(canvas, 420, 170, 90, 70, "salmon", "gray")

aken.mainloop()