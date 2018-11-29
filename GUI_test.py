import rpmClass_Stable as rpm
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from importlib import *

reload(rpm)



class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.total = 0
        self.entered_number = 0

        #self.folder_label_test = tk.StrVar()
        #self.
        self.folder_entry = tk.Entry(master)
        self.folder_label = tk.Label(master, text = 'Folder loc:')
        self.folder_entry.grid(row=3, column = 2)
        self.folder_label.grid(row = 3, column = 0)

        self.file_entry = tk.Entry(master)
        self.file_label = tk.Label(master, text = 'File loc:')
        self.file_entry.grid(row = 4, column = 2)
        self.file_label.grid(row = 4, column = 0)

        self.load_button = tk.Button(master, text="Load", command=rpm.load(self.folder_entry, self.file_entry))
        self.load_button.grid(row = 3.5, column = 3)

        self.total_label_text = tk.IntVar()
        self.total_label_text.set(self.total)
        self.total_label = tk.Label(master, textvariable=self.total_label_text)

        self.label = tk.Label(master, text="Total:")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = tk.Entry(master)

        self.add_button = tk.Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = tk.Button(master, text="-", command=lambda: self.update("subtract"))
        self.reset_button = tk.Button(master, text="Reset", command=lambda: self.update("reset"))

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=tk.W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=tk.E)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=tk.W+tk.E)

        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.reset_button.grid(row=2, column=2, sticky=tk.W+tk.E)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        else: # reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, tk.END)

root = tk.Tk()
my_gui = Calculator(root)
root.mainloop()


def __main__():
	print('test')