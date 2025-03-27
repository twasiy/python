import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import time
import threading
from plyer import notification
import json
import webbrowser
import os
from datetime import datetime

class TaskNotifier:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Notifier")
        self.root.geometry("800x700")
        self.root.configure(bg="#1e272e")
        
        self.reminders = self.load_reminders()
        
        title_label = tk.Label(root, text="Task Notifier", bg="#1e272e", fg="white", font=("Arial", 18, "bold"))
        title_label.pack(pady=10)
        
        self.time_label = tk.Label(root, text="", bg="#1e272e", fg="white", font=("Arial", 14, "bold"))
        self.time_label.pack(pady=5)
        self.update_time()
        
        frame = tk.Frame(root, bg="#485460")
        frame.pack(pady=10, padx=20, fill=tk.X)
        
        tk.Label(frame, text="Task:", bg="#485460", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
        self.task_entry = tk.Entry(frame, width=40, font=("Arial", 12))
        self.task_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(frame, text="Interval (minutes):", bg="#485460", fg="white", font=("Arial", 12, "bold")).grid(row=1, column=0, padx=10, pady=5)
        self.interval_entry = tk.Entry(frame, width=10, font=("Arial", 12))
        self.interval_entry.grid(row=1, column=1, padx=10, pady=5)
        
        button_frame = tk.Frame(root, bg="#1e272e")
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="Add Reminder", command=self.add_reminder, bg="#27ae60", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Delete Selected", command=self.delete_reminder, bg="#c0392b", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5).grid(row=0, column=1, padx=5)
        
        search_frame = tk.Frame(root, bg="#1e272e")
        search_frame.pack(pady=10)
        
        tk.Button(search_frame, text="Search Google", command=self.search_google, bg="#3498db", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5).grid(row=0, column=0, padx=5)
        tk.Button(search_frame, text="Search YouTube", command=self.search_youtube, bg="#e74c3c", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5).grid(row=0, column=1, padx=5)
        tk.Button(search_frame, text="Search Facebook", command=self.search_facebook, bg="#2980b9", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5).grid(row=0, column=2, padx=5)
        tk.Button(search_frame, text="Open File", command=self.open_file, bg="#f1c40f", fg="black", font=("Arial", 12, "bold"), padx=10, pady=5).grid(row=0, column=3, padx=5)
        
        self.style = ttk.Style()
        self.style.configure("Treeview", font=("Arial", 12), background="#34495e", fieldbackground="#34495e", foreground="white")
        self.style.map("Treeview", background=[("selected", "#00a8ff")])
        
        self.tree = ttk.Treeview(root, columns=("Task", "Interval"), show="headings")
        self.tree.heading("Task", text="Task")
        self.tree.heading("Interval", text="Interval (min)")
        self.tree.column("Task", width=400)
        self.tree.column("Interval", width=100)
        self.tree.pack(pady=10)
        
        self.load_listbox()
        
        threading.Thread(target=self.start_reminders, daemon=True).start()
    
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
            messagebox.showwarning("Invalid Input", "Please enter a valid task and time in minutes.")
    
    def delete_reminder(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a reminder to delete.")
            return
        
        for item in selected_item:
            task = self.tree.item(item, "values")[0]
            if task in self.reminders:
                del self.reminders[task]
            self.tree.delete(item)
        
        self.save_reminders()
    
    def search_google(self):
        webbrowser.open("https://www.google.com/")
    
    def search_youtube(self):
        webbrowser.open("https://www.youtube.com/")
    
    def search_facebook(self):
        webbrowser.open("https://www.facebook.com/")
    
    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            os.startfile(file_path)
    
    def save_reminders(self):
        with open("reminders.json", "w") as f:
            json.dump(self.reminders, f)
    
    def load_reminders(self):
        try:
            with open("reminders.json", "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def load_listbox(self):
        for task, interval in self.reminders.items():
            self.tree.insert("", tk.END, values=(task, interval))

root = tk.Tk()
app = TaskNotifier(root)
root.mainloop()
