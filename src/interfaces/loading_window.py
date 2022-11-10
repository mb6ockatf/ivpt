"""LoadingPage class"""
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QFontDatabase, QFont
from .font import Font


class LoadingPage(QMainWindow):
    """Create element's window"""
    def __init__(self):
        super().__init__()
        font = self.get_fonts()
        self.exclamation_font = QFont(font.name, font.large_size)
        width = 500
        height = 400
        self.setGeometry(300, 300, width, height)
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        self.setWindowTitle("Loading")
        self.wait_label = QLabel(self)
        self.create_wait_label()

    def get_fonts(self):
        size_sheet = {"normal": 20, "large": 30, "giant": 90}
        font = Font(name="Ubuntu Regular", **size_sheet)
        QFontDatabase.addApplicationFont(font.path)
        return font

    def create_wait_label(self):
        self.wait_label.resize(300, 300)
        self.wait_label.setText("Please wait")
        self.wait_label.move(60, 30)
        self.wait_label.setFont(self.exclamation_font)
