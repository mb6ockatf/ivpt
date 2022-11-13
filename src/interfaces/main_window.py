"""Main window class"""
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QFontDatabase, QFont
from .font import Font
from database import DatabaseSelect
from essential.config import configuration
from .element_window import ElementPage
from .stoichiometry import StoichiometryPage


class Main(QMainWindow):
    """Create perodic table window"""
    def __init__(self):
        super().__init__()
        font = self.get_fonts()
        self.regular_font = QFont(font.name, font.normal_size)
        self.symbol_font = QFont(font.name, font.giant_size)
        self.exclamation_font = QFont(font.name, font.large_size)
        self.setGeometry(0, 0, 1280, 740)
        self.setWindowTitle("Periodic table of elements")
        self.config = configuration()
        self.database = DatabaseSelect(self.config)
        self.stoichiometry_button = QPushButton("Stoichiometry", self)
        self.widgets = []
        self.buttons = []
        self.init_ui()

    def get_fonts(self):
        size_sheet = {"normal": 10, "large": 30, "giant": 90}
        font = Font(name="Ubuntu Regular", **size_sheet)
        QFontDatabase.addApplicationFont(font.path)
        return font

    def init_ui(self):
        """Set up the window"""
        for column in range(18):
            text = str(column + 1)
            self.btn = QLabel(text, self)
            self.btn.move(170 + 60 * column, 20)
            self.btn.setFont(self.regular_font)
            self.buttons += [self.btn]
        for row in range(7):
            text = str(row + 1)
            self.btn = QLabel(text, self)
            self.btn.move(110, 80 + 60 * row)
            self.btn.setFont(self.regular_font)
            self.buttons += [self.btn]
        basic_info = self.database.select_basic_info()
        table = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                 [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
        table += [[1 for _ in range(18)] for _ in range(2)]
        table += [[1 for _ in range(32)] for _ in range(2)]
        for row_index, row in enumerate(table):
            for column_index, column in enumerate(row):
                if not column:
                    continue
                number, name = basic_info.pop(0)
                btn_text = str(number) + " " + str(name)
                self.btn = QPushButton(btn_text, self)
                self.btn.setFont(self.regular_font)
                self.btn.resize(60, 60)
                match number:
                    case _ if 57 < number < 72:
                        self.btn.move(150 + 60 * column_index, 500)
                    case _ if 89 < number < 104:
                        self.btn.move(150 + 60 * column_index, 560)
                    case _:
                        if column_index > 17 or row_index in (5, 6) and column_index == 17:
                            column_index -= 14
                        self.btn.move(150 + 60 * column_index, 70 + 60 * row_index)
                self.btn.name = name
                self.btn.number = number
                self.btn.clicked.connect(self.open_element_page)
                self.buttons += [self.btn]
        self.database.close()
        self.stoichiometry_button.resize(140, 70)
        self.stoichiometry_button.move(1100, 640)
        self.stoichiometry_button.clicked.connect(self.show_stoichiometry_window)

    def show_stoichiometry_window(self):
        """Open stoichiometry operations' window"""
        widget = StoichiometryPage()
        widget.show()
        self.widgets += [widget]

    def open_element_page(self):
        """Open element's page window when button is pressed"""
        sender = self.sender()
        widget = ElementPage(sender.name, sender.number)
        widget.show()
        self.widgets += [widget]
