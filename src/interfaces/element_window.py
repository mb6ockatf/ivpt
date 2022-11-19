"""ElementPage class"""
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QFontDatabase, QFont
from essential import configuration
from database import DatabaseSelect
from .hyper_link_label import HyperlinkLabel
from .font import Font


class ElementPage(QWidget):
    """Create element's window"""
    def __init__(self, element: str, number: int):
        super().__init__()
        font = self.get_fonts()
        self.regular_font = QFont(font.name, font.normal_size)
        self.symbol_font = QFont(font.name, font.giant_size)
        self.exclamation_font = QFont(font.name, font.large_size)
        self.wiki_label_y = 275
        self.element = element
        self.number = number
        self.config = configuration()
        self.database = DatabaseSelect(self.config)
        self.name_label = QLabel(self)
        self.abb_label = QLabel(self)
        self.mass_value_label = QLabel(self)
        self.group_value_label = QLabel(self)
        self.period_value_label = QLabel(self)
        self.period_label = QLabel(self)
        self.group_label = QLabel(self)
        self.mass_label = QLabel(self)
        self.energy_level_label = QLabel(self)
        self.wiki_label = HyperlinkLabel(self)
        self.gas_label = QLabel(self)
        self.metal_label = QLabel(self)
        self.amphoteric_metal_label = QLabel(self)
        self.energy_level_value_label = QLabel(self)
        self.semiconductor_label = QLabel(self)
        self.init_ui()
        self.show_static_labels()
        self.show_congregation()
        self.show_link()

    def get_fonts(self):
        size_sheet = {"normal": 20, "large": 30, "giant": 90}
        font = Font(name="Ubuntu Regular", **size_sheet)
        QFontDatabase.addApplicationFont(font.path)
        return font


    def init_ui(self):
        """Show data labels"""
        width = 500
        height = 400
        self.setGeometry(300, 300, width, height)
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        self.setWindowTitle(self.element)
        data = self.database.select_basic_params(self.number)
        data = data[0]
        self.name_label.setText(data[0])
        self.name_label.move(30, 30)
        self.name_label.setFont(self.regular_font)

        self.abb_label.setText(self.element)
        self.abb_label.move(250, 0)
        self.abb_label.setFont(self.symbol_font)

        self.mass_value_label.setText(str(data[1]))
        self.mass_value_label.move(120, 130)
        self.mass_value_label.setFont(self.regular_font)

        self.group_value_label.setText(str(data[2]))
        self.group_value_label.move(120, 160)
        self.group_value_label.setFont(self.regular_font)

        self.period_value_label.setText(str(data[3]))
        self.period_value_label.move(120, 190)
        self.period_value_label.setFont(self.regular_font)

    def show_static_labels(self):
        """Show static labels"""
        self.period_label.setText("Period:")
        self.period_label.move(30, 190)
        self.period_label.setFont(self.regular_font)

        self.group_label.setText("Group:")
        self.group_label.move(30, 160)
        self.group_label.setFont(self.regular_font)

        self.mass_label.setText("Mass:")
        self.mass_label.move(30, 130)
        self.mass_label.setFont(self.regular_font)

        self.energy_level_label.setText("Energy level:")
        self.energy_level_label.move(30, 100)
        self.energy_level_label.setFont(self.regular_font)

    def show_congregation(self):
        """Show extended element's information"""
        data = self.database.select_congregation(self.number)
        data = data[0]
        data = {"metal":         data[0],
                "amphoteric":    data[1],
                "energy_levels": data[2],
                "gas":           data[3],
                "semiconductor": data[4]}
        if data["gas"]:
            self.gas_label.setText("GAS")
            self.gas_label.move(250, 220)
            self.gas_label.setFont(self.exclamation_font)
        if data["metal"]:
            if data["amphoteric"]:
                self.amphoteric_metal_label.setText("AMPHOTERIC METAL")
                self.amphoteric_metal_label.move(40, 220)
                self.amphoteric_metal_label.setFont(self.exclamation_font)
            else:
                self.metal_label.setText("METAL")
                self.metal_label.move(40, 220)
                self.metal_label.setFont(self.exclamation_font)
        energy_levels = str(data["energy_levels"])
        self.energy_level_value_label.setText(energy_levels)
        self.energy_level_value_label.move(190, 100)
        self.energy_level_value_label.setFont(self.regular_font)
        if data["semiconductor"]:
            self.semiconductor_label.setText("SEMICONDUCTOR")
            self.wiki_label_y += 50
            self.semiconductor_label.move(40, 270)
            self.semiconductor_label.setFont(self.exclamation_font)

    def show_link(self):
        """Show link to element's wiki page"""
        data_tuple = self.database.select_links(self.number)[0]
        data = data_tuple[0]
        link_template = "<a href={0}>{1}</a>"
        decorated_link = link_template.format(data, "read more")
        self.wiki_label.setText(decorated_link)
        self.wiki_label.move(275, self.wiki_label_y)
