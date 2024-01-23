import tkinter as tk
class Calculatrice:
    def __init__(self, master):
        self.master = master
        master.title('Calculatrice')
        self.display = tk.Entry(master, bg="#98FB98")
        self.display.grid(row=0, column=0, columnspan=3, )
        for i in range(10):
            tk.Button(master, text=str(i), command=lambda)
