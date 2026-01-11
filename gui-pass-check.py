import tkinter as tk
from tkinter import messagebox
import re

def check(password):
    strength = 0

    if len(password) >= 8: strength += 1
    if re.search(r"[A-Z]", password): strength += 1
    if re.search(r"[a-z]", password): strength += 1
    if re.search(r"[0-9]", password): strength += 1
    if re.search(r"[@$!%*?&]", password): strength += 1

    if strength == 5:
        return "STRONG"
    elif strength >= 3:
        return "MEDIUM"
    else:
        return "WEAK"

def analyze():
    pwd = entry.get()
    result = check(pwd)
    messagebox.showinfo("Password Strength", f"Your password is: {result}")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x200")

label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, show="*", width=25, font=("Arial", 12))
entry.pack()

btn = tk.Button(root, text="Check Strength", command=analyze, font=("Arial", 12))
btn.pack(pady=20)

root.mainloop()
