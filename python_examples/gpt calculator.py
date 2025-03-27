import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "Add":
            result.set(str(add(num1, num2)))
        elif operation == "Subtract":
            result.set(str(subtract(num1, num2)))
        elif operation == "Multiply":
            result.set(str(multiply(num1, num2)))
        elif operation == "Divide":
            result.set(str(divide(num1, num2)))
        else:
            result.set("Select an operation")
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers")

root = tk.Tk()
root.title("Calculator")
root.geometry('350x150')

tk.Label(root, text="Enter first number:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter second number:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

operation_var = tk.StringVar()
operation_var.set("Add")
operations = ["Add", "Subtract", "Multiply", "Divide"]
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.grid(row=2, column=1)
operation_menu.config(width=10)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=1)

result = tk.StringVar()
tk.Label(root, text="Result:").grid(row=4, column=0)
tk.Entry(root, textvariable=result, state='readonly').grid(row=4, column=1)

root.mainloop()
