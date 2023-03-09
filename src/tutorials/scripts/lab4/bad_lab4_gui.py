# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *

# button1.pack(expand=True, fill=BOTH)

def init_gui():
    master = Tk()
    # master.geometry("300x150")
    master.title = "Керування Гектором"
    frame1 = Frame(master)
    frame1.pack(expand=True, fill=BOTH)
    # w.pack(fill=tk.X, padx=10)

    # initialize buttons
    button1 = Button(frame1, text="Уперед")
    button1.bind("w", forward)
    # button1.bind("<Button-1>", forward)
    button1.grid(row=0, column=1)
    # button1.place(height=100, width=100, relx=30, rely=30).br
    button2 = Button(frame1, text="Назад")
    button2.bind("s", move_back, add="+")
    button2.grid(row=2, column=1)
    # button2.pack()

    # button2.place(height=100, width=100, relx=100, rely=100)
    button3 = Button(frame1, text="Ліворуч")
    button3.grid(row=1, column=0)
    # button3.place(height=100, width=100)
    button4 = Button(frame1, text="Праворуч")
    button4.grid(row=1, column=3)
    # button4.place(height=100, width=100)
    # master.focus_force()
    master.mainloop()

def forward(data):
    print(data)
    print("move forward")

def move_back(data):
    print(data)
    print("move back")


if __name__ == "__main__":
    init_gui()
