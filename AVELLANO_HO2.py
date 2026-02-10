import tkinter as tk

win = tk.Tk()
win.title("Jireh Mei's Profile")
win.geometry("600x600")
win.resizable(True, True)
win.configure(bg="lightblue")

profile_label = tk.Label(win, text="Student's Profile", font=("Cooper Black", 30, "bold"), bg="lightblue")
name_label = tk.Label(win, text="Name: Jireh Mei Alimpolos Avellano", font=("Kristen ITC", 15), bg="lightblue") 
age_label = tk.Label(win, text="Age: 18", font=("Kristen ITC", 15),  bg="lightblue")
course_label = tk.Label(win, text="Course: Bachelor of Science in Information Technology",font=("Kristen ITC", 15), bg="lightblue")
birthday_label = tk.Label(win, text="Birthday: August 23, 2007", font=("Kristen ITC", 15), bg="lightblue")
motto_label = tk.Label(win, text="Motto:", font=("Kristen ITC", 15), bg="lightblue")
quote_label = tk.Label(win, text="\t\"Let go and let God.\"", font=("Kristen ITC", 18, "italic"), bg="lightblue")

profile_label.pack(pady=30)
name_label.pack(pady=15, padx=20, anchor="w")
age_label.pack(pady=15, padx=20, anchor="w")
course_label.pack(pady=15, padx=20, anchor="w")
birthday_label.pack(pady=15, padx=20, anchor="w")
motto_label.pack(pady=15, padx=20, anchor="w")
quote_label.pack(pady=0, padx=0, anchor="w")

win.mainloop()
