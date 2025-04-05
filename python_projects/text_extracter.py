import sys
import pytesseract
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QFileDialog,
    QTextEdit,
    QMessageBox,
    QProgressBar,
)
from PyQt5.QtGui import QFont, QPixmap, QPalette, QColor
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PIL import Image
import pyperclip

# Optional: Only import docx if available
try:
    from docx import Document

    HAS_DOCX = True
except ImportError:
    HAS_DOCX = False
    print("Warning: 'python-docx' not available. Save to Word feature disabled.")


class OCRWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image to Text Extractor")
        self.setGeometry(100, 100, 900, 650)

        # Set dark theme
        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #2b2b2b;
            }
            QLabel {
                color: #ffffff;
            }
            QTextEdit {
                background-color: #3c3f41;
                color: #ffffff;
                border: 1px solid #555555;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #4a4a4a;
                color: #ffffff;
                border: none;
                padding: 10px;
                border-radius: 8px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #5e5e5e;
            }
            QPushButton:pressed {
                background-color: #3a3a3a;
            }
            QProgressBar {
                background-color: #3c3f41;
                color: #ffffff;
                border: 1px solid #555555;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #1e90ff;
                border-radius: 3px;
            }
        """
        )

        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setSpacing(20)
        self.main_layout.setContentsMargins(20, 20, 20, 20)

        # Top label
        self.label = QLabel("Select an image to extract text")
        self.label.setFont(QFont("Arial", 14, QFont.Bold))
        self.main_layout.addWidget(self.label, alignment=Qt.AlignCenter)

        # Horizontal layout for image and text
        self.content_layout = QHBoxLayout()
        self.content_layout.setSpacing(20)

        # Image preview area (left side)
        self.image_label = QLabel("No image selected")
        self.image_label.setFixedSize(350, 350)
        self.image_label.setStyleSheet(
            "border: 2px solid #555555; border-radius: 10px; background-color: #3c3f41;"
        )
        self.image_label.setAlignment(Qt.AlignCenter)
        self.content_layout.addWidget(self.image_label)

        # Text area (right side)
        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        self.text_area.setFixedSize(450, 350)
        self.content_layout.addWidget(self.text_area)

        self.main_layout.addLayout(self.content_layout)

        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(0)
        self.progress_bar.setVisible(False)
        self.main_layout.addWidget(self.progress_bar)

        # Buttons layout
        self.button_layout = QHBoxLayout()
        self.button_layout.setSpacing(15)

        self.select_button = QPushButton("Select Image")
        self.select_button.clicked.connect(self.select_image)
        self.button_layout.addWidget(self.select_button)

        self.copy_button = QPushButton("Copy to Clipboard")
        self.copy_button.clicked.connect(self.copy_text)
        self.button_layout.addWidget(self.copy_button)

        if HAS_DOCX:
            self.save_button = QPushButton("Save to Word")
            self.save_button.clicked.connect(self.save_to_word)
            self.button_layout.addWidget(self.save_button)

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_text)
        self.button_layout.addWidget(self.clear_button)

        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addStretch()  # Push content up

        # Variable to store extracted text
        self.extracted_text = ""

        # Check if Tesseract is available
        try:
            pytesseract.get_tesseract_version()
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Tesseract not found: {str(e)}\nPlease install Tesseract OCR (e.g., 'sudo apt install tesseract-ocr' on Linux).",
            )
            sys.exit(1)

    def select_image(self):
        # Create a QFileDialog with preview
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("Image Files (*.png *.jpg *.jpeg *.bmp *.tiff)")
        dialog.setStyleSheet(
            """
            QFileDialog {
                background-color: #2b2b2b;
                color: #ffffff;
            }
            QListView {
                background-color: #3c3f41;
                color: #ffffff;
                border: 1px solid #555555;
            }
        """
        )

        # Add a preview widget
        preview_label = QLabel("No preview available")
        preview_label.setFixedSize(250, 250)
        preview_label.setStyleSheet(
            "border: 2px solid #555555; border-radius: 10px; background-color: #3c3f41;"
        )
        preview_label.setAlignment(Qt.AlignCenter)
        dialog.setMinimumWidth(700)
        dialog.layout().addWidget(preview_label, 1, 3)

        def update_preview(path):
            pixmap = QPixmap(path)
            if not pixmap.isNull():
                scaled_pixmap = pixmap.scaled(
                    preview_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
                )
                preview_label.setPixmap(scaled_pixmap)
            else:
                preview_label.setText("No preview available")

        dialog.currentChanged.connect(update_preview)

        # Show dialog and get selected file
        if dialog.exec_():
            files = dialog.selectedFiles()
            file_path = files[0] if files else None
        else:
            return

        if not file_path:
            return

        try:
            # Show progress bar
            self.progress_bar.setVisible(True)
            self.label.setText("Processing...")
            QApplication.processEvents()

            # Simulate progress (since OCR is fast, this is for effect)
            for i in range(0, 101, 20):
                self.progress_bar.setValue(i)
                QApplication.processEvents()
                import time

                time.sleep(0.1)  # Small delay for visual effect

            # Open and convert image to RGB
            img = Image.open(file_path).convert("RGB")
            self.extracted_text = pytesseract.image_to_string(img)

            # Display image preview
            pixmap = QPixmap(file_path)
            if not pixmap.isNull():
                scaled_pixmap = pixmap.scaled(
                    self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
                )
                self.image_label.setPixmap(scaled_pixmap)
            else:
                self.image_label.setText("Failed to load image preview")

            # Display extracted text
            if self.extracted_text.strip():
                self.text_area.setText(self.extracted_text)
                self.label.setText(f"Text extracted from: {file_path.split('/')[-1]}")
            else:
                self.text_area.setText("No text found in the image.")
                self.label.setText(f"Image loaded: {file_path.split('/')[-1]}")
                QMessageBox.warning(
                    self, "Warning", "No text could be extracted from the image."
                )

            self.progress_bar.setValue(100)
            self.progress_bar.setVisible(False)
        except Exception as e:
            self.label.setText("Select an image to extract text")
            self.image_label.setText("No image selected")
            self.text_area.clear()
            self.progress_bar.setVisible(False)
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def copy_text(self):
        if self.extracted_text:
            pyperclip.copy(self.extracted_text)
            QMessageBox.information(self, "Success", "Text copied to clipboard!")
            self.animate_button(self.copy_button)
        else:
            QMessageBox.warning(self, "Warning", "No text to copy!")

    def save_to_word(self):
        if not HAS_DOCX:
            QMessageBox.warning(
                self,
                "Warning",
                "Save to Word feature unavailable. Install 'python-docx'.",
            )
            return

        if not self.extracted_text:
            QMessageBox.warning(self, "Warning", "No text to save!")
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Word Document", "", "Word Files (*.docx)"
        )
        if not file_path:
            return

        try:
            doc = Document()
            doc.add_paragraph(self.extracted_text)
            doc.save(file_path)
            QMessageBox.information(self, "Success", f"Text saved to {file_path}!")
            self.animate_button(self.save_button)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save file: {str(e)}")

    def clear_text(self):
        self.extracted_text = ""
        self.text_area.clear()
        self.image_label.setPixmap(QPixmap())
        self.image_label.setText("No image selected")
        self.label.setText("Select an image to extract text")
        self.animate_button(self.clear_button)

    def animate_button(self, button):
        # Simple scale animation for interactivity
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
    # Set dark palette for native elements
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
