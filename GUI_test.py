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
		master.title("ASI")
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
		#self.box = tk.Entry(self.master)
		#self.box.pack()
		#self.folder_entry = tk.Entry(self.master)
		#self.folder_label = tk.Label(self.master, text = 'Folder loc:')
		#self.folder_entry.pack()
		#self.folder_label.pack()

		#self.file_entry = tk.Entry(self.master)
		#self.file_label = tk.Label(self.master, text = 'File loc:')
		#self.file_entry.pack()
		#self.file_label.pack()
		#test = askopenfilename()
		#print(test)
		self.load_button = tk.Button(self.master, text="Load", command=self.load)
		self.load_button.pack()

		self.total_label_text = tk.IntVar()
		self.total_label_text.set(self.total)
		self.total_label = tk.Label(self.master, textvariable=self.total_label_text)

		self.label = tk.Label(self.master, text="Total:")

		vcmd = self.master.register(self.validate) # we have to wrap the command
		#self.entry = tk.Entry(self.master)

		# LAYOUT


		self.graphoptions = tk.StringVar(self.master)
		self.graphchoices = {'Count', 'Magnetic charge', 'Local correlation', 'Magnetic field', 'Vertex type'}
		self.graphoptions.set('Count')
		self.popmenu = tk.OptionMenu(self.master, self.graphoptions, *self.graphchoices)
		self.popmenu_label = tk.Label(self.master, text="Lattice graph type:")
		self.popmenu_label.pack()
		self.popmenu.pack()
		
		#self.graphoptions.pack()

		self.graph_button = tk.Button(master, text="Graph", command=self.graph)
		self.graph_button.pack()
		self.fig = plt.figure('test')
		self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
		self.canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
		self.canvas.get_tk_widget().delete("all")

		#self.canvas = None
		self.total_label_text = tk.IntVar()
		self.total_label_text.set(self.total)
		self.total_label = tk.Label(self.master, textvariable=self.total_label_text)
		self.energy_button = tk.Button(self.master, text="Energy", command=self.energy_calc)
		self.energy_button.pack()
		self.energy_entry = tk.Entry(master)
		self.energy_entry.pack()

		#self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
		#self.canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
		#self.canvas.get_tk_widget().pack()
		#self.canvas.show()

	def energy_calc(self):
		eng = self.lattice.demagEnergy(4)
		self.total_label_text.set(self.total)

	def graph(self):
		#canvas = None		
		print(self.graphoptions.get())
		if self.graphoptions.get() == 'Count':
			plt.clf()
			self.fig = self.lattice.graph(show =False)
		if self.graphoptions.get() == 'Magnetic charge':
			plt.clf()
			self.fig = self.lattice.graphCharge(show =False)
		if self.graphoptions == 'Local correlation':
			plt.clf()
			self.fig = self.lattice.localCorrelation(show =False)
		if self.graphoptions.get() == 'Magnetic field':
			plt.clf()
			self.fig = self.lattice.fieldPlot(show =False)
		if self.graphoptions.get() == 'Vertex type':
			plt.clf()
			self.fig = self.lattice.vertexTypeMap(show =False)
		
		print(self.fig)
		self.canvas.draw()
		#plt.show()



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