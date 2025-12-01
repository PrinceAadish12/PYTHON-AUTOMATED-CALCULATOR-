import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        choice = operation.get()

        if choice == "Addition":
            result = num1 + num2
        elif choice == "Subtraction":
            result = num1 - num2
        elif choice == "Multiplication":
            result = num1 * num2
        elif choice == "Division":
            if num2 == 0:
                messagebox.showerror("Error", "You cannot divide by zero!")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Please select an operation!")
            return

        label_result.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")


# ---------- GUI SETUP ----------
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("350x300")
window.configure(bg="#e1e8f0")

# Title
title = tk.Label(window, text="Calculator", font=("Arial", 20, "bold"), bg="#e1e8f0")
title.pack(pady=10)

# Number 1
label1 = tk.Label(window, text="Enter first number:", bg="#e1e8f0", font=("Arial", 12))
label1.pack()
entry_num1 = tk.Entry(window, width=20, font=("Arial", 12))
entry_num1.pack(pady=5)

# Number 2
label2 = tk.Label(window, text="Enter second number:", bg="#e1e8f0", font=("Arial", 12))
label2.pack()
entry_num2 = tk.Entry(window, width=20, font=("Arial", 12))
entry_num2.pack(pady=5)

# Operation Menu
operation = tk.StringVar()
operation.set("Addition")  # default choice

dropdown = tk.OptionMenu(window, operation, "Addition", "Subtraction", "Multiplication", "Division")
dropdown.config(font=("Arial", 12))
dropdown.pack(pady=10)

# Calculate Button
btn = tk.Button(window, text="Calculate", command=calculate, font=("Arial", 14), bg="#4CAF50", fg="white")
btn.pack(pady=10)

# Result Label
label_result = tk.Label(window, text="Result: ", font=("Arial", 14), bg="#e1e8f0")
label_result.pack(pady=10)

# Run the window
window.mainloop()
