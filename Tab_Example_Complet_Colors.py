import tkinter as tk
from tkinter import ttk

root = tk.Tk()
mygreen2 = "#ddff02"
mygreen = "#d2ffd2"
myred = "#dd0202"
COLOR_1 = 'black'

style = ttk.Style()

style.theme_create( "yummy", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0],"background": mygreen2 } },
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1], "background": mygreen },
            "map":       {"background": [("selected", myred)],
                          "expand": [("selected", [1, 1, 1, 0])] } } } )


style.theme_use("yummy")



note = ttk.Notebook(root)
f1 = ttk.Frame(note, width=300, height=200)
note.add(f1, text = 'First')
f2 = tk.Frame(note, width=300, height=200, bg="black", colormap="new")
note.add(f2, text = 'Second')
note.pack(expand=1, fill='both', padx=5, pady=5)

tk.Button(root, text='yummy!').pack(fill='x')

root.mainloop()