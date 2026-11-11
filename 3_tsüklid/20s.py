import tkinter as tk

suurus = 500
ruut = 50

aken = tk.Tk()
aken.title("Maleruudustik")

tahvel = tk.Canvas(aken, width=400, height=400, bg="white")
tahvel.pack()

for rida in range(8):
  for veerg in range(8):
    print("rida = " + str(rida), "veerg=" + str(veerg))
    if (rida + veerg) % 2 ==1:
        x = veerg * 50
        y= rida * 50
        print("x="+str(x), "y="+str(y))
        tahvel.create_rectangle(x, y, x + 50, y + 50, fill="black")

aken.mainloop()