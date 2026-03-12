import tkinter as tk

win = tk.Tk()

win.title("SIMPLE CALCULATOR^^")
win.geometry("300x220")
win.resizable(True, True)
win.configure(bg = "blue", cursor = "cross")

mn = tk.Label(win, text = "Simple Calculator", font = ("Cooper Black", 15))
mn.pack(padx = 10, pady = 10)

frame = tk.Frame(win)
frame.pack()

frstlabl = tk.Label(frame, text = "Enter 1st number:")
frstlabl.grid(row = 1, column = 0, columnspan = 2)

frstnm = tk.Entry(frame)
frstnm.grid(row = 1, column = 2, columnspan = 2)

scndlabl = tk.Label(frame, text = "Enter 2nd number:")
scndlabl.grid(row = 2, column = 0, columnspan = 2)

scndnm = tk.Entry(frame)
scndnm.grid(row = 2, column = 2, columnspan = 2)

def add():
    nmb1 = float(frstnm.get())
    nmb2 = float(scndnm.get())
    mn.config(text="The sum is " + str(nmb1 + nmb2))

def subtract():
    nmb1 = float(frstnm.get())
    nmb2 = float(scndnm.get())
    mn.config(text="The difference is " + str(nmb1 - nmb2))

def multiply():
    nmb1 = float(frstnm.get())
    nmb2 = float(scndnm.get())
    mn.config(text="The product is " + str(nmb1 * nmb2))

def division():
    nmb1 = float(frstnm.get())
    nmb2 = float(scndnm.get())
    mn.config(text="The quotient is " + str(nmb1 / nmb2))

btn_add = tk.Button(win, text = "Add", command=add)
btn_add.place (x = 86, y = 100)

btn_subtract = tk.Button(win, text = "Subtract", command=subtract)
btn_subtract.place (x = 170, y = 100)

btn_multiply = tk.Button(win, text = "Multiply", command=multiply)
btn_multiply.place (x = 80, y = 135)

btn_division = tk.Button(win, text = "Division", command=division)
btn_division.place (x = 171, y = 135)

win.mainloop()