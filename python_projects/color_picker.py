from PyQt5.QtWidgets import QApplication, QWidget, QColorDialog, QLabel, QVBoxLayout, QFrame, QPushButton, QScrollArea,QTextEdit
from PyQt5.QtGui import QFont, QColor
import sys

def rgb_to_cmyk(r, g, b):
    # Dummy implementation for the sake of completeness
    if (r == 0) and (g == 0) and (b == 0):
        return 0, 0, 0, 100
    c = 1 - r / 255.
    m = 1 - g / 255.
    y = 1 - b / 255.
    min_cmy = min(c, m, y)
    c = (c - min_cmy) / (1 - min_cmy)
    m = (m - min_cmy) / (1 - min_cmy)
    y = (y - min_cmy) / (1 - min_cmy)
    k = min_cmy
    return int(c * 100), int(m * 100), int(y * 100), int(k * 100)

def rgb_to_hsl(r, g, b):
    # Dummy implementation for the sake of completeness
    r /= 255.
    g /= 255.
    b /= 255.
    max_color = max(r, g, b)
    min_color = min(r, g, b)
    l = (max_color + min_color) / 2
    if max_color == min_color:
        s = 0
        h = 0
    else:
        if l < 0.5:
            s = (max_color - min_color) / (max_color + min_color)
        else:
            s = (max_color - min_color) / (2.0 - max_color - min_color)
        if r == max_color:
            h = (g - b) / (max_color - min_color)
        elif g == max_color:
            h = 2.0 + (b - r) / (max_color - min_color)
        else:
            h = 4.0 + (r - g) / (max_color - min_color)
    h = (h * 60) % 360
    if h < 0:
        h += 360
    return int(h), int(s * 100), int(l * 100)

class ColorPicker(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Modern Color Picker")
        self.setGeometry(100, 100, 500, 500)
        self.setStyleSheet("background-color: #1E1E1E; color: #FFFFFF; font-family: Arial;")
        
        self.layout = QVBoxLayout()
        
        self.color_palettes = QVBoxLayout()
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        
        self.scroll_content = QWidget()
        self.scroll_content.setLayout(self.color_palettes)
        
        self.scroll_area.setWidget(self.scroll_content)
        
        self.pick_color_button = QPushButton("Pick a Color", self)
        self.pick_color_button.setStyleSheet("background-color: #444; padding: 10px; border-radius: 5px;")
        self.pick_color_button.setFont(QFont("Arial", 12))
        self.pick_color_button.clicked.connect(self.add_color)
        
        self.layout.addWidget(self.pick_color_button)
        self.layout.addWidget(self.scroll_area)
        
        self.setLayout(self.layout)
    
    def add_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            r, g, b, _ = color.getRgb()
            color_hex = color.name()
            c, m, y, k = rgb_to_cmyk(r, g, b)
            h, s, l = rgb_to_hsl(r, g, b)
            
            color_display = QFrame(self)
            color_display.setStyleSheet(f"background: {color_hex}; border-radius: 10px; border: 2px solid #444;")
            color_display.setFixedHeight(50)
            
            color_label = QTextEdit(
                f"<b>HEX:</b> {color_hex}<br>"
                f"<b>RGB:</b> {r}, {g}, {b}<br>"
                f"<b>HSL:</b> {h}, {s}%, {l}%<br>"
                f"<b>CMYK:</b> {c}%, {m}%, {y}%, {k}%",
                self
            )
            color_label.setFont(QFont("ubuntu sans", 15))
            color_label.setStyleSheet("padding: 10px; background-color: #2E2E2E; border-radius: 10px;")
            
            color_layout = QVBoxLayout()
            color_layout.addWidget(color_display)
            color_layout.addWidget(color_label)
            
            self.color_palettes.addLayout(color_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ColorPicker()
    window.show()
    sys.exit(app.exec_())