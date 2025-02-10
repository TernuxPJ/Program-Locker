import psutil
import time
import tkinter as tk
from tkinter import messagebox
from threading import Thread

blocked_programs = []

def block_programs():
    while True:
        for proc in psutil.process_iter(attrs=['pid', 'name']):
            try:
                if proc.info['name'].lower() in blocked_programs:
                    print(f"Blocked {proc.info['name']} ...")
                    proc.terminate()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        time.sleep(1)

def start_blocking():
    program_name = entry.get().strip().lower()
    if program_name and program_name not in blocked_programs:
        blocked_programs.append(program_name)
        entry.delete(0, tk.END)
        messagebox.showinfo("Started", f"Blocking {program_name.capitalize()} started!")
    elif program_name in blocked_programs:
        messagebox.showwarning("Warning", "This program is already blocked!")
    else:
        messagebox.showerror("Error", "Please enter a valid program name.")

root = tk.Tk()
root.title("Program Blocker")
root.geometry("950x600")
root.config(bg="#2c3e50")

title_font = ("Montserrat", 26, "bold")
label_font = ("Montserrat", 14)
button_font = ("Montserrat", 16, "bold")
result_font = ("Montserrat", 16)

frame = tk.Frame(root, bg="#34495e", relief="flat", bd=0, padx=40, pady=40)
frame.place(relx=0.5, rely=0.5, anchor="center")

title_label = tk.Label(frame, text="Program Blocker", font=title_font, fg="#ecf0f1", bg="#34495e")
title_label.grid(row=0, column=0, columnspan=2, pady=40)

city_label = tk.Label(frame, text="Enter Program Name:", font=label_font, fg="#ecf0f1", bg="#34495e")
city_label.grid(row=1, column=0, padx=15, pady=10, sticky="w")

entry = tk.Entry(frame, font=("Montserrat", 16), bd=0, relief="solid", width=35,
                 fg="#ecf0f1", bg="#2c3e50", insertbackground="white", justify="center")
entry.grid(row=1, column=1, padx=15, pady=10)

start_button = tk.Button(frame, text="Start Blocking", font=button_font, bg="#1abc9c", fg="white", bd=0,
                         relief="flat", width=20, height=2, command=start_blocking)
start_button.grid(row=2, column=0, columnspan=2, pady=30)

exit_button = tk.Button(frame, text="Exit", font=button_font, bg="#e74c3c", fg="white", bd=0,
                        relief="flat", width=20, height=2, command=root.quit)
exit_button.grid(row=3, column=0, columnspan=2, pady=20)

def on_enter(e):
    start_button['bg'] = "#16a085"

def on_leave(e):
    start_button['bg'] = "#1abc9c"

start_button.bind("<Enter>", on_enter)
start_button.bind("<Leave>", on_leave)

block_thread = Thread(target=block_programs, daemon=True)
block_thread.start()

root.mainloop()
