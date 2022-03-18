import tkinter as tk
from tkinter import ttk

nova = tk.Tk()

nova.geometry('300x300')
nova.title('New window')
nova.resizable(False, False)

ttk.Label(nova, text='teste').pack()

tk.Button(nova, text='Sair', command=nova.quit).pack()

nova.mainloop()
nova.destroy()

print('fui encerrado agora')
