import tkinter as tk

suurus = 500
samm = 50

aken = tk.Tk()
aken.title("Koordinaatvõrgustik")

tahvel = tk.Canvas(aken, width=suurus, height=suurus, bg="white")
tahvel.pack()

for i in range(0, suurus + 1, samm):
    # vertikaalne joon
    tahvel.create_line(i, 0, i, suurus, fill="gray")
    tahvel.create_text(i, 10, text=str(i), font=("Arial", 8))

    # horisontaalne joon
    tahvel.create_line(0, i, suurus, i, fill="gray")
    tahvel.create_text(15, i, text=str(i), font=("Arial", 8))

aken.mainloop()