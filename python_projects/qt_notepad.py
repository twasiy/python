import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QFontDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class ModernNotepad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)
        
        self.setWindowTitle("Notepad")
        self.setGeometry(100, 100, 800, 600)
        
        self.createMenuBar()
        self.show()
    
    def createMenuBar(self):
        menuBar = self.menuBar()
        
        fileMenu = menuBar.addMenu("File")
        editMenu = menuBar.addMenu("Edit")
        formatMenu = menuBar.addMenu("Format")
        
        # File actions
        newAction = QAction("New", self)
        newAction.triggered.connect(self.newFile)
        fileMenu.addAction(newAction)
        
        openAction = QAction("Open", self)
        openAction.triggered.connect(self.openFile)
        fileMenu.addAction(openAction)
        
        saveAction = QAction("Save", self)
        saveAction.triggered.connect(self.saveFile)
        fileMenu.addAction(saveAction)
        
        saveAsAction = QAction("Save As", self)
        saveAsAction.triggered.connect(self.saveFileAs)
        fileMenu.addAction(saveAsAction)
        
        fileMenu.addSeparator()
        
        exitAction = QAction("Exit", self)
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)
        
        # Edit actions
        undoAction = QAction("Undo", self)
        undoAction.triggered.connect(self.textEdit.undo)
        editMenu.addAction(undoAction)
        
        redoAction = QAction("Redo", self)
        redoAction.triggered.connect(self.textEdit.redo)
        editMenu.addAction(redoAction)
        
        editMenu.addSeparator()
        
        cutAction = QAction("Cut", self)
        cutAction.triggered.connect(self.textEdit.cut)
        editMenu.addAction(cutAction)
        
        copyAction = QAction("Copy", self)
        copyAction.triggered.connect(self.textEdit.copy)
        editMenu.addAction(copyAction)
        
        pasteAction = QAction("Paste", self)
        pasteAction.triggered.connect(self.textEdit.paste)
        editMenu.addAction(pasteAction)
        
        # Format actions
        fontAction = QAction("Font", self)
        fontAction.triggered.connect(self.selectFont)
        formatMenu.addAction(fontAction)
        
    def newFile(self):
        self.textEdit.clear()
    
    def openFile(self):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textEdit.setText(file.read())
    
    def saveFile(self):
        if not hasattr(self, 'currentFile') or not self.currentFile:
            self.saveFileAs()
        else:
            with open(self.currentFile, 'w', encoding='utf-8') as file:
                file.write(self.textEdit.toPlainText())
    
    def saveFileAs(self):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File As", "", "Text Files (*.txt);;All Files (*)", options=options)
        if filePath:
            self.currentFile = filePath
            self.saveFile()
    
    def selectFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    notepad = ModernNotepad()
    sys.exit(app.exec_())
