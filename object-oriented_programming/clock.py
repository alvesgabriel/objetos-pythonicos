from time import strftime
from tkinter import Label


class Clock(Label):
    """
    Create a clock
    """
    def __init__(self):
        super().__init__()
        self.pack()
        self["font"] = "Helvetica 90 bold"
        self["text"] = strftime("%H:%M:%S")
        self.tictac()

    def tictac(self):
        self["text"] = strftime("%H:%M:%S")
        self.after(100, self.tictac)


if __name__ == "__main__":
    clock = Clock()
    clock.mainloop()
