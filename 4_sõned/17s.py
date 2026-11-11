import tkinter as tk

aken = tk.Tk()
aken.title("Minu kujundid")

tahvel = tk.Canvas(aken, width=600, height=400, bg="white")
tahvel.pack()

# punane ristkülik
tahvel.create_rectangle(50, 50, 200, 130, fill="red")

# sinine ring
tahvel.create_oval(300, 40, 400, 140, fill="blue")

# roheline joon
tahvel.create_line(50, 200, 250, 280, fill="green", width=4)

# kollane ovaal
tahvel.create_oval(350, 200, 550, 290, fill="yellow")

# tekst
tahvel.create_text(300, 350, text="Minu kujundid", font=("Arial", 20))

aken.mainloop()
