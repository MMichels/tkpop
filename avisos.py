import tkinter as tk
from tkinter import ttk


def aviso(aviso: str):
    visivel = True

    def fechar():
        root.destroy()
        global visivel
        visivel = False

    root = tk.Tk()
    root.geometry("250x200+600+300")

    l = tk.Label(root, text=aviso)
    l.place(relx=0.2, rely=0.3)

    b = ttk.Button(root, text="Ok", command=fechar)
    b.place(relx=0.35, rely=0.5, height=30, width=76)

    root.wait_window(root)



