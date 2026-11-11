import tkinter as tk

laius = 600
korgus = 300
triibu_korgus = korgus / 3

aken = tk.Tk()
aken.title("Eesti lipp")

tahvel = tk.Canvas(aken, width=laius, height=korgus, bg="white", highlightthickness=0)
tahvel.pack()

# sinine triip
tahvel.create_rectangle(0, 0, laius, triibu_korgus, fill="blue", outline="")

# must triip
tahvel.create_rectangle(0, triibu_korgus, laius, 2 * triibu_korgus, fill="black", outline="")

# valge triip
tahvel.create_rectangle(0, 2 * triibu_korgus, laius, korgus, fill="white", outline="")

aken.mainloop()