from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.slider import Slider
from kivy.uix.spinner import Spinner
from kivy.uix.switch import Switch
from kivy.uix.filechooser import FileChooserListView
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.dropdown import DropDown
from kivy.uix.carousel import Carousel
import random
import os

# Custom ImageButton
class ImageButton(ButtonBehavior, Image):
    pass

# Main Screen
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # Title
        self.label = Label(text="Custom OS - Home", font_size=24)
        layout.add_widget(self.label)
        
        # Buttons for navigation
        self.file_explorer_button = Button(text="File Explorer", size_hint=(1, 0.2))
        self.file_explorer_button.bind(on_press=self.switch_to_file_explorer)
        layout.add_widget(self.file_explorer_button)
        
        self.settings_button = Button(text="Settings", size_hint=(1, 0.2))
        self.settings_button.bind(on_press=self.switch_to_settings)
        layout.add_widget(self.settings_button)
        
        self.task_manager_button = Button(text="Task Manager", size_hint=(1, 0.2))
        self.task_manager_button.bind(on_press=self.switch_to_task_manager)
        layout.add_widget(self.task_manager_button)
        
        # Notification button
        self.notification_button = Button(text="Show Notification", size_hint=(1, 0.2))
        self.notification_button.bind(on_press=self.show_notification)
        layout.add_widget(self.notification_button)
        
        self.add_widget(layout)
    
    def switch_to_file_explorer(self, instance):
        self.manager.current = 'file_explorer'
    
    def switch_to_settings(self, instance):
        self.manager.current = 'settings'
    
    def switch_to_task_manager(self, instance):
        self.manager.current = 'task_manager'
    
    def show_notification(self, instance):
        popup = Popup(title="Alert",
                      content=Label(text="This is a notification!"),
                      size_hint=(0.5, 0.3))
        popup.open()

# File Explorer Screen
class FileExplorerScreen(Screen):
    def __init__(self, **kwargs):
        super(FileExplorerScreen, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # File chooser
        self.file_chooser = FileChooserListView(path=os.getcwd())
        layout.add_widget(self.file_chooser)
        
        # Back button
        self.back_button = Button(text="Back to Home", size_hint=(1, 0.2))
        self.back_button.bind(on_press=self.switch_to_main_screen)
        layout.add_widget(self.back_button)
        
        self.add_widget(layout)
    
    def switch_to_main_screen(self, instance):
        self.manager.current = 'main'

# Settings Screen
class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # Theme toggle
        self.theme_label = Label(text="Dark Mode", font_size=18)
        layout.add_widget(self.theme_label)
        
        self.theme_switch = Switch(active=False)
        self.theme_switch.bind(active=self.toggle_theme)
        layout.add_widget(self.theme_switch)
        
        # Volume slider
        self.volume_label = Label(text="Volume", font_size=18)
        layout.add_widget(self.volume_label)
        
        self.volume_slider = Slider(min=0, max=100, value=50)
        self.volume_slider.bind(value=self.update_volume)
        layout.add_widget(self.volume_slider)
        
        # Back button
        self.back_button = Button(text="Back to Home", size_hint=(1, 0.2))
        self.back_button.bind(on_press=self.switch_to_main_screen)
        layout.add_widget(self.back_button)
        
        self.add_widget(layout)
    
    def toggle_theme(self, instance, value):
        if value:
            Window.clearcolor = (0.1, 0.1, 0.1, 1)  # Dark theme
        else:
            Window.clearcolor = (1, 1, 1, 1)  # Light theme
    
    def update_volume(self, instance, value):
        print(f"Volume set to: {int(value)}")
    
    def switch_to_main_screen(self, instance):
        self.manager.current = 'main'

# Task Manager Screen
class TaskManagerScreen(Screen):
    def __init__(self, **kwargs):
        super(TaskManagerScreen, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # Simulated tasks
        self.tasks = [
            {"name": "System Process", "cpu": random.randint(1, 100)},
            {"name": "File Explorer", "cpu": random.randint(1, 100)},
            {"name": "Web Browser", "cpu": random.randint(1, 100)},
        ]
        
        # Task list
        self.task_list = GridLayout(cols=2, spacing=10, size_hint_y=None)
        self.task_list.bind(minimum_height=self.task_list.setter('height'))
        
        for task in self.tasks:
            self.task_list.add_widget(Label(text=task["name"], size_hint_y=None, height=40))
            self.task_list.add_widget(Label(text=f"CPU: {task['cpu']}%", size_hint_y=None, height=40))
        
        # Scrollable task list
        scroll_view = ScrollView(size_hint=(1, 0.8))
        scroll_view.add_widget(self.task_list)
        layout.add_widget(scroll_view)
        
        # Refresh button
        self.refresh_button = Button(text="Refresh Tasks", size_hint=(1, 0.2))
        self.refresh_button.bind(on_press=self.refresh_tasks)
        layout.add_widget(self.refresh_button)
        
        # Back button
        self.back_button = Button(text="Back to Home", size_hint=(1, 0.2))
        self.back_button.bind(on_press=self.switch_to_main_screen)
        layout.add_widget(self.back_button)
        
        self.add_widget(layout)
    
    def refresh_tasks(self, instance):
        self.task_list.clear_widgets()
        for task in self.tasks:
            self.task_list.add_widget(Label(text=task["name"], size_hint_y=None, height=40))
            self.task_list.add_widget(Label(text=f"CPU: {task['cpu']}%", size_hint_y=None, height=40))
    
    def switch_to_main_screen(self, instance):
        self.manager.current = 'main'

# Main App
class CustomOSUI(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(FileExplorerScreen(name='file_explorer'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(TaskManagerScreen(name='task_manager'))
        return sm

if __name__ == '__main__':
    CustomOSUI().run()
