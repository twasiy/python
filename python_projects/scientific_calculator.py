from tkinter import *
import math

expression = ""

def on_button_click(char):
    global expression
    if char == "C":
        expression = ""
    elif char == "=":
        try:
            expression = str(eval(expression))
        except:
            expression = "Error"
    elif char == "\u03C0":  # Pi symbol (π)
        expression += str(math.pi)
    elif char == "x²":
        expression = str(eval(expression + "**2"))
    elif char == "√":
        expression = str(math.sqrt(eval(expression)))
    elif char == "mod":
        expression += "%"
    else:
        expression += char
    
    update_entry()
    

def update_entry():
    entry.delete(0, END)
    entry.insert(END, expression)

root = Tk()
root.title('Scientific Calculator')
root.geometry('420x550')
root.config(bg='#1C1C1C')

entry = Entry(root, font=('Arial', 30, 'bold'), relief=RIDGE, borderwidth=3, 
              justify='right', bg='#333', fg='white', width=20)
entry.grid(row=0, column=0, columnspan=5, pady=15, padx=10)

buttons = [
    ('C', 1, 0), ('(', 1, 1), (')', 1, 2), ('mod', 1, 3), ('\u03C0', 1, 4),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3), ('√', 2, 4),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3), ('x²', 3, 4),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3), ('%', 4, 4),
    ('0', 5, 0), ('.', 5, 1), ('+', 5, 2), ('=', 5, 3, 2, 2)
]

for button in buttons:
    text, row, col = button[0], button[1], button[2]
    rowspan = button[3] if len(button) >= 4 else 1
    colspan = button[4] if len(button) == 5 else 1
    btn_color = '#F28C28' if text == '=' else '#333'
    button = Button(root, text=text, font=('Arial', 18), width=6, height=2, 
                    command=lambda t=text: on_button_click(t), bg=btn_color, fg='white')
    button.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, padx=5, pady=5, sticky='nsew')

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(5):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()

