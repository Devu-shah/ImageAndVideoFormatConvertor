# import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os

# Making Screen
root = Tk()

# Canvases
canvas1 = Canvas(root, width=300, height=250, bg='azure3', relief='raised')
# canvas1.pack()

label1 = Label(root, text ="Image Format Convertor", fg="red", bg="Black", font=('helvetica', 20)).grid(sticky = N, pady=5, padx=10)
canvas1.create_window(150, 60, window=label1)

notif = Label(root, font=('times new roman', 10))
notif.grid(row=4, sticky=N, pady=5, padx=10)
canvas1.create_window(200, 150, window=notif)

notif.config(fg='red', text='File Not Selected Still !')

# Get the PNG file
def getPNG():
	global im1

	import_file_path = filedialog.askopenfilename()
	im1 = Image.open(import_file_path)

	notif.config(fg='green', text="File Selected Successfully !")

	im1.resize((150,150))
	im1 = ImageTk.PhotoImage(im1)
	Label(root, image=im1).grid(row=5, sticky = N, pady = 15)
	Label(root, text='Selected File', fg='Green', font=('Algerian', 15)).grid(row=6, sticky=N, pady=5, padx=10)
	Label(root, text='☝☝', fg='Green', font=('Algerian', 15)).grid(row=6, pady=5, padx=10, sticky=E)


def converttoJPG():
	export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
	im1.save(export_file_path)

	
browseButton_PNG = Button(text = "Import PNG File", command = getPNG, bg='royalblue', fg='white', font=('helventica', 12, 'bold'))
browseButton_PNG.grid(row=1, sticky = N, pady=5, padx=10)


saveAsButton_JPG = Button(root, text='Save As',font=('times new roman', 12), fg='black', bg='red', command=converttoJPG).grid(row=3, sticky=N, pady=5, padx=10)

root.mainloop()