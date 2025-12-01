import tkinter as tk
from tkinter import ttk, messagebox

# Bank account data
accounts = {
    "mohit": 5000,
    "rohit": 6000,
    "sahil": 4500,
    "neha": 8000
}

# Main window
root = tk.Tk()
root.title("3D Bank Management System")
root.geometry("450x350")
root.config(bg="#1e1e1e")

# 3D Title Label
title = tk.Label(root, text="Bank Management System", 
                 font=("Arial", 20, "bold"), fg="white",
                 bg="#1e1e1e")
title.pack(pady=15)

# Create main frame (3D look)
frame = tk.Frame(root, bg="#2c2c2c", bd=8, relief="groove")
frame.pack(pady=10)

# User Selection
tk.Label(frame, text="Select Name:", font=("Arial", 12), bg="#2c2c2c", fg="white").grid(row=0, column=0, pady=10)

user_var = tk.StringVar()
user_dropdown = ttk.Combobox(frame, textvariable=user_var, values=list(accounts.keys()))
user_dropdown.grid(row=0, column=1, padx=10)


# ---------- Functions ----------
def check_balance():
    name = user_var.get()
    if name in accounts:
        messagebox.showinfo("Balance", f"{name}, your balance is: ₹{accounts[name]}")
    else:
        messagebox.showwarning("Error", "Please select a valid user!")

def deposit_money():
    name = user_var.get()
    if name in accounts:
        amount = amount_entry.get()
        if amount.isdigit():
            amount = int(amount)
            accounts[name] += amount
            messagebox.showinfo("Deposit Successful", 
                                f"₹{amount} deposited.\nNew Balance: ₹{accounts[name]}")
        else:
            messagebox.showwarning("Error", "Enter a valid amount!")
    else:
        messagebox.showwarning("Error", "Please select a valid user!")

def withdraw_money():
    name = user_var.get()
    if name in accounts:
        amount = amount_entry.get()
        if amount.isdigit():
            amount = int(amount)
            if amount <= accounts[name]:
                accounts[name] -= amount
                messagebox.showinfo("Withdrawal Successful", 
                                    f"₹{amount} withdrawn.\nNew Balance: ₹{accounts[name]}")
            else:
                messagebox.showerror("Insufficient Funds", "Not enough balance!")
        else:
            messagebox.showwarning("Error", "Enter a valid amount!")
    else:
        messagebox.showwarning("Error", "Please select a valid user!")


# Amount Entry
tk.Label(frame, text="Amount:", font=("Arial", 12), bg="#2c2c2c", fg="white").grid(row=1, column=0, pady=10)

amount_entry = tk.Entry(frame, font=("Arial", 12), bd=4, relief="sunken")
amount_entry.grid(row=1, column=1, padx=10)


# 3D Buttons
btn_style = {"font": ("Arial", 12, "bold"), "bd": 5, "relief": "raised", "width": 15}

check_btn = tk.Button(frame, text="Check Balance", command=check_balance, **btn_style, bg="#0099ff", fg="white")
check_btn.grid(row=2, column=0, pady=10)

deposit_btn = tk.Button(frame, text="Deposit", command=deposit_money, **btn_style, bg="#00cc66", fg="white")
deposit_btn.grid(row=2, column=1, pady=10)

withdraw_btn = tk.Button(frame, text="Withdraw", command=withdraw_money, **btn_style, bg="#ff3333", fg="white")
withdraw_btn.grid(row=3, column=0, columnspan=2, pady=10)


# Start App
root.mainloop()
