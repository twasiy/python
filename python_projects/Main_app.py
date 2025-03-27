import tkinter as tk
from tkinter import messagebox, ttk, filedialog, simpledialog
import time
import threading
from plyer import notification
import json
import webbrowser
import os
import platform
import subprocess
from datetime import datetime

class TaskNotifier:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Notifier")
        self.root.geometry("900x700")
        self.root.configure(bg="#121212")
        
        self.reminders = self.load_reminders()
        self.bookmarks = self.load_bookmarks()
        self.todos = self.load_todos()
        
        # Title and Time
        title_label = tk.Label(root, text="Task Notifier", bg="#121212", fg="white", 
                              font=("Arial", 20, "bold"))
        title_label.pack(pady=10)
        
        self.time_label = tk.Label(root, text="", bg="#121212", fg="white", 
                                  font=("Arial", 14, "bold"))
        self.time_label.pack(pady=5)
        self.update_time()
        
        # Input Frame
        input_frame = tk.Frame(root, bg="#1f1f1f", padx=10, pady=10)
        input_frame.pack(pady=10, padx=20, fill=tk.X)
        
        tk.Label(input_frame, text="Task:", bg="#1f1f1f", fg="white", 
                font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.task_entry = tk.Entry(input_frame, width=50, font=("Arial", 12))
        self.task_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(input_frame, text="Interval (min):", bg="#1f1f1f", fg="white", 
                font=("Arial", 12, "bold")).grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.interval_entry = tk.Entry(input_frame, width=15, font=("Arial", 12))
        self.interval_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')
        
        # Button Groups
        utility_frame = tk.Frame(root, bg="#121212")
        utility_frame.pack(pady=5)
        
        tk.Button(utility_frame, text="Calculator", command=self.open_calculator, 
                 bg="#f39c12", fg="black", font=("Arial", 12, "bold"), padx=10, pady=5
                 ).grid(row=0, column=0, padx=5)
        tk.Button(utility_frame, text="Notepad", command=self.open_notepad, 
                 bg="#9b59b6", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5
                 ).grid(row=0, column=1, padx=5)
        tk.Button(utility_frame, text="Add Bookmark", command=self.add_bookmark, 
                 bg="#2ecc71", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5
                 ).grid(row=0, column=2, padx=5)
        
        reminder_btn_frame = tk.Frame(root, bg="#121212")
        reminder_btn_frame.pack(pady=5)
        
        tk.Button(reminder_btn_frame, text="Add Reminder", command=self.add_reminder, 
                 bg="#27ae60", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5
                 ).grid(row=0, column=0, padx=5)
        tk.Button(reminder_btn_frame, text="Delete Selected", command=self.delete_reminder, 
                 bg="#c0392b", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5
                 ).grid(row=0, column=1, padx=5)
        
        # Search/File Frame
        search_frame = tk.Frame(root, bg="#121212")
        search_frame.pack(pady=10)
        
        tk.Button(search_frame, text="Search Google", command=self.search_google, 
                 bg="#3498db", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5
                 ).grid(row=0, column=0, padx=5)
        tk.Button(search_frame, text="Search YouTube", command=self.search_youtube, 
                 bg="#e74c3c", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5
                 ).grid(row=0, column=1, padx=5)
        tk.Button(search_frame, text="Open File", command=self.open_file, 
                 bg="#f1c40f", fg="black", font=("Arial", 12, "bold"), padx=10, pady=5
                 ).grid(row=0, column=2, padx=5)
        
        # Reminders List
        self.tree = ttk.Treeview(root, columns=("Task", "Interval"), show="headings")
        self.tree.heading("Task", text="Task")
        self.tree.heading("Interval", text="Interval (min)")
        self.tree.column("Task", width=500, anchor="center")
        self.tree.column("Interval", width=150, anchor="center")
        self.tree.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        # Load existing reminders
        self.refresh_reminder_list()
        
        threading.Thread(target=self.start_reminders, daemon=True).start()

    def open_calculator(self):
        calculator_window = tk.Toplevel(self.root)
        calculator_window.title("Calculator")
        calculator_window.resizable(False, False)
        calculator_window.configure(bg="#2c3e50")

        display_var = tk.StringVar()
        entry = tk.Entry(calculator_window, textvariable=display_var, font=('Arial', 20), 
                        bd=10, insertwidth=4, width=14, justify='right', bg="#34495e", fg="white")
        entry.grid(row=0, column=0, columnspan=4, pady=5)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('/', 4, 3),
            ('=', 5, 0, 4)
        ]

        number_style = {'bg': '#95a5a6', 'fg': 'black', 'font': ('Arial', 14, 'bold')}
        operator_style = {'bg': '#3498db', 'fg': 'white', 'font': ('Arial', 14, 'bold')}
        equal_style = {'bg': '#2ecc71', 'fg': 'white', 'font': ('Arial', 14, 'bold')}

        for button in buttons:
            text = button[0]
            row = button[1]
            col = button[2]
            if text == '=':
                btn = tk.Button(calculator_window, text=text, **equal_style,
                               command=lambda t=text: self.on_calc_button_click(t, display_var))
                btn.grid(row=row, column=col, columnspan=4, sticky='nsew')
            else:
                style = number_style if text.isdigit() or text == '.' else operator_style
                if text == 'C':
                    style = {'bg': '#e74c3c', 'fg': 'white', 'font': ('Arial', 14, 'bold')}
                btn = tk.Button(calculator_window, text=text, **style,
                               command=lambda t=text: self.on_calc_button_click(t, display_var))
                btn.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)

        for i in range(4):
            calculator_window.columnconfigure(i, weight=1)
        for i in range(5):
            calculator_window.rowconfigure(i, weight=1)

    def on_calc_button_click(self, value, display_var):
        current = display_var.get()
        if value == 'C':
            display_var.set('')
        elif value == '=':
            try:
                result = str(eval(current))
                display_var.set(result)
            except:
                display_var.set('Error')
        else:
            display_var.set(current + value)

    def open_notepad(self):
        notepad_window = tk.Toplevel(self.root)
        notepad_window.title("Untitled - Notepad")
        notepad_window.geometry("800x600")
        
        current_file = None
        text_modified = False
        
        text_frame = tk.Frame(notepad_window,bg='#2C2C2C')
        text_frame.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        
        text_area = tk.Text(text_frame, wrap="word", font=("ubuntu sans", 12),bg='#3C3C3C',fg='white')
        text_area.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        
        scrollbar = tk.Scrollbar(text_frame, command=text_area.yview,bg='#3C3C3C')
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_area.config(yscrollcommand=scrollbar.set)
        
        status_bar = tk.Label(notepad_window, text="", anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        def update_status():
            status_bar.config(text=f"File: {current_file}" if current_file else "New File")
            title = os.path.basename(current_file) if current_file else "Untitled"
            if text_modified:
                title = "*" + title
            notepad_window.title(f"{title} - Notepad")
        
        def open_file(event=None):
            nonlocal current_file, text_modified
            file_path = filedialog.askopenfilename(
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
            )
            if file_path:
                try:
                    with open(file_path, "r") as file:
                        content = file.read()
                        text_area.delete(1.0, tk.END)
                        text_area.insert(tk.END, content)
                    current_file = file_path
                    text_modified = False
                    update_status()
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to open file: {e}")
        
        def save_file(event=None):
            nonlocal current_file, text_modified
            if current_file:
                try:
                    with open(current_file, "w") as file:
                        file.write(text_area.get(1.0, tk.END))
                    text_modified = False
                    update_status()
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save file: {e}")
            else:
                save_as_file()
        
        def save_as_file():
            nonlocal current_file, text_modified
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
            )
            if file_path:
                current_file = file_path
                save_file()
        
        menubar = tk.Menu(notepad_window,fg='white',bg='#3C3C3C')
        file_menu = tk.Menu(menubar, tearoff=0,bg='#3C3C3C')
        file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As...", command=save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=notepad_window.destroy)
        menubar.add_cascade(label="File", menu=file_menu)
        notepad_window.config(menu=menubar)
        
        text_area.bind("<Control-o>", open_file)
        text_area.bind("<Control-s>", save_file)
        text_area.bind("<<Modified>>", lambda e: (text_area.edit_modified(False), 
                          setattr(text_modified, 'True', True), update_status()))
        
        update_status()

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                if platform.system() == 'Windows':
                    os.startfile(file_path)
                elif platform.system() == 'Darwin':
                    subprocess.call(['open', file_path])
                else:
                    subprocess.call(['xdg-open', file_path])
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {str(e)}")

    def load_bookmarks(self):
        try:
            with open("bookmarks.json", "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def load_todos(self):
        try:
            with open("todos.json", "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def add_bookmark(self):
        url = simpledialog.askstring("Add Bookmark", "Enter URL:")
        if url:
            self.bookmarks.append(url)
            with open("bookmarks.json", "w") as f:
                json.dump(self.bookmarks, f)
            messagebox.showinfo("Success", "Bookmark added successfully!")

    def search_google(self):
        webbrowser.open("https://www.google.com/")

    def search_youtube(self):
        webbrowser.open("https://www.youtube.com/")

    def update_time(self):
        now = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
        self.time_label.config(text=f"Current Time: {now}")
        self.root.after(1000, self.update_time)

    def notify(self, task):
        notification.notify(
            title="Reminder",
            message=task,
            timeout=10
        )

    def start_reminders(self):
        while True:
            time.sleep(60)
            for task, interval in list(self.reminders.items()):
                self.reminders[task] -= 1
                if self.reminders[task] <= 0:
                    self.notify(task)
                    self.reminders[task] = self.load_reminders().get(task, interval)
                self.save_reminders()

    def add_reminder(self):
        task = self.task_entry.get().strip()
        interval = self.interval_entry.get().strip()
        
        if task and interval.isdigit():
            self.reminders[task] = int(interval)
            self.tree.insert("", tk.END, values=(task, interval))
            self.save_reminders()
            self.task_entry.delete(0, tk.END)
            self.interval_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Invalid Input", "Please enter valid task and time")

    def delete_reminder(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a reminder to delete")
            return
        
        for item in selected_item:
            task = self.tree.item(item, "values")[0]
            if task in self.reminders:
                del self.reminders[task]
            self.tree.delete(item)
        self.save_reminders()

    def save_reminders(self):
        with open("reminders.json", "w") as f:
            json.dump(self.reminders, f)

    def load_reminders(self):
        try:
            with open("reminders.json", "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def refresh_reminder_list(self):
        self.tree.delete(*self.tree.get_children())
        for task, interval in self.reminders.items():
            self.tree.insert("", tk.END, values=(task, interval))

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskNotifier(root)
    root.mainloop()