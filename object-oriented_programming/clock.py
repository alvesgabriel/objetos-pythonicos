from time import strftime
from tkinter import Label

clock = Label()
clock.pack()

clock["font"] = "Helvetica 90 bold"


def tictac():
    clock["text"] = strftime("%H:%M:%S")
    clock.after(100, tictac)


if __name__ == "__main__":
    tictac()
    clock.mainloop()
