import tkinter as tk
from tkinter import messagebox
import string
import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters (!@#$ etc.).")

    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score == 3 or score == 4:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    return strength, color, feedback

def analyze_password():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    strength, color, tips = check_password_strength(password)
    result_label.config(text=f"Strength: {strength}", fg=color)

    tips_text.delete("1.0", tk.END)
    if tips:
        tips_text.insert(tk.END, "\n".join(tips))
    else:
        tips_text.insert(tk.END, "Great password!")

# GUI setup
root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("450x320")
root.configure(bg="#1e1e2e")

# Title
tk.Label(root, text="Password Complexity Checker", font=("Arial", 16, "bold"), fg="white", bg="#1e1e2e").pack(pady=10)

# Entry
entry = tk.Entry(root, width=40, show='*', font=("Arial", 12))
entry.pack(pady=10)

# Button
check_btn = tk.Button(root, text="Check Password", command=analyze_password, font=("Arial", 12), bg="#3b82f6", fg="white", padx=10, pady=5)
check_btn.pack(pady=5)

# Result
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#1e1e2e")
result_label.pack(pady=5)

# Feedback Box
tk.Label(root, text="Feedback:", font=("Arial", 12, "bold"), fg="white", bg="#1e1e2e").pack()
tips_text = tk.Text(root, height=6, width=50, font=("Arial", 10))
tips_text.pack(pady=5)

root.mainloop()
