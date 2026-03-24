import tkinter as tk

win = tk.Tk()
win.title("AVELLANO HANDS-OUT EXAM")
win.geometry("900x400")
win.resizable(True, True)
win.configure(bg = "lightgrey")

greet = tk.Label(text = "Welcome!", font = ("Cooper Black", 50, "bold"), bg = "lightgrey")
greet.pack(pady=15)


def reg():
    win = tk.Tk()
    win.title("AVELLANO HANDS-OUT EXAM")
    win.geometry("350x200")
    win.resizable(True, True)
    win.configure(bg = "lightyellow")

    ttl1 = tk.Label(win, text = "Register Form", font = ("Poppins", 15, "bold"), bg = "lightyellow")
    ttl1.grid(row=0, column=2)

    usrnm = tk.Label(win, text="  Username", bg="lightyellow", font=("Arial", 10, "bold"))
    usrnm.grid(row= 1, column=1)

    username_ent = tk.Entry(win)
    username_ent.grid(row=1, column= 2)

    psswrd = tk.Label(win, text="  Password", bg="lightyellow", font=("Arial", 10, "bold"))
    psswrd.grid(row= 2, column=1)

    password_ent = tk.Entry(win, show="*")
    password_ent.grid(row=2, column= 2)

    check_val = tk.IntVar()

    check_btn = tk.Checkbutton(win, text = "Show Password", variable = check_val)
    check_btn.grid(row=3, column=2)

    register = tk.Button(win, text="Register", font = ("Poppins", 10, "italic"), command = reg)
    register.grid(row=4, column=2)

reg = tk.Button(win, text="Register", font = ("Cooper Black", 30, "bold"), bg="Blue", command = reg)
reg.pack(pady=40)



def log():
    win = tk.Tk()
    win.title("AVELLANO HANDS-OUT EXAM")
    win.geometry("350x200")
    win.resizable(True, True)
    win.configure(bg = "Green")

    ttl2 = tk.Label(win, text = "Log In", font = ("Poppins", 15, "bold"), bg = "Green")
    ttl2.grid(row=0, column=2)

    usrnm = tk.Label(win, text="  Username", bg="Green", font=("Arial", 10, "bold"))
    usrnm.grid(row= 1, column=1)

    username_ent = tk.Entry(win)
    username_ent.grid(row=1, column= 2)

    psswrd = tk.Label(win, text="  Password", bg="Green", font=("Arial", 10, "bold"))
    psswrd.grid(row= 2, column=1)

    password_ent = tk.Entry(win)
    password_ent.grid(row=2, column= 2)

    check_val = tk.IntVar()

    check_btn = tk.Checkbutton(win, text = "Show Password", variable = check_val)
    check_btn.grid(row=3, column=2)

    login = tk.Button(win, text="Log In", font = ("Poppins", 10, "italic"), command = reg)
    login.grid(row=4, column=2)

log = tk.Button(win, text="Log In", font = ("Cooper Black", 30, "bold"), bg="Green", command = log)
log.pack()

win.mainloop()
