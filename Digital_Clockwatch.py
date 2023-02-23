from tkinter import *
import time as t

dw = Tk()
dw.title("DIGITAL CLOCK")
dw.geometry("800x100")

def time():
    d = t.strftime("%d-%m-%y , %H:%M:%S %p")
    l.config(text=d)
    l.after(1000,time)

l=Label(dw,font=('Orpheus Italic',25),text = " The most precious resource we all have is Time ")
l.pack()

l=Label(dw,font=('arial',25),bg="black",fg="yellow")
l.pack()

time()

mainloop()