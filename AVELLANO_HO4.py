import tkinter as tk

win = tk.Tk()

win.title("PROFILE BUILDER")
win.geometry("400x400")
win.resizable(True, True)
win.configure(bg = "lightpink", cursor = "arrow")

prfbldr = tk.Label(win, text = "Profile Builder", bg = "lightpink", font = ("Cooper Black", 15))
prfbldr.pack(padx = 15, pady = 15)

frame = tk.Frame(win, bg = "lightgrey")
frame.pack()

frstlabl = tk.Label(frame, text = "First Name", bg = "lightgrey")
frstlabl.grid(row = 3, column = 1, columnspan = 2)

frstnm = tk.Entry(frame)
frstnm.grid(row = 2, column = 1, columnspan = 2)

scndlabl = tk.Label(frame, text = "Middle Name", bg = "lightgrey")
scndlabl.grid(row = 3, column = 3, columnspan = 2)

mddlnm = tk.Entry(frame)
mddlnm.grid(row = 2, column = 3, columnspan = 2)

thrdlabl = tk.Label(frame, text = "Last Name", bg = "lightgrey")
thrdlabl.grid(row = 3, column = 5, columnspan = 2)

lstnm = tk.Entry(frame)
lstnm.grid(row = 2, column = 5, columnspan = 2)

frthlbl = tk.Label(frame, text = "Birth Year", bg = "lightgrey")
frthlbl.grid(row = 5, column = 1, columnspan = 2)

brthyr = tk.Entry(frame)
brthyr.grid(row = 4, column = 1, columnspan = 2)

gndrlbl = tk.Label(frame, text = "Gender", bg = "lightgrey")
gndrlbl.grid(row = 7, column = 1, columnspan = 2)

radio_val = tk.IntVar()

gndrml = tk.Radiobutton(frame, text= "Male", bg = "lightgrey", variable = radio_val, value = 0)
gndrml.grid(row = 7, column = 2, columnspan = 2)

gndrfml = tk.Radiobutton(frame, text= "Female", bg = "lightgrey", variable = radio_val, value = 1)
gndrfml.grid(row = 7, column = 4, columnspan = 2)

button = tk.Button(win, text =" Submit", relief = "sunken", activebackground = "blue", activeforeground = "lightgrey")
button.pack(pady=10)



# frstnm = tk.StringVar()
# mddlnm = tk.StringVar()
# lstnm = tk.StringVar()
# brthyr = tk.StringVar()
# gender = tk.StringVar()
# age = tk.StringVar()




win.mainloop()