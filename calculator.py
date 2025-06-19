import tkinter as tk
import math

def calculate():
    try:
        num1 = float(entry1.get())
        operation = operation_var.get()
        
        # Square root requires only one input
        if operation == '√':
            result = math.sqrt(num1)
        else:
            num2 = float(entry2.get())
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    result_label.config(text="Error: Division by zero!")
                    return
                result = num1 / num2
            elif operation == '%':
                result = num1 % num2
            elif operation == '^':
                result = num1 ** num2
            else:
                result_label.config(text="Invalid Operation")
                return
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Error: Enter valid number(s)")

def clear_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result: ")

# GUI setup
root = tk.Tk()
root.title("Advanced Calculator")

# Entry fields
tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number (if needed):").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Operations
tk.Label(root, text="Select operation:").pack()
operation_var = tk.StringVar(value='+')
operations = ['+', '-', '*', '/', '%', '^', '√']
for op in operations:
    tk.Radiobutton(root, text=op, variable=operation_var, value=op).pack(anchor='w')

# Buttons
tk.Button(root, text="Calculate", command=calculate).pack(pady=5)
tk.Button(root, text="Clear", command=clear_fields).pack(pady=5)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Start GUI
root.mainloop()

