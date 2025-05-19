import sys
import time
import pytesseract
import pyperclip
from PIL import Image
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QFileDialog, QTextEdit, QMessageBox, QProgressBar
)
from PyQt5.QtGui import QFont, QPixmap, QPalette, QColor
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve

# Optional DOCX support
try:
    from docx import Document
    HAS_DOCX = True
except ImportError:
    HAS_DOCX = False
    print("Warning: Install 'python-docx' to enable Save to Word feature.")


class OCRWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image to Text Extractor")
        self.setGeometry(100, 100, 900, 650)
        self.extracted_text = ""

        self.setStyleSheet("""
            QMainWindow { background-color: #2b2b2b; }
            QLabel, QTextEdit, QPushButton, QProgressBar {
                color: #ffffff;
                font-size: 14px;
            }
            QTextEdit {
                background-color: #3c3f41;
                border: 1px solid #555;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #4a4a4a;
                border-radius: 8px;
                padding: 10px;
            }
            QPushButton:hover { background-color: #5e5e5e; }
            QPushButton:pressed { background-color: #3a3a3a; }
            QProgressBar {
                background-color: #3c3f41;
                border: 1px solid #555;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk { background-color: #1e90ff; }
        """)

        self.init_ui()

        # Check for Tesseract installation
        try:
            pytesseract.get_tesseract_version()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Tesseract not found:\n{e}")
            sys.exit(1)

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        self.label = QLabel("Select an image to extract text")
        self.label.setFont(QFont("Arial", 14, QFont.Bold))
        self.main_layout.addWidget(self.label, alignment=Qt.AlignCenter)

        # Image and Text area
        content_layout = QHBoxLayout()
        self.image_label = QLabel("No image selected")
        self.image_label.setFixedSize(350, 350)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("border: 2px solid #555; border-radius: 10px; background-color: #3c3f41;")
        content_layout.addWidget(self.image_label)

        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        self.text_area.setFixedSize(450, 350)
        content_layout.addWidget(self.text_area)
        self.main_layout.addLayout(content_layout)

        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.main_layout.addWidget(self.progress_bar)

        # Buttons
        btn_layout = QHBoxLayout()
        self.select_button = QPushButton("Select Image")
        self.select_button.clicked.connect(self.select_image)
        btn_layout.addWidget(self.select_button)

        self.copy_button = QPushButton("Copy to Clipboard")
        self.copy_button.clicked.connect(self.copy_text)
        btn_layout.addWidget(self.copy_button)

        if HAS_DOCX:
            self.save_button = QPushButton("Save to Word")
            self.save_button.clicked.connect(self.save_to_word)
            btn_layout.addWidget(self.save_button)

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_text)
        btn_layout.addWidget(self.clear_button)

        self.main_layout.addLayout(btn_layout)

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.tiff)"
        )
        if not file_path:
            return

        try:
            self.progress_bar.setVisible(True)
            self.label.setText("Processing...")
            QApplication.processEvents()

            for i in range(0, 101, 25):
                self.progress_bar.setValue(i)
                QApplication.processEvents()
                time.sleep(0.05)

            img = Image.open(file_path).convert("RGB")
            self.extracted_text = pytesseract.image_to_string(img)

            pixmap = QPixmap(file_path).scaled(
                self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
            self.image_label.setPixmap(pixmap)

            self.text_area.setText(self.extracted_text or "No text found in the image.")
            self.label.setText(f"Processed: {file_path.split('/')[-1]}")
            self.progress_bar.setValue(100)
            self.progress_bar.setVisible(False)

        except Exception as e:
            self.label.setText("Select an image to extract text")
            self.image_label.setText("No image selected")
            self.text_area.clear()
            self.progress_bar.setVisible(False)
            QMessageBox.critical(self, "Error", str(e))

    def copy_text(self):
        if self.extracted_text.strip():
            pyperclip.copy(self.extracted_text)
            QMessageBox.information(self, "Copied", "Text copied to clipboard!")
        else:
            QMessageBox.warning(self, "Warning", "No text to copy!")

    def save_to_word(self):
        if not self.extracted_text.strip():
            QMessageBox.warning(self, "Warning", "No text to save!")
            return

        file_path, _ = QFileDialog.getSaveFileName(self, "Save as Word", "", "Word Files (*.docx)")
        if file_path:
            try:
                doc = Document()
                doc.add_paragraph(self.extracted_text)
                doc.save(file_path)
                QMessageBox.information(self, "Saved", f"Saved to {file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))

    def clear_text(self):
        self.extracted_text = ""
        self.text_area.clear()
        self.image_label.clear()
        self.image_label.setText("No image selected")
        self.label.setText("Select an image to extract text")

    def animate_button(self, button):
        anim = QPropertyAnimation(button, b"geometry")
        anim.setDuration(100)
        original = button.geometry()
        anim.setStartValue(original)
        anim.setEndValue(original.adjusted(-5, -5, 5, 5))
        anim.setEasingCurve(QEasingCurve.InOutQuad)
        anim.start()
        anim.finished.connect(lambda: button.setGeometry(original))


def main():
    app = QApplication(sys.argv)
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(43, 43, 43))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(60, 63, 65))
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(74, 74, 74))
    palette.setColor(QPalette.ButtonText, Qt.white)
    app.setPalette(palette)

    window = OCRWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
