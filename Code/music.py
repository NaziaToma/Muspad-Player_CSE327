import os
import pickle
import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from pygame import mixer

class Player(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		mixer.init()

			self.playlist=[]

		self.create_frames()
    
    def add_song():


	def create_frames(self):
		self.track = tk.LabelFrame(self, text='Song Track', 
					font=("times new roman",15,"bold"),
					bg="grey",fg="white",bd=5,relief=tk.GROOVE)
		self.track.config(width=600,height=300)
		self.track.grid(row=0, column=0, padx=0)

		
root = tk.Tk()
root.geometry('800x600')
root.wm_title('MusPad Player')

app = Player(master=root)
app.mainloop()