from tkinter import *
from tkinter.ttk import *
import datetime
from time import strftime

root = Tk()
root.title("Reloj")
root.resizable(width=False, height=False)


def time():
    string = strftime('%H:%M:%S %p')
    current_date = datetime.date.today()
    get_date = current_date.strftime("%A %d/%B/%Y").replace("August", "Agosto")
    label.config(text=f'{get_date}\n{string}')
    label.after(1000, time)


label = Label(root, font=("ds-digital", 50), background="black", foreground="greenyellow")
label.pack(anchor='n')
time()
mainloop()
