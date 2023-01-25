import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

#https://www.guru99.com/reading-and-writing-files-in-python.html