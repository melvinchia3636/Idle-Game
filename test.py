from tkinter import *
import time

n=0

main = Tk()

def current_money():
    global n
    n+=1
    return n

now = StringVar()
num = Label(main, font=('Helvetica', 24))
num.pack(side="top")
num["textvariable"] = now

def onUpdate():
    now.set(current_money())
    num.after(1000, onUpdate)

onUpdate()

main.mainloop()
