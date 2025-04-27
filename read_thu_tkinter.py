import tkinter as tk
from tkinter import filedialog

menu = tk.Tk ()
menu.withdraw () # to ukrywa okno
menu.title ("Moje pierwsze menu") #nagłowek
menu.geometry ("600x600") #wielkość okna

file_path = filedialog.askopenfilename(title="Wybierz plik", filetypes=[("Text Files", "*.txt")])

if file_path:
    with open(file_path) as fh:
        inp = fh.read().rstrip().upper()
    print(inp)
else:
    print("Nie wybrano pliku.")





