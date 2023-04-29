#!/usr/bin/env python3


def fill_database_tables(config_object: dict):
    if not config_object:
        raise ValueError("No configuration object has been specified")
    table = ElementsTable()
    sql_executor = DatabaseInsert(config_object)
    for row in table.get_basic_info():
        sql_executor.insert_basic_info(**row)
    for row in table.get_basic_params():
        sql_executor.insert_basic_params(**row)
    for row in table.get_congregation():
        sql_executor.insert_congregation(**row)
    for row in table.get_links():
        sql_executor.insert_links(**row)
    sql_executor.close()


if __name__ == '__main__':
    import sys
    if sys.version_info < (3, 11):
        raise DeprecationWarning("Python >= 3.11 required")
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtGui import QFontDatabase, QFont
    from interfaces import Main, LoadingPage, Font
    from elements import ElementsTable
    from essential import setup_logging, configuration
    from database import DatabaseCreateTable, DatabaseInsert, DatabaseSelect
    app = QApplication(sys.argv)
    loading_window = LoadingPage()
    loading_window.show()
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
    setup_logging(config["log"])
    loading_window.hide()
    main_window = Main()
    main_window.show()
    sys.exit(app.exec())