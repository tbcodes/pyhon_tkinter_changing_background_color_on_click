# Python + Tkinter: Changing background color on click

import tkinter as tk
import random

mywindow = tk.Tk()
def changeBG():
    #mywindow.config(background = "#76880A")
    colors = ["#76880A", "#7F8F87", "#65de4c", "#058ff4", "#78dd99", "black", "green", "cyan"]
    random_colors = random.choice(colors)
    mywindow.config(background = random_colors)

mywindow.geometry("520x200")
mywindow.resizable(False,False)
mywindow.title("Changing BG Color - Tkinter")
main_title = tk.Label(text="Python + Tkinter - Truzz Blogg", font=("Tahoma", 12), bg="#ff7763", fg="black", width=60, height=2)
main_title.place(x=0, y=10)
# Adding a button
main_btn = tk.Button(mywindow, text="Change Background Color", command=changeBG)
main_btn.place(x=190, y=150)

mywindow.mainloop()
