import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from .Shift import Shift


class Ablak:

    def __init__(self):
        self.master = tk.Tk()
        self.container = ttk.Frame(self.master)
        self.canvas = tk.Canvas(self.container, width=400,height=400)
        self.scrollbar = ttk.Scrollbar(self.container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.canvas.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.scrollable_frame.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        tk.Label(self.scrollable_frame, text="Szöveg").grid(row=0)
        tk.Label(self.scrollable_frame, text="K").grid(row=1)
        tk.Label(self.scrollable_frame, text="Eredmény").grid(row=2)

        self.check_var1 = IntVar()
        self.c1 = Checkbutton(self.scrollable_frame, text="Decode", variable=self.check_var1, onvalue=1, offvalue=0, )
        self.e1 = tk.Text(self.scrollable_frame, state="normal", height=10, width=40)
        self.e2 = tk.Entry(self.scrollable_frame, textvariable=IntVar(0))
        self.e3 = tk.Text(self.scrollable_frame, state="normal", height=10,  width=40)

        self.e1.grid(row=0, column=1, sticky="e")
        self.e2.grid(row=1, column=1, sticky="w")
        self.e3.grid(row=2, column=1, sticky="w")
        self.c1.grid(row=3, column=1)

        tk.Button(self.scrollable_frame,
                  text='Quit',
                  command=self.master.quit).grid(row=3,
                                                 column=0,
                                                 sticky=tk.W,
                                                 pady=4)
        tk.Button(self.scrollable_frame, text='Show', command=self.show_entry_fields).grid(row=3,
                                                                                           column=1,
                                                                                           sticky=tk.W,
                                                                                           pady=4)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.container.pack(side="left", fill="both", expand=True)

        self.scrollbar.pack(side="right", fill="y")
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.master.title("Shift coder")
        self.master.iconbitmap(default="icon.ico")
        self.master.mainloop()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.master.destroy()

    def show_entry_fields(self):
        if self.check_var1.get() is 0:
            coded_message = Shift().encode(self.e1.get(1.0, END), int(self.e2.get()))
        else:
            coded_message = Shift().decode(self.e1.get(1.0, END), int(self.e2.get()))
        print(self.check_var1.get())
        self.e3.delete(1.0, tk.END)
        self.e3.insert(10.0, coded_message)
        messagebox.showinfo("Information", coded_message)
        print("Szöveg: %s\nKód: %s" % (self.e1.get(1.0, END), self.e2.get()))
