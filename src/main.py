#!/usr/bin/env python3
"""Main module"""
from sys import argv, version_info
from PyQt5.QtWidgets import QApplication
from config import configuration
from database import DatabaseCreateTable, DatabaseInsert, DatabaseSelect
from interfaces import Main
from elements import ElementsTable
from log import setup_logging


def fill_database_tables(config: dict):
	table = ElementsTable()
	database = DatabaseInsert(config)
	for row in table.get_basic_info():
		database.insert_basic_info(**row)
	for row in table.get_basic_params():
		database.insert_basic_params(**row)
	for row in table.get_congregation():
		database.insert_congregation(**row)
	for row in table.get_links():
		database.insert_links(**row)
	database.close()


if __name__ == '__main__':
	if version_info <= (3, 10):
		...
	config = configuration()
	setup_logging(config["log"])
	database = DatabaseCreateTable(config)
	database.create_all_tables()
	database.close()
	database = DatabaseSelect(config)
	rows = database.select_basic_info()
	length = len(rows)
	database.close()
	match length:
		case 0:
			fill_database_tables(config)
		case _ if length > 118 or length > 118:
			database = DatabaseCreateTable(config)
			database.drop_all_tables()
			database.close()
			fill_database_tables(config)
		case 118:
			pass
	app = QApplication(argv)
	window = Main(config)
	window.show()
	exit(app.exec())
