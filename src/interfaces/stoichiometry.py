"""Stoichiometry sums window"""

from PyQt5.QtWidgets import QMainWindow, QLabel, QTextEdit, QPushButton
from PyQt5.QtGui import QFontDatabase, QFont
from essential import configuration
from database import DatabaseSelect
from .font import Font


class StoichiometryPage(QMainWindow):
    """Stoichiometry sums' window"""
    def __init__(self):
        super().__init__()
        width = 1200
        height = 800
        self.slots = 10
        self.setGeometry(300, 300, width, height)
        self.setWindowTitle("Stoichiometry")
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        self.rows_count = 0
        self.things = []
        self.add_row_btn = QPushButton("+", self)
        self.add_row_btn.resize(350, 30)
        self.add_row_btn.move(30, 30)
        self.add_row_btn.clicked.connect(self.draw_line)

    def draw_line(self):
        self.input_frame = QTextEdit(self)
        self.input_frame.resize(350, 100)
        self.input_frame.move(30, 30 + 120 * self.rows_count)
        placeholder = """Enter formula
For instance, H2SO4"""
        self.input_frame.setPlaceholderText(placeholder)
        self.input_frame.show()
        self.eval_button = QPushButton("eval", self)
        self.eval_button.resize(100, 100)
        self.eval_button.move(400, 30 + 120 * (self.rows_count))
        self.eval_button.show()
        self.add_row_btn.move(30, 30 + 120 * (self.rows_count + 1))
        self.things += [self.input_frame]
        self.things += [self.eval_button]
        self.rows_count += 1
        if self.rows_count == 6:
            self.add_row_btn.hide()
