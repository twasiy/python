import tkinter as tk
from tkinter import filedialog, messagebox, font
from datetime import datetime

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        self.root.geometry("1000x700")

        # Variables
        self.current_file = None
        self.text_modified = False
        self.font_size = 12  # Default font size

        # Text Frame
        text_frame = tk.Frame(root)
        text_frame.pack(fill=tk.BOTH, expand=True)

        # Line Numbers
        self.line_numbers = tk.Text(text_frame, width=4, padx=5, pady=5, bg="#2C2C2C", fg="white", state="disabled")
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        # Text Area
        self.text_area = tk.Text(text_frame, wrap="word", font=("Consolas", self.font_size), bg="#3C3C3C", fg="white", undo=True)
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = tk.Scrollbar(text_frame, command=self.on_scroll)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area.config(yscrollcommand=scrollbar.set)

        # Bind Events
        self.text_area.bind("<KeyRelease>", self.update_line_numbers)
        self.text_area.bind("<MouseWheel>", self.on_scroll)
        self.text_area.bind("<Button-4>", self.on_scroll)
        self.text_area.bind("<Button-5>", self.on_scroll)
        self.text_area.bind("<<Modified>>", self.on_text_modified)

        # Menu Bar
        menubar = tk.Menu(root)

        # File Menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Edit Menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.undo, accelerator="Ctrl+Z")
        edit_menu.add_command(label="Redo", command=self.redo, accelerator="Ctrl+Y")
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=self.cut_text, accelerator="Ctrl+X")
        edit_menu.add_command(label="Copy", command=self.copy_text, accelerator="Ctrl+C")
        edit_menu.add_command(label="Paste", command=self.paste_text, accelerator="Ctrl+V")
        edit_menu.add_command(label="Select All", command=self.select_all, accelerator="Ctrl+A")
        edit_menu.add_separator()
        edit_menu.add_command(label="Find", command=self.find_text, accelerator="Ctrl+F")
        edit_menu.add_command(label="Replace", command=self.replace_text, accelerator="Ctrl+H")
        edit_menu.add_separator()
        edit_menu.add_command(label="Time/Date", command=self.insert_time_date, accelerator="F5")
        menubar.add_cascade(label="Edit", menu=edit_menu)

        # Format Menu
        format_menu = tk.Menu(menubar, tearoff=0)
        format_menu.add_command(label="Word Wrap", command=self.toggle_word_wrap)
        format_menu.add_command(label="Font", command=self.change_font)
        menubar.add_cascade(label="Format", menu=format_menu)

        # View Menu
        view_menu = tk.Menu(menubar, tearoff=0)
        view_menu.add_command(label="Zoom In", command=self.zoom_in, accelerator="Ctrl++")
        view_menu.add_command(label="Zoom Out", command=self.zoom_out, accelerator="Ctrl+-")
        view_menu.add_separator()
        view_menu.add_command(label="Dark/Light Mode", command=self.toggle_theme)
        menubar.add_cascade(label="View", menu=view_menu)

        root.config(menu=menubar)

        # Initialize Line Numbers
        self.update_line_numbers()

    # Update Line Numbers
    def update_line_numbers(self, event=None):
        # Get the number of lines in the text area
        lines = self.text_area.get("1.0", "end-1c").split("\n")
        line_count = len(lines)

        # Update the line numbers
        self.line_numbers.config(state="normal")
        self.line_numbers.delete("1.0", "end")
        self.line_numbers.insert("1.0", "\n".join(str(i) for i in range(1, line_count + 1)))
        self.line_numbers.config(state="disabled")

        # Sync the scroll position of the text area and line numbers
        self.on_scroll()

    # Sync Scroll Position
    def on_scroll(self, *args):
        self.line_numbers.yview_moveto(self.text_area.yview()[0])

    # File Menu Functions
    def new_file(self):
        self.text_area.delete("1.0", "end")
        self.current_file = None
        self.text_modified = False
        self.update_line_numbers()

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete("1.0", "end")
                self.text_area.insert("1.0", file.read())
            self.current_file = file_path
            self.text_modified = False
            self.update_line_numbers()

    def save_file(self):
        if self.current_file:
            with open(self.current_file, "w") as file:
                file.write(self.text_area.get("1.0", "end-1c"))
            self.text_modified = False
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get("1.0", "end-1c"))
            self.current_file = file_path
            self.text_modified = False

    # Edit Menu Functions
    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")

    def select_all(self):
        self.text_area.tag_add("sel", "1.0", "end")

    def insert_time_date(self):
        now = datetime.now()
        self.text_area.insert("insert", now.strftime("%H:%M %Y-%m-%d"))

    def undo(self):
        self.text_area.edit_undo()

    def redo(self):
        self.text_area.edit_redo()

    def find_text(self):
        find_window = tk.Toplevel(self.root)
        find_window.title("Find")

        tk.Label(find_window, text="Find:").pack(pady=5)
        find_entry = tk.Entry(find_window)
        find_entry.pack(pady=5)

        def find():
            self.text_area.tag_remove("found", "1.0", "end")
            search_term = find_entry.get()
            if search_term:
                start = "1.0"
                while True:
                    start = self.text_area.search(search_term, start, stopindex="end")
                    if not start:
                        break
                    end = f"{start}+{len(search_term)}c"
                    self.text_area.tag_add("found", start, end)
                    start = end
                self.text_area.tag_config("found", background="yellow")

        tk.Button(find_window, text="Find", command=find).pack(pady=5)

    def replace_text(self):
        replace_window = tk.Toplevel(self.root)
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
                content = self.text_area.get("1.0", "end-1c")
                new_content = content.replace(search_term, replace_term)
                self.text_area.delete("1.0", "end")
                self.text_area.insert("1.0", new_content)

        tk.Button(replace_window, text="Replace", command=replace).pack(pady=5)

    # Format Menu Functions
    def toggle_word_wrap(self):
        if self.text_area.cget("wrap") == "none":
            self.text_area.config(wrap="word")
        else:
            self.text_area.config(wrap="none")

    def change_font(self):
        font_window = tk.Toplevel(self.root)
        font_window.title("Font Settings")

        font_family = tk.StringVar(value="Consolas")
        font_size = tk.IntVar(value=self.font_size)

        tk.Label(font_window, text="Font Family:").pack(pady=5)
        font_family_entry = tk.Entry(font_window, textvariable=font_family)
        font_family_entry.pack(pady=5)

        tk.Label(font_window, text="Font Size:").pack(pady=5)
        font_size_entry = tk.Entry(font_window, textvariable=font_size)
        font_size_entry.pack(pady=5)

        def apply_font():
            self.font_size = font_size.get()
            new_font = (font_family.get(), self.font_size)
            self.text_area.config(font=new_font)
            font_window.destroy()

        tk.Button(font_window, text="Apply", command=apply_font).pack(pady=10)

    # View Menu Functions
    def zoom_in(self):
        self.font_size += 2
        self.text_area.config(font=("Consolas", self.font_size))

    def zoom_out(self):
        self.font_size = max(8, self.font_size - 2)
        self.text_area.config(font=("Consolas", self.font_size))

    def toggle_theme(self):
        if self.text_area.cget("bg") == "#3C3C3C":
            self.text_area.config(bg="white", fg="black")
            self.line_numbers.config(bg="lightgray", fg="black")
        else:
            self.text_area.config(bg="#3C3C3C", fg="white")
            self.line_numbers.config(bg="#2C2C2C", fg="white")

    # Text Modified Event
    def on_text_modified(self, event=None):
        self.text_modified = True
        self.text_area.edit_modified(False)

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()