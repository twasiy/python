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
        

        # Variables
        current_file = None
        text_modified = False
        font_size = 12  # Default font size
        

        # Text Frame
        text_frame = tk.Frame(notepad_window,bg='#2C2C2C')
        text_frame.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        text_area = tk.Text(text_frame,wrap = 'word',font=('ubuntu sans',12),bg = '#3C3C3C',fg='white')
        text_area.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)


        # Line Numbers
        line_numbers = tk.Text(text_frame, width=4, padx=5, pady=5, bg="#2C2C2C", fg="white", state="disabled")
        line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        #Text area
        text_area = tk.Text(text_frame, wrap="word", font=("Consolas",font_size), bg="#3C3C3C", fg="white", undo=True)
        text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


        # Scrollbar
        scrollbar = tk.Scrollbar(text_frame, command= on_scroll)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_area.config(yscrollcommand= scrollbar.set)

        # Bind Events
        text_area.bind("<KeyRelease>", update_line_numbers)
        text_area.bind("<MouseWheel>", on_scroll)
        text_area.bind("<Button-4>", on_scroll)
        text_area.bind("<Button-5>", on_scroll)
        text_area.bind("<<Modified>>", on_text_modified)

        # Menu Bar
        menubar = tk.Menu(notepad_window)

        # File Menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command= new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Open", command= open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command= save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As", command= save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=notepad_window.quit)
        menubar.add_cascade(label="File", menu=file_menu)


        # Edit Menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Undo", command=undo, accelerator="Ctrl+Z")
        edit_menu.add_command(label="Redo", command=self.redo, accelerator="Ctrl+Y")
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=cut_text, accelerator="Ctrl+X")
        edit_menu.add_command(label="Copy", command=copy_text, accelerator="Ctrl+C")
        edit_menu.add_command(label="Paste", command=paste_text, accelerator="Ctrl+V")
        edit_menu.add_command(label="Select All", command=select_all, accelerator="Ctrl+A")
        edit_menu.add_separator()
        edit_menu.add_command(label="Find", command=find_text, accelerator="Ctrl+F")
        edit_menu.add_command(label="Replace", command=replace_text, accelerator="Ctrl+H")
        edit_menu.add_separator()
        edit_menu.add_command(label="Time/Date", command=insert_time_date, accelerator="F5")
        menubar.add_cascade(label="Edit", menu=edit_menu)
        

        # Format Menu
        format_menu = tk.Menu(menubar, tearoff=0)
        format_menu.add_command(label="Word Wrap", command= toggle_word_wrap)
        format_menu.add_command(label="Font", command= change_font)
        menubar.add_cascade(label="Format", menu=format_menu)

        # View Menu
        view_menu = tk.Menu(menubar, tearoff=0)
        view_menu.add_command(label="Zoom In", command= zoom_in, accelerator="Ctrl++")
        view_menu.add_command(label="Zoom Out", command= zoom_out, accelerator="Ctrl+-")
        view_menu.add_separator()
        view_menu.add_command(label="Dark/Light Mode", command= toggle_theme)
        menubar.add_cascade(label="View", menu=view_menu)

        root.config(menu=menubar)

        # Initialize Line Numbers
        update_line_numbers()

        # Update Line Numbers
        def update_line_numbers(event=None):
        # Get the number of lines in the text area
            lines = text_area.get("1.0", "end-1c").split("\n")
            line_count = len(lines)

        # Update the line numbers
            line_numbers.config(state="normal")
            line_numbers.delete("1.0", "end")
            line_numbers.insert("1.0", "\n".join(str(i) for i in range(1, line_count + 1)))
            line_numbers.config(state="disabled")

        # Sync the scroll position of the text area and line numbers
            on_scroll()


        # Sync Scroll Position
        def on_scroll(*args):
            line_numbers.yview_moveto(text_area.yview()[0])


        # File Menu Functions
        def new_file():
            text_area.delete("1.0", "end")
            current_file = None
            text_modified = False
            update_line_numbers()

        def open_file():
            file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if file_path:
                with open(file_path, "r") as file:
                    text_area.delete("1.0", "end")
                    text_area.insert("1.0", file.read())
                current_file = file_path
                text_modified = False
                update_line_numbers()

        def save_file():
            if current_file:
                with open(current_file, "w") as file:
                    file.write(text_area.get("1.0", "end-1c"))
                text_modified = False
            else:
                save_as_file()

        def save_as_file():
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if file_path:
                with open(file_path, "w") as file:
                    file.write(text_area.get("1.0", "end-1c"))
                current_file = file_path
                text_modified = False

         # Edit Menu Functions
        def cut_text():
            text_area.event_generate("<<Cut>>")

        def copy_text():
            text_area.event_generate("<<Copy>>")

        def paste_text():
            text_area.event_generate("<<Paste>>")

        def select_all():
            text_area.tag_add("sel", "1.0", "end")

        def insert_time_date():
            now = datetime.now()
            text_area.insert("insert", now.strftime("%H:%M %Y-%m-%d"))

        def undo():
            text_area.edit_undo()

        def redo():
            text_area.edit_redo()

        def find_text():
            find_window = tk.Toplevel(notepad_window)
            find_window.title("Find")

            tk.Label(find_window, text="Find:").pack(pady=5)
            find_entry = tk.Entry(find_window)
            find_entry.pack(pady=5)

            def find():
                text_area.tag_remove("found", "1.0", "end")
                search_term = find_entry.get()
                if search_term:
                    start = "1.0"
                    while True:
                        start = text_area.search(search_term, start, stopindex="end")
                        if not start:
                            break
                        end = f"{start}+{len(search_term)}c"
                        text_area.tag_add("found", start, end)
                        start = end
                    text_area.tag_config("found", background="yellow")

            tk.Button(find_window, text="Find", command=find).pack(pady=5)

        def replace_text():
            replace_window = tk.Toplevel(notepad_window)
            replace_window.title("Replace")

            tk.Label(replace_window, text="Find:").pack(pady=5)
            find_entry = tk.Entry(replace_window)
            find_entry.pack(pady=5)

            tk.Label(replace_window, text="Replace with:").pack(pady=5)
            replace_entry = tk.Entry(replace_window)
            replace_entry.pack(pady=5)

            def replace():
                search_term = find_entry.get()
                replace_term = replace_entry.get()
                if search_term and replace_term:
                    content = text_area.get("1.0", "end-1c")
                    new_content = content.replace(search_term, replace_term)
                    text_area.delete("1.0", "end")
                    text_area.insert("1.0", new_content)

            tk.Button(replace_window, text="Replace", command=replace).pack(pady=5)

        # Format Menu Functions
        def toggle_word_wrap(self):
            if text_area.cget("wrap") == "none":
                text_area.config(wrap="word")
            else:
                text_area.config(wrap="none")

        def change_font():
            font_window = tk.Toplevel(notepad_window)
            font_window.title("Font Settings")

            font_family = tk.StringVar(value="ubuntu sans")
            font_size = tk.IntVar(value= font_size)

            tk.Label(font_window, text="Font Family:").pack(pady=5)
            font_family_entry = tk.Entry(font_window, textvariable=font_family)
            font_family_entry.pack(pady=5)

            tk.Label(font_window, text="Font Size:").pack(pady=5)
            font_size_entry = tk.Entry(font_window, textvariable=font_size)
            font_size_entry.pack(pady=5)

            def apply_font():
                font_size = font_size.get()
                new_font = (font_family.get(),font_size)
                text_area.config(font=new_font)
                font_window.destroy()

            tk.Button(font_window, text="Apply", command=apply_font).pack(pady=10)

            # View Menu Functions
        def zoom_in():
            font_size = font_size + 2
            text_area.config(font=("ubuntu sans", font_size))

        def zoom_out():
            font_size = max(8, font_size - 2)
            text_area.config(font=("ubuntu sans", font_size))

        def toggle_theme():
            if text_area.cget("bg") == "#3C3C3C":
                text_area.config(bg="white", fg="black")
                line_numbers.config(bg="lightgray", fg="black")
            else:
                text_area.config(bg="#3C3C3C", fg="white")
                line_numbers.config(bg="#2C2C2C", fg="white")

        # Text Modified Event
        def on_text_modified(event=None):
            text_modified = True
            text_area.edit_modified(False)

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