#!/usr/bin/env python3
"""ElementPage class"""
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QFont
from config import configuration
from database import DatabaseSelect
from .hyper_link_label import HyperlinkLabel


class ElementPage(QWidget):
	"""Create element's window"""
	def __init__(self, element: str, number: int):
		super().__init__()
		self.element = element
		self.number = number
		self.config = configuration()
		self.database = DatabaseSelect(self.config)
		self.init_ui()
		self.show_congregation()
		self.show_link()

	def init_ui(self):
		self.setGeometry(300, 300, 400, 300)
		self.setWindowTitle(self.element)
		self.show_static_labels()
		data = self.database.select_basic_params(self.number)[0]
		self.name_label = QLabel(self)
		self.name_label.setText(data[0])
		self.name_label.move(30, 30)
		self.name_label.setFont(QFont('Mono', 20))

		self.abb_label = QLabel(self)
		self.abb_label.setText(self.element)
		self.abb_label.move(250, 0)
		self.abb_label.setFont(QFont('Mono', 90))

		self.mass_value_label = QLabel(self)
		self.mass_value_label.setText(str(data[1]))
		self.mass_value_label.move(120, 130)
		self.mass_value_label.setFont(QFont('Mono', 15))

		self.group_value_label = QLabel(self)
		self.group_value_label.setText(str(data[2]))
		self.group_value_label.move(120, 160)
		self.group_value_label.setFont(QFont('Mono', 15))

		self.period_value_label = QLabel(self)
		self.period_value_label.setText(str(data[3]))
		self.period_value_label.move(120, 190)
		self.period_value_label.setFont(QFont('Mono', 15))

	def show_static_labels(self):
		self.period_label = QLabel(self)
		self.period_label.setText("Period:")
		self.period_label.move(30, 190)
		self.period_label.setFont(QFont('Mono', 15))

		self.group_label = QLabel(self)
		self.group_label.setText("Group:")
		self.group_label.move(30, 160)
		self.group_label.setFont(QFont('Mono', 15))

		self.mass_label = QLabel(self)
		self.mass_label.setText("Mass:")
		self.mass_label.move(30, 130)
		self.mass_label.setFont(QFont('Mono', 15))

		self.energy_level_label = QLabel(self)
		self.energy_level_label.setText("Energy level:")
		self.energy_level_label.move(30, 100)
		self.energy_level_label.setFont(QFont('Mono', 15))

	def show_congregation(self):
		data = self.database.select_congregation(self.number)[0]
		if data[3]:
			self.gas_label = QLabel(self)
			self.gas_label.setText("GAS")
			self.gas_label.move(250, 220)
			self.gas_label.setFont(QFont('Mono', 40))
		if data[0]:
			if data[1]:
				self.amphoteric_metal_label = QLabel(self)
				self.amphoteric_metal_label.setText("AMPHOTERIC METAL")
				self.amphoteric_metal_label.move(40, 220)
				self.amphoteric_metal_label.setFont(QFont('Mono', 25))
			else:
				self.metal_label = QLabel(self)
				self.metal_label.setText("METAL")
				self.metal_label.move(40, 220)
				self.metal_label.setFont(QFont('Mono', 40))
		self.energy_level_value_label = QLabel(self)
		self.energy_level_value_label.setText(str(data[2]))
		self.energy_level_value_label.move(190, 100)
		self.energy_level_value_label.setFont(QFont('Mono', 15))
		if data[4]:
			self.semiconductor_label = QLabel(self)
			self.semiconductor_label.setText("SEMICONDUCTOR")
			self.semiconductor_label.move(40, 270)
			self.semiconductor_label.setFont(QFont('Mono', 22))

	def show_link(self):
		data = self.database.select_links(self.number)[0][0]
		link_template = "<a href={0}>{1}</a>"
		self.wiki_label = HyperlinkLabel(self)
		self.wiki_label.setText(link_template.format(data, "read more"))
		self.wiki_label.move(275, 275)
