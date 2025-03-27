import tkinter as tk
from tkinter import messagebox
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Main Calculator Class
class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Desmos-like Scientific Calculator")
        self.root.geometry("1000x700")
        self.root.configure(bg="#2E2E2E")

        # Variables
        self.expression = ""
        self.history = []

        # Main Frame
        main_frame = tk.Frame(root, bg="#2E2E2E")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Input Frame
        input_frame = tk.Frame(main_frame, bg="#2E2E2E")
        input_frame.pack(fill=tk.X, pady=10)

        self.input_entry = tk.Entry(input_frame, font=("Arial", 24), width=40, bd=5, relief=tk.FLAT, bg="#3C3C3C", fg="white")
        self.input_entry.pack(fill=tk.X, padx=10, pady=10)

        # Buttons Frame
        buttons_frame = tk.Frame(main_frame, bg="#2E2E2E")
        buttons_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Button Layout
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("C", 1, 4),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("(", 2, 4),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), (")", 3, 4),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3), ("^", 4, 4),
            ("√", 5, 0), ("sin", 5, 1), ("cos", 5, 2), ("tan", 5, 3), ("π", 5, 4),
            ("log", 6, 0), ("ln", 6, 1), ("!", 6, 2), ("%", 6, 3), ("e", 6, 4),
            ("Graph", 7, 0), ("History", 7, 1), ("Clear", 7, 2), ("Exit", 7, 3)
        ]

        # Create Buttons
        for (text, row, col) in buttons:
            button = tk.Button(buttons_frame, text=text, font=("Arial", 18), width=5, height=2, bd=1, relief=tk.RAISED,
                               bg="#4C4C4C", fg="white", command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        # Configure Grid Weights for Buttons Frame
        for i in range(8):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for j in range(5):
            buttons_frame.grid_columnconfigure(j, weight=1)

        # History Frame
        history_frame = tk.Frame(main_frame, bg="#2E2E2E")
        history_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        self.history_label = tk.Label(history_frame, text="History", font=("Arial", 16), bg="#2E2E2E", fg="white")
        self.history_label.pack()

        self.history_text = tk.Text(history_frame, height=5, width=50, font=("Arial", 12), bg="#3C3C3C", fg="white")
        self.history_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Graph Frame
        self.graph_frame = tk.Frame(main_frame, bg="#2E2E2E")
        self.graph_frame.pack(fill=tk.BOTH, expand=True, pady=10)

    # Button Click Handler
    def on_button_click(self, text):
        if text == "=":
            self.calculate()
        elif text == "C":
            self.clear()
        elif text == "Clear":
            self.clear_history()
        elif text == "Graph":
            self.plot_graph()
        elif text == "History":
            self.show_history()
        elif text == "Exit":
            self.root.quit()
        else:
            self.expression += text
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, self.expression)

    # Clear Input
    def clear(self):
        self.expression = ""
        self.input_entry.delete(0, tk.END)

    # Clear History
    def clear_history(self):
        self.history = []
        self.history_text.delete(1.0, tk.END)

    # Show History
    def show_history(self):
        self.history_text.delete(1.0, tk.END)
        for item in self.history:
            self.history_text.insert(tk.END, item + "\n")

    # Calculate Expression
    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.history.append(f"{self.expression} = {result}")
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, result)
            self.expression = result
        except:
            messagebox.showerror("Error", "Invalid Expression")

    # Plot Graph
    def plot_graph(self):
        try:
            # Clear previous graph
            for widget in self.graph_frame.winfo_children():
                widget.destroy()

            # Parse the expression
            x = sp.symbols('x')
            expr = sp.sympify(self.expression)  # Convert string to symbolic expression
            lambdified_expr = sp.lambdify(x, expr, "numpy")  # Convert to a callable function

            # Generate x and y values
            x_vals = [i / 10.0 for i in range(-100, 100)]  # x values from -10 to 10
            y_vals = [lambdified_expr(val) for val in x_vals]  # Compute y values

            # Create a matplotlib figure
            fig, ax = plt.subplots()
            ax.plot(x_vals, y_vals, label=self.expression)  # Plot the function
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.legend()
            ax.grid()

            # Embed the graph in the Tkinter window
            canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        except Exception as e:
            messagebox.showerror("Error", f"Invalid Function for Graphing: {e}")

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()