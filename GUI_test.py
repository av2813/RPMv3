__author__ = 'Alex'
import matplotlib
matplotlib.use('TkAgg')
import rpmClass_Stable as rpm

import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import os
from importlib import *
from tkinter.filedialog import askopenfilename
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

reload(rpm)



class Calculator:

	def __init__(self, master):
		self.master = master
		master.title("Calculator")
		self.lattice = rpm.ASI_RPM(1,1)

		self.total = 0
		self.entered_number = 0
		mainframe = tk.Frame(root)
		#mainframe.grid(column=5,row=5, sticky=(tk.N,tk.W,tk.E,tk.S) )
		#mainframe.columnconfigure(5, weight = 1)
		#mainframe.rowconfigure(5, weight = 1)
		#mainframe.pack(pady = 100, padx = 100)
		#self.folder_label_test = tk.StrVar()
		#self.
		self.box = tk.Entry(master)
		self.box.pack()
		self.folder_entry = tk.Entry(master)
		self.folder_label = tk.Label(master, text = 'Folder loc:')
		self.folder_entry.pack()
		self.folder_label.pack()

		self.file_entry = tk.Entry(master)
		self.file_label = tk.Label(master, text = 'File loc:')
		self.file_entry.pack()
		self.file_label.pack()
		#test = askopenfilename()
		#print(test)
		self.load_button = tk.Button(master, text="Load", command=self.load)
		self.load_button.pack()

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


		self.graphoptions = tk.StringVar(master)
		self.graphchoices = {'Count', 'Magnetic charge', 'Local correlation', 'Magnetic field', 'Vertex type'}
		self.graphoptions.set('Count')
		self.popmenu = tk.OptionMenu(mainframe, self.graphoptions, *self.graphchoices)
		self.popmenu_label = tk.Label(mainframe, text="Lattice graph type:")
		self.popmenu_label.pack()
		self.popmenu.pack()

		self.graph_button = tk.Button(master, text="Graph", command=self.graph)
		self.graph_button.pack()


	def graph(self):

		print(self.graphoptions.get())
		if self.graphoptions.get() == 'Count':
			fig = self.lattice.graph(show =False)
		if self.graphoptions.get() == 'Magnetic charge':
			self.lattice.graphCharge(show =False)
		if self.graphoptions == 'Local correlation':
			self.lattice.localCorrelation(show =False)
		if self.graphoptions.get() == 'Magnetic field':
			self.lattice.fieldPlot(show =False)
		if self.graphoptions.get() == 'Vertex type':
			self.lattice.vertexTypeMap(show =False)
		canvas = FigureCanvasTkAgg(fig, master=self.master)
		canvas.get_tk_widget().pack()
		canvas.draw()



	def load(self):
		filename = askopenfilename()
		try:
			print(filename)
			self.lattice.load(filename)
		except:
			print('This is not a Lattice file')

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