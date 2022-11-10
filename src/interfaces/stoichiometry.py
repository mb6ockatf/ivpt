"""Stoichiometry sums window"""
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFontDatabase, QFont
from molmass import Formula
from essential import configuration
from database import DatabaseSelect
from .font import Font


class SumRow:
    """Store formula data"""
    def __init__(self, number: int, input: QLineEdit, **labels):
        """
        :number: int, row's number in the window
        :input: QLineEdit, formula input field
        :labels["mass"]: QLabel, formula mass label
        :labels["atoms"]: QLabel, formula atoms label
        """
        self.number = number
        self.input = input
        self.mass_label = labels["mass"]
        self.atoms_label = labels["atoms"]
        self.config = configuration()

    def count_mass(self):
        """Set masses label's text"""
        text = self.input.text()
        text = text.upper()
        self.input.setText(text)
        accuracy = int(self.config["accuracy"])
        try:
            formula = Formula(text)
            mass = formula.mass
            mass = str(mass)
            mass = round(float(mass), ndigits=-accuracy)
            self.mass_label.setText(str(mass))
        except Exception:
            self.mass_label.setText("ERROR")

    def count_atoms(self):
        """Set atoms label's text"""
        text = self.input.text()
        self.input.setText(text.upper())
        text = self.input.text()
        try:
            formula = Formula(text)
            atoms = str(formula.atoms)
            self.atoms_label.setText(atoms)
        except Exception:
            self.atoms_label.setText("ERROR")


class StoichiometryPage(QMainWindow):
    """Stoichiometry sums' window"""
    def __init__(self):
        super().__init__()
        width = 1200
        height = 800
        size_sheet = {"normal": 20, "large": 30, "giant": 90}
        self.setGeometry(300, 200, width, height)
        self.setWindowTitle("Stoichiometry")
        font = Font(name="Ubuntu Regular", **size_sheet)
        QFontDatabase.addApplicationFont(font.path)
        self.regular_font = QFont(font.name, font.normal_size)
        self.config = configuration()
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        self.database = DatabaseSelect(self.config)
        self.rows_count = 0
        self.rows = []
        self.mass_column_label = QLabel(self)
        self.atom_column_label = QLabel(self)
        self.eval_button = QPushButton("eval", self)
        self.eval_button.clicked.connect(lambda: self.count_mass(self.rows))
        self.eval_button.clicked.connect(lambda: self.count_atoms(self.rows))
        self.add_row_btn = QPushButton("+", self)
        self.create_column_labels()
        self.create_eval_button()
        self.create_add_row_button()
        self.draw_line()

    def create_column_labels(self):
        self.mass_column_label.setText("mass")
        self.mass_column_label.move(420, 20)
        self.mass_column_label.setFont(self.regular_font)
        self.atom_column_label.setText("atoms")
        self.atom_column_label.move(600, 20)
        self.atom_column_label.setFont(self.regular_font)

    def create_eval_button(self):
        self.eval_button.resize(100, 100)
        self.eval_button.move(800, 600)
        self.eval_button.show()

    def create_add_row_button(self):
        self.add_row_btn.resize(350, 30)
        self.add_row_btn.move(30, 30)
        self.add_row_btn.clicked.connect(self.draw_line)

    def draw_line(self):
        input_frame = QLineEdit(self)
        input_frame.resize(350, 100)
        input_frame.move(30, 100 + 120 * self.rows_count)
        placeholder = """Enter formula. For instance, H2SO4"""
        input_frame.setPlaceholderText(placeholder)
        input_frame.show()
        mass_label = QLabel(self)
        mass_label.resize(300, 100)
        mass_label.move(400, 100 + 120 * self.rows_count)
        mass_label.setFont(self.regular_font)
        mass_label.show()
        atom_label = QLabel(self)
        atom_label.resize(300, 100)
        atom_label.move(660, 100 + 120 * self.rows_count)
        atom_label.setFont(self.regular_font)
        atom_label.show()
        self.add_row_btn.move(30, 100 + 120 * (self.rows_count + 1))
        labels = {"mass": mass_label, "atoms": atom_label}
        data = SumRow(self.rows_count, input_frame, **labels)
        self.rows += [data]
        if self.rows_count == 3:
            self.add_row_btn.hide()
        self.rows_count += 1

    def count_mass(self, rows: list):
        for line in rows:
            line.count_mass()

    def count_atoms(self, rows: list):
        for line in rows:
            line.count_atoms()
