import tkinter as tk
import time
import datetime


def countdowntimer():
    times = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(secs.get())

    while times > -1:
        minute, second = (times // 60, times % 60)
        hour = 0

        if minute > 60:
            hour, minute = (minute // 60, minute % 60)
        
        secs.set(second)
        mins.set(minute)
        hrs.set(hour)

        window.update()
        time.sleep(1)

        if times == 0:
            secs.set('00')
            mins.set('00')
            hrs.set('00')

        times -= 1


window = tk.Tk()

window.geometry('750x300')

secs = tk.StringVar()
tk.Entry(window, textvariable=secs, width=2, font=("Arial", 15)).place(x=220, y=120)
secs.set('00')

mins = tk.StringVar()
tk.Entry(window, textvariable=mins, width=2, font=("Arial", 15)).place(x=180, y=120)
mins.set('00')

hrs = tk.StringVar()
tk.Entry(window, textvariable=hrs, width=2, font=("Arial", 15)).place(x=142, y=120)
hrs.set('00')


tk.Label(window, font=('Arial', 22), text='Set Timer', bg='black').place(x=105, y=70)
tk.Button(window, text='Start', bd='2', bg='red', font=('Arial', 12), command=countdowntimer).place(x=167, y=165)

window.mainloop()

