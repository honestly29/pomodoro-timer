import tkinter as tk
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    time_label.after(1000, update)


window = tk.Tk()

time_label = tk.Label(window, font=("Arial",50), fg="white", bg="black")
time_label.pack()

update()

window.mainloop()