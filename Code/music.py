import os
import pickle
import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter import Menu
from pygame import mixer

class Player(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		
		self.playlist=[]

		self.create_frames()
		self.initUI()

	def initUI(self):

		menubar = Menu(self.master)
		self.master.config(menu=menubar)

		fileMenu = Menu(menubar)
		fileMenu.add_command(label="Exit", command=self.onExit)
		menubar.add_cascade(label="Add Song", menu=fileMenu)

	def onExit(self):

		self.quit()
			
	def create_frames(self):
		self.track = tk.LabelFrame(self,
					font=("times new roman",15,"bold"),
					bg="white",fg="white",bd=5,relief=tk.GROOVE)
		self.track.config(width=600,height=400)
		self.track.grid(row=0, column=0, padx=10, pady=30)

		self.controls = tk.LabelFrame(self,
							font=("times new roman",15,"bold"),
							bg="white",fg="white",bd=2,relief=tk.GROOVE)
		self.controls.config(width=600,height=80)
		self.controls.grid(row=2, column=0, pady=35, padx=10)



		
root = tk.Tk()
root.geometry('800x600')
root.wm_title('MusPad Player')

app = Player(master=root)
app.mainloop()