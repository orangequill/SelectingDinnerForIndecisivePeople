import csv
import random
import tkinter as tk

class Application(tk.Frame):
	"""docstring for Application"""
	def __init__(self, master=None):
		super(Application, self).__init__()
		self.master = master
		self.pack()
		self.create_widgets()

	def selectFile(self):
		filestring = 'placesInDurham.csv'
		return filestring

	def create_widgets(self):
		topFrame = tk.Frame(self.master)
		lbl = tk.Label(topFrame, text=self.chooseRandPlace(), font=("Arial Bold", 50))
		lbl.pack()
		topFrame.pack()

	def chooseRandPlace(self):
		file = self.selectFile()
		with open(file, newline='') as f:
			content = f.readlines()
			stripped = [x.strip() for x in content]
			randMax = len(stripped)
			place = random.randint(1,randMax)
			return content[place]

	def rePick(self):
		pass


root = tk.Tk()
root.title('Place Chooser')
root.geometry('1000x250')
app = Application(master=root)
root.mainloop()